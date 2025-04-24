import os

def get_env_var(key=None):
    """Get environment variable(s)."""
    if key:
        return os.getenv(key, f"Environment variable '{key}' not set")
    return "\n".join(f"{k}={v}" for k, v in os.environ.items())