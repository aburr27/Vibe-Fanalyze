import tkinter as tk
from tkinter import ttk, messagebox
import json
import datetime

EXPORT_CHAT_TITLE = "Export Chat"

class VibeBot:
    """Simple rule-based assistant for Vibe-Fanalyze.
    It can answer basic queries about predictions, players, and provide help.
    This is intentionally local and deterministic so it works offline and is easy to extend.
    """
    def __init__(self, data_source=None):
        # data_source can be a dict or callable providing current predictions/players
        self.data_source = data_source or self._default_data()

    def _default_data(self):
        # lightweight sample data; replace or extend to call your FastAPI backend
        return {
            "predictions": [
                {"id": 1, "game": "Lakers vs. Warriors", "confidence": 72, "sport": "NBA", "pick": "Lakers"},
                {"id": 2, "game": "Cowboys vs. Eagles", "confidence": 65, "sport": "NFL", "pick": "Cowboys"},
                {"id": 3, "game": "Yankees vs. Red Sox", "confidence": 59, "sport": "MLB", "pick": "Yankees"},
            ],
            "players": {
                "lebron": {"name": "LeBron James", "team": "Lakers", "ppg": 27.2, "rpg": 7.4, "apg": 7.1},
                "dak": {"name": "Dak Prescott", "team": "Cowboys", "cmp": "65%", "ypg": 245},
            },
        }

def respond(self, text: str) -> str:
    """Return a short text reply for the given user input."""
    if not text or not text.strip():
        return "Say something — ask for 'help' to see examples."

    t = text.lower()

    if any(k in t for k in ("help", "commands")):
        return self._respond_help()

    if "top predictions" in t or "predictions" in t:
        return self._respond_predictions()

    if any(k in t for k in ("favored", "who is favored", "who's favored")):
        return self._respond_favored(t)

    if t.startswith("player "):
        return self._respond_player(t)

    if "export chat" in t:
        return "EXPORT_CHAT"  # special signal for the UI to handle

    if any(k in t for k in ("hello", "hi")):
        return self._respond_smalltalk()

    return "Sorry, I don't understand that yet. Try 'help' to see what I can do."

def _respond_help(self) -> str:
    return (
        "VibeBot commands:\n"
        "- 'top predictions' — show top predicted games.\n"
        "- 'favored <team or game>' or 'who is favored' — show pick for a game.\n"
        "- 'player <name>' — show sample player stats (e.g., 'player lebron').\n"
        "- 'export chat' — save the current chat to a local file.\n"
    )

def _respond_predictions(self) -> str:
    preds = self.data_source.get("predictions", [])
    if not preds:
        return "No predictions available."
    lines = [f"{p['game']} — {p.get('pick','Unknown')} ({p.get('confidence',0)}% confidence)" for p in preds]
    return "Top predictions:\n" + "\n".join(lines)

def _respond_favored(self, t: str) -> str:
    preds = self.data_source.get("predictions", [])
    for p in preds:
        if p["game"].split()[0].lower() in t or p.get("sport", "").lower() in t or p.get("pick", "").lower() in t:
            return f"{p['game']}: {p['pick']} is favored ({p.get('confidence',0)}% confidence)."
    if not preds:
        return "No predictions available."
    top = max(preds, key=lambda x: x.get("confidence", 0))
    return f"Top pick right now: {top['game']} — {top['pick']} ({top['confidence']}% confidence)."

def _respond_player(self, t: str) -> str:
    name = t.replace("player ", "").strip()
    players = self.data_source.get("players", {})
    key = name.lower()
    if key in players:
        p = players[key]
        stats = ", ".join([f"{k.upper()}: {v}" for k, v in p.items() if k not in ("name",)])
        return f"{p['name']} ({p.get('team','')}) — {stats}"
    return f"No local data for '{name}'. Try 'help' for commands."

def _respond_smalltalk(self) -> str:
    return "Hey! I'm VibeBot — ask me for 'top predictions' or 'player lebron', or type 'help'."


class VibeFanalyzeDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vibe-Fanalyze")
        self.geometry("1100x700")
        self.configure(bg="#121212")

        self.chat_open = False
        # instantiate VibeBot with default sample data
        self.vibebot = VibeBot()
        self.create_sidebar()
        self.create_main_area()
        self.create_chatbot_panel()

    def create_sidebar(self):
        sidebar = tk.Frame(self, bg="#1e1e1e", width=180)
        sidebar.pack(side="left", fill="y")

        tk.Label(sidebar, text="Vibe-Fanalyze", bg="#1e1e1e", fg="#4ade80", font=("Arial", 16, "bold")).pack(pady=10)

        leagues = ["NBA", "NFL", "MLB", "WNBA", "UFC", "NHL", "MLS"]
        for league in leagues:
            btn = tk.Button(sidebar, text=league, bg="#2d2d2d", fg="white", relief="flat", command=lambda l=league: self.filter_league(l))
            btn.pack(fill="x", padx=10, pady=4)

        tk.Label(sidebar, text="© 2025 Vibe-Fanalyze", bg="#1e1e1e", fg="#9ca3af", font=("Arial", 8)).pack(side="bottom", pady=10)

    def create_main_area(self):
        main = tk.Frame(self, bg="#121212")
        main.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        header = tk.Frame(main, bg="#121212")
        header.pack(fill="x", pady=5)

        tk.Label(header, text="Dashboard", bg="#121212", fg="white", font=("Arial", 14, "bold")).pack(side="left")

        self.chat_btn = tk.Button(header, text="💬 Chatbot", command=self.toggle_chatbot, bg="#1e1e1e", fg="white", relief="ridge")
        self.chat_btn.pack(side="right")

        predictions = [
            {"game": "Lakers vs. Warriors", "confidence": 72, "sport": "NBA"},
            {"game": "Cowboys vs. Eagles", "confidence": 65, "sport": "NFL"},
            {"game": "Yankees vs. Red Sox", "confidence": 59, "sport": "MLB"},
        ]

        cards = tk.Frame(main, bg="#121212")
        cards.pack(fill="both", expand=True)

        for p in predictions:
            frame = tk.LabelFrame(cards, text=p["sport"], bg="#1f1f1f", fg="white", labelanchor="n", font=("Arial", 10, "bold"))
            frame.pack(fill="x", pady=5)
            tk.Label(frame, text=p["game"], bg="#1f1f1f", fg="white", font=("Arial", 11)).pack(anchor="w", padx=10, pady=2)
            tk.Label(frame, text=f"{p['confidence']}% Confidence", bg="#1f1f1f", fg="#4ade80", font=("Arial", 10, "bold")).pack(anchor="w", padx=10, pady=2)

        reports = tk.LabelFrame(main, text="Recent Reports", bg="#1f1f1f", fg="white", labelanchor="n")
        reports.pack(fill="both", expand=True, pady=8)
        tk.Label(reports, text="No reports available.", bg="#1f1f1f", fg="#9ca3af").pack(pady=20)

    def create_chatbot_panel(self):
        self.chat_frame = tk.Frame(self, bg="#1e1e1e", width=320)

        tk.Label(self.chat_frame, text="VibeBot", bg="#1e1e1e", fg="white", font=("Arial", 12, "bold")).pack(pady=8)

        self.chat_log = tk.Text(self.chat_frame, bg="#2d2d2d", fg="white", state="disabled", height=25, wrap="word")
        self.chat_log.pack(fill="both", expand=True, padx=5)

        input_frame = tk.Frame(self.chat_frame, bg="#1e1e1e")
        input_frame.pack(fill="x", pady=5)

        self.chat_input = tk.Entry(input_frame, bg="#2d2d2d", fg="white", relief="flat")
        self.chat_input.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        send_btn = tk.Button(input_frame, text="Send", command=self.send_message, bg="#4ade80", fg="black", relief="flat")
        send_btn.pack(side="right", padx=5)

        # Add a small help button
        help_btn = tk.Button(self.chat_frame, text="Help", command=lambda: self.insert_bot_response(self.vibebot.respond("help")), bg="#272727", fg="white", relief="flat")
        help_btn.pack(fill="x", padx=8, pady=6)

    def toggle_chatbot(self):
        if self.chat_open:
            self.chat_frame.pack_forget()
            self.chat_open = False
            self.chat_btn.config(text="💬 Chatbot")
        else:
            self.chat_frame.pack(side="right", fill="y")
            self.chat_open = True
            self.chat_btn.config(text="✕ Close Chat")

def insert_bot_response(self, response_text: str):
    """Insert response_text into the chat log. Handle special signals like EXPORT_CHAT."""
    if response_text == "EXPORT_CHAT":
        self.export_chat()
        return
    self.chat_log.config(state="normal")
    self.chat_log.insert(tk.END, f"VibeBot: {response_text}\n\n")
    self.chat_log.config(state="disabled")
    self.chat_log.see(tk.END)

def send_message(self):
    """Read the input, display the user message, get a response from VibeBot, and display it."""
    msg = self.chat_input.get().strip()
    if not msg:
        return
    # display user message
    self.chat_input.delete(0, tk.END)
    self.chat_log.config(state="normal")
    self.chat_log.insert(tk.END, f"You: {msg}\n")
    self.chat_log.config(state="disabled")
    self.chat_log.see(tk.END)

    # get and display bot response
    self.insert_bot_response(self.vibebot.respond(msg))
def export_chat(self):
    # saves chat to a timestamped local JSON file
    content = self.chat_log.get("1.0", tk.END).strip()
    if not content:
        messagebox.showinfo(EXPORT_CHAT_TITLE, "Chat is empty — nothing to export.")
        return
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"vibebot_chat_{now}.txt"
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        messagebox.showinfo(EXPORT_CHAT_TITLE, f"Chat exported to {filename}")
    except Exception as e:
        messagebox.showerror(EXPORT_CHAT_TITLE, f"Failed to export chat: {e}")

def filter_league(self, league):
    messagebox.showinfo("Filter", f"Filtering data for {league}!")

if __name__ == "__main__":
    app = VibeFanalyzeDashboard()
    app.mainloop()