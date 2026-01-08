import json
import os
from pathlib import Path

# Configurable path via environment variable,
DEFAULT_HISTORY_PATH = os.getenv("CHAT_HISTORY_PATH", "chat_history.json")

def save_chat_history(history, file_path=DEFAULT_HISTORY_PATH):
    try:
        # Error handling and UTF-8 encoding
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error saving history: {e}")

def load_chat_history(file_path=DEFAULT_HISTORY_PATH):
    # Cross-platform path validation using pathlib
    if not Path(file_path).exists():
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        print(f"Error loading history (Invalid data): {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []