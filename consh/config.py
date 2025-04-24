import os
import configparser

CONFIG_FILE = "conshrc"
ALIASES = {}

def load_config():
    """Load configuration from conshrc file."""
    config = configparser.ConfigParser()
    if os.path.exists(CONFIG_FILE):
        config.read(CONFIG_FILE)
        if "aliases" in config:
            for name, value in config["aliases"].items():
                ALIASES[name] = value

def get_aliases():
    """Return current aliases."""
    return ALIASES

def set_alias(name, value):
    """Set an alias and save to conshrc"""
    ALIASES[name] = value
    config = configparser.ConfigParser()
    if os.path.exists(CONFIG_FILE):
        config.read(CONFIG_FILE)
    if "aliases" not in config:
        config["aliases"] = {}
    config["aliases"][name] = value
    with open(CONFIG_FILE, "w") as f:
        config.write(f)