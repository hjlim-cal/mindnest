import json
import os
import random


def load_prompts(prompts_path):
    """Load diary prompts from a JSON file.

    Args:
        prompts_path: Absolute path to the prompts JSON file.

    Returns:
        A list of prompt strings.

    Raises:
        FileNotFoundError: If the prompts file does not exist.
        ValueError: If the file is not a valid JSON array.
    """
    if not os.path.exists(prompts_path):
        raise FileNotFoundError(f"Prompts file not found: {prompts_path}")

    with open(prompts_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("prompts.json must contain a JSON array.")

    return data


def run_diary_session(prompts):
    """Run an interactive prompt-selection and writing session.

    Randomly presents one prompt at a time. The user can request a different
    prompt or choose to write about the current one. Once the user writes,
    the session ends and the entry is returned.

    Args:
        prompts: Full list of available prompt strings.

    Returns:
        A dict with 'prompt' and 'response' keys, or None if the user quits.
    """
    pool = prompts[:]
    random.shuffle(pool)
    index = 0

    print("\n=== MindNest ===")

    while True:
        if index >= len(pool):
            pool = prompts[:]
            random.shuffle(pool)
            index = 0

        prompt = pool[index]
        index += 1

        print(f"\nPrompt: {prompt}")
        print("[w] Write about this  [n] Next prompt  [q] Quit")

        while True:
            choice = input("> ").strip().lower()
            if choice in ("w", "n", "q"):
                break
            print("Please enter w, n, or q.")

        if choice == "q":
            return None

        if choice == "n":
            continue

        # choice == "w"
        print("\nWrite your entry. Press Enter twice when done.\n")
        lines = []
        while True:
            line = input()
            if line == "" and lines:
                break
            lines.append(line)

        response = "\n".join(lines).strip()
        return {"prompt": prompt, "response": response}
