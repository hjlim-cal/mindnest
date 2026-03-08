import os

from modules.diary import load_prompts, run_diary_session
from modules.storage import save_entry

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPTS_PATH = os.path.join(BASE_DIR, "data", "prompts.json")
ENTRIES_DIR = os.path.join(BASE_DIR, "data", "entries")


def main():
    """Run the MindNest CLI diary session."""
    try:
        prompts = load_prompts(PROMPTS_PATH)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error loading prompts: {e}")
        return

    entry = run_diary_session(prompts)

    if entry is None:
        print("Session ended without saving.")
        return

    try:
        saved_path = save_entry([entry], ENTRIES_DIR)
        print(f"\nEntry saved to: {saved_path}")
    except OSError as e:
        print(f"Error saving entry: {e}")


if __name__ == "__main__":
    main()
