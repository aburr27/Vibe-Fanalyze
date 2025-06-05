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
    return 0.0
