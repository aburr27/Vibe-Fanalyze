import datetime

def current_timestamp() -> str:
return datetime.datetime.utcnow().isoformat()