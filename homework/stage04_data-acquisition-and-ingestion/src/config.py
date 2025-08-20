import os
from dotenv import load_dotenv, find_dotenv

def load_env():
    load_dotenv(find_dotenv())

def get_key(name: str, default=None):
    return os.getenv(name, default)
