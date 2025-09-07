from datetime import datetime, timezone

def current_timestamp() -> str:
    """
    Return the current UTC timestamp in ISO 8601 format with timezone info.

    Returns:
        str: Current timestamp, e.g., "2025-09-07T16:45:30+00:00"
    """
    return datetime.now(timezone.utc).isoformat()
