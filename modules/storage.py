import json
import os
from datetime import datetime


def save_entry(entries, entries_dir):
    """Save a diary session to a JSON file.

    Args:
        entries: List of dicts with 'prompt' and 'response' keys.
        entries_dir: Directory path where entry files are stored.

    Returns:
        The absolute path of the saved file.

    Raises:
        OSError: If the directory cannot be created or the file cannot be written.
    """
    os.makedirs(entries_dir, exist_ok=True)

    now = datetime.now()
    filename = now.strftime("%Y-%m-%d_%H%M%S") + ".json"
    filepath = os.path.join(entries_dir, filename)

    record = {
        "date": now.strftime("%Y-%m-%d"),
        "timestamp": now.isoformat(),
        "entries": entries,
    }

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)

    return filepath
