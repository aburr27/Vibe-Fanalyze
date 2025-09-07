def format_player_name(first_name: str, last_name: str) -> str:
    """
    Format a player's name with proper title casing.

    Args:
        first_name (str): Player's first name
        last_name (str): Player's last name

    Returns:
        str: Full name in "First Last" format
    """
    if not first_name or not last_name:
        return (first_name or "") + (last_name or "")
    
    # Remove extra spaces and ensure proper title casing
    return f"{first_name.strip().title()} {last_name.strip().title()}"
