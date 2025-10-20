// charts.js — handles visual analytics for Vibe-Fanalyze

let winChart, bankrollChart;

function renderWinProbChart(ctx, data) {
    if (winChart) winChart.destroy();

    winChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [data.team_a, data.team_b],
            datasets: [{
                label: 'Win Probability (%)',
                data: [data.win_prob_a * 100, data.win_prob_b * 100],
                backgroundColor: ['#1f6feb', '#238636'],
                borderRadius: 6
            }]
        },
        options: {
            plugins: { legend: { display: false } },
            scales: { y: { beginAtZero: true, max: 100 } }
        }
    });
}

function renderBankrollChart(ctx, data) {
    if (bankrollChart) bankrollChart.destroy();

    const steps = Array.from({length: 10}, (_, i) => i + 1);
    const growth = steps.map(i => (1 + data.bet_size) ** i * 100);

    bankrollChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: steps.map(s => `Game ${s}`),
            datasets: [{
                label: 'Bankroll Growth (%)',
                data: growth,
                borderColor: '#f0f6fc',
                backgroundColor: '#1f6feb40',
                tension: 0.3,
                fill: true
            }]
        },
        options: {
            plugins: { legend: { display: true } },
            scales: { y: { beginAtZero: true } }
        }
    });
}

document.addEventListener("DOMContentLoaded", () => {
const sendBtn = document.getElementById("send-btn");
const userInput = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");
const historyPanel = document.getElementById("history");

async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    // Display user message
    chatBox.innerHTML += `<p><strong>You:</strong> ${message}</p>`;
    userInput.value = "";

    // Send to backend
    const response = await fetch("/vibebot", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_query: message })
    });

    const data = await response.json();
    chatBox.innerHTML += `<p class="text-green-400"><strong>VibeBot:</strong> ${data.response}</p>`;
    chatBox.scrollTop = chatBox.scrollHeight;

    // Refresh history panel
    loadHistory();
}

async function loadHistory() {
    const response = await fetch("/api/chats/recent");
    const chats = await response.json();

    historyPanel.innerHTML = "";
    for (const chat of chats) {
    historyPanel.innerHTML += `
        <div class="mb-4 border-b border-gray-700 pb-2">
        <p class="text-sm text-gray-300"><strong>You:</strong> ${chat.user_message}</p>
        <p class="text-xs text-green-400"><strong>VibeBot:</strong> ${chat.bot_response}</p>
        </div>
    `;
    }
}

sendBtn.addEventListener("click", sendMessage);
userInput.addEventListener("keypress", e => { if (e.key === "Enter") sendMessage(); });

  // Auto-refresh history every 10 seconds
setInterval(loadHistory, 10000);
});
