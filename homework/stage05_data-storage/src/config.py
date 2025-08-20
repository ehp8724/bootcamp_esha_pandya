import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

def load_env():
    load_dotenv(find_dotenv())

def get_path(key: str, default: str) -> Path:
    return Path(os.getenv(key, default))