# Vibe-Fanalyze MongoDB Collections

### `chat_logs`
- Stores chat history between user and assistant.
- Includes message array and intent context.

### `predictions`
- Stores prediction results for games.
- Includes model name, features used, confidence, and output.

### `raw_event_data`
- Raw game data from external APIs (e.g., Sportradar).
- Keeps JSON payload and metadata like timestamp and game_id.

### `user_profiles`
- Stores preferences for users (optional, for personalization).

### `fantasy_snapshots`
- Per-player snapshot of fantasy points for a given game.
- Useful for fantasy models and history tracking.
