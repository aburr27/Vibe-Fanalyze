import React, { useState } from "react";

// Local lightweight UI primitives to avoid external dependency issues
function SimpleButton({ children, variant = "solid", className = "", onClick }) {
const base =
    "inline-flex items-center gap-2 px-3 py-2 rounded-md text-sm font-medium focus:outline-none";
const variants = {
    solid: "bg-green-500 hover:bg-green-600 text-white",
    outline: "border border-gray-700 text-gray-100",
    ghost: "bg-transparent text-gray-100 hover:bg-gray-800",
};
return (
    <button
    onClick={onClick}
    className={`${base} ${variants[variant] || variants.solid} ${className}`}
    >
    {children}
    </button>
);
}

function Card({ children, className = "" }) {
return (
    <div className={`rounded-lg shadow-sm ${className}`}> {children} </div>
);
}

function CardContent({ children, className = "p-4" }) {
return <div className={className}>{children}</div>;
}

export default function VibeFanalyzeDashboard() {
const [chatOpen, setChatOpen] = useState(false);

const leagues = ["NBA", "NFL", "MLB", "WNBA", "UFC", "NHL", "MLS"];

const samplePredictions = [
    { game: "Lakers vs. Warriors", confidence: 72, sport: "NBA" },
    { game: "Cowboys vs. Eagles", confidence: 65, sport: "NFL" },
    { game: "Yankees vs. Red Sox", confidence: 59, sport: "MLB" },
];

return (
    <div className="flex h-screen bg-gray-950 text-gray-100">
      {/* Sidebar */}
    <aside className="w-64 bg-gray-900 p-4 flex flex-col">
        <h1 className="text-2xl font-bold mb-6 text-green-400">Vibe‑Fanalyze</h1>

        <nav className="space-y-2">
        {leagues.map((league) => (
            <SimpleButton
            key={league}
            variant="ghost"
            className="w-full justify-start text-left"
            onClick={() => console.log(`Filter: ${league}`)}
            >
            {league}
            </SimpleButton>
        ))}
        </nav>

        <div className="mt-auto">
        <p className="text-xs text-gray-500 mt-6">© 2025 Vibe‑Fanalyze</p>
        </div>
    </aside>

      {/* Main Content */}
    <main className="flex-1 p-6 overflow-y-auto">
        <header className="flex items-center justify-between mb-6">
        <h2 className="text-xl font-semibold">Dashboard</h2>
        <SimpleButton variant="outline" onClick={() => setChatOpen(!chatOpen)}>
            {chatOpen ? (
            <span aria-hidden>✕</span>
            ) : (
            <span aria-hidden>💬</span>
            )}{" "}
            Chatbot
        </SimpleButton>
        </header>

        <section className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {samplePredictions.map((p) => (
            <Card key={p.game} className="bg-gray-800 border border-gray-700">
            <CardContent className="p-4">
                <h3 className="text-lg font-semibold">{p.game}</h3>
                <p className="text-sm text-gray-400">{p.sport}</p>
                <div className="mt-2 text-green-400 font-bold">
                {p.confidence}% Confidence
                </div>
            </CardContent>
            </Card>
        ))}
        </section>

        {/* Placeholder for additional sections */}
        <section className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-4">
        <Card className="bg-gray-800 border border-gray-700">
            <CardContent>
            <h4 className="font-semibold">Live Feed</h4>
            <p className="text-sm text-gray-400">No live data connected yet.</p>
            </CardContent>
        </Card>

        <Card className="bg-gray-800 border border-gray-700">
            <CardContent>
            <h4 className="font-semibold">Recent Reports</h4>
            <p className="text-sm text-gray-400">No reports available.</p>
            </CardContent>
        </Card>
        </section>
    </main>

      {/* Chatbot Panel */}
    {chatOpen && (
        <aside className="w-80 bg-gray-900 p-4 border-l border-gray-800 flex flex-col">
        <h3 className="text-lg font-bold mb-2">VibeBot</h3>
        <div className="flex-1 bg-gray-800 rounded p-2 overflow-y-auto text-sm">
            <p className="text-gray-400 italic">Ask me about any game, player, or prediction...</p>
        </div>

        <form
            onSubmit={(e) => {
            e.preventDefault();
            const input = e.currentTarget.elements.namedItem(
                "vibebot-input"
            );
            if (input && typeof input === "object" && "value" in input) {
                // @ts-ignore
                const value = input.value.trim();
                if (value) {
                console.log("VibeBot query:", value);
                  // simple echo behavior placeholder
                alert(`VibeBot received: ${value}`);
                  // clear input
                  // @ts-ignore
                input.value = "";
                }
            }
            }}
            className="mt-2"
        >
            <input
            name="vibebot-input"
            type="text"
            placeholder="Type a question..."
            className="w-full bg-gray-800 border border-gray-700 rounded p-2 text-sm text-gray-100 focus:outline-none"
            />
            <div className="mt-2 text-right">
            <SimpleButton type="submit">Send</SimpleButton>
            </div>
        </form>
        </aside>
    )}
    </div>
);
}
