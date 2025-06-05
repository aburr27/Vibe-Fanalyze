def calculate_fantasy_points(stats: dict, league: str = "NBA") -> float:
    if league == "NBA":
        return (
            stats.get("points", 0) +
            1.2 * stats.get("rebounds", 0) +
            1.5 * stats.get("assists", 0) +
            2 * stats.get("steals", 0) +
            2 * stats.get("blocks", 0) -
            stats.get("turnovers", 0)
        )
    elif league == "NFL":
        # Example scoring system for NFL QBs
        return (
            0.04 * stats.get("passing_yards", 0) +
            4 * stats.get("passing_tds", 0) +
            6 * stats.get("rushing_tds", 0) +
            0.1 * stats.get("rushing_yards", 0) -
            2 * stats.get("interceptions", 0)
        )
    # Add other leagues as needed
    return 0.0
