from pathlib import Path
import sys

REQUIRED_FIELDS = [
    "# MasterSap Script",
    "# Titolo:",
    "# Autore:",
    "# Licenza:",
    "# Testato su:",
    "# Unità:",
    "# Scopo:",
    "# Input:",
    "# Output:",
    "# Limitazioni:",
]

TARGET_FOLDERS = ["examples", "community", "verified"]


def validate_header(path: Path) -> list[str]:
    errors = []

    try:
        text = path.read_text(encoding="utf-8")
    except Exception as exc:
        return [f"{path}: cannot be read ({exc})"]

    for field in REQUIRED_FIELDS:
        if field not in text:
            errors.append(f"{path}: missing required field '{field}'")

    if "..." in text:
        errors.append(f"{path}: contains placeholder '...'")

    return errors


def main() -> int:
    all_errors = []

    for folder in TARGET_FOLDERS:
        folder_path = Path(folder)
        if not folder_path.exists():
            continue

        for py_file in folder_path.rglob("*.py"):
            all_errors.extend(validate_header(py_file))

    if all_errors:
        print("Header validation failed:\n")
        for error in all_errors:
            print(f"- {error}")
        return 1

    print("All script headers are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
