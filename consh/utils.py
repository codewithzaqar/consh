import os
import time
import datetime

def get_env_var(key=None):
    """Get environment variable(s)."""
    if key:
        return os.getenv(key, f"Environment variable '{key}' not set")
    return "\n".join(f"{k}={v}" for k, v in os.environ.items())

def log_command(command):
    """Log a command to .consh_log."""
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(".consh_log", "a") as f:
            f.write(f"[{timestamp}] {command}\n")
    except Exception:
        pass  # Silent fail to avoid disrupting CLI