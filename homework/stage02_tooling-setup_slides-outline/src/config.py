import os
from dotenv import load_dotenv

def load_env():
    """Load environment variables from the .env file."""
    load_dotenv()

def get_key(key: str, default=None):
    """Fetch a config value by name."""
    return os.getenv(key, default)