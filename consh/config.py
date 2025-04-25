import os
import configparser
from .utils import get_env_var

CONFIG_FILE = "conshrc"
ALIASES = {}

def load_config():
    """Load configuration from conshrc file with validation."""
    config = configparser.ConfigParser()
    try:
        if os.path.exists(CONFIG_FILE):
            config.read(CONFIG_FILE)
            if "aliases" in config:
                for name, value in config["aliases"].items():
                    if name and value.strip():
                        ALIASES[name] = value
            if "env" in config:
                for key, value in config["env"].items():
                    if key and value.strip():
                        os.environ[key] = value
    except configparser.Error as e:
        print(f"Warning: Invalid conshrc format: {e}")

def get_aliases():
    """Return current aliases."""
    return ALIASES

def set_alias(name, value):
    """Set an alias and save to conshrc"""
    if not name or not value.strip():
        return  # Skip invalid aliases
    ALIASES[name] = value
    config = configparser.ConfigParser()
    try:
        if os.path.exists(CONFIG_FILE):
            config.read(CONFIG_FILE)
        if "aliases" not in config:
            config["aliases"] = {}
        config["aliases"][name] = value
        with open(CONFIG_FILE, "w") as f:
            config.write(f)
    except configparser.Error as e:
        print(f"Warning: Failed to save alias to conshrc: {e}")