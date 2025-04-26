import os
import configparser
from .utils import get_env_var

CONFIG_FILE = "conshrc"
ALIASES = {}
PROMPT = "consh> "

def load_config():
    """Load configuration from conshrc file with validation."""
    global PROMPT
    config = configparser.ConfigParser()
    try:
        if os.path.exists(CONFIG_FILE):
            config.read(CONFIG_FILE)
            if "aliases" in config:
                for name, value in config["aliases"].items():
                    if name and value is not None and value.strip():  # Line 18
                        ALIASES[name] = value
            if "env" in config:
                for key, value in config["env"].items():
                    if key and value is not None and value.strip():
                        os.environ[key] = value
            if "prompt" in config and "PS1" in config["prompt"]:
                prompt = config["prompt"]["PS1"]
                if prompt is not None and prompt.strip():
                    PROMPT = prompt
    except configparser.Error as e:
        print(f"Warning: Invalid conshrc format: {e}")

def get_aliases():
    """Return current aliases."""
    return ALIASES

def set_alias(name, value):
    """Set an alias and save to conshrc."""
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

def get_prompt():
    """Return the current prompt."""
    return PROMPT