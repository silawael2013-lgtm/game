import argparse
import json
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data" / "notes.json"


def load_notes():
    if not DATA.exists():
        return []
    return json.loads(DATA.read_text(encoding="utf-8"))


def save_notes(items):
    DATA.parent.mkdir(parents=True, exist_ok=True)
    DATA.write_text(
        json.dumps(items, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main():
    parser = argparse.ArgumentParser(description="Notes CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_add = sub.add_parser("add")
    p_add.add_argument("text", type=str)
    sub.add_parser("list")
    args = parser.parse_args()
    if args.cmd == "add":
        text = args.text.strip()
        if not text:
            print("Empty note ignored.")
            return
        notes = load_notes()
        notes.append(text)
        save_notes(notes)
        print("Saved.")
    elif args.cmd == "list":
        notes = load_notes()
        if not notes:
            print("No notes yet.")
        else:
            for i, n in enumerate(notes, start=1):
                print(f"{i}. {n}")


if __name__ == "__main__":
    main()
