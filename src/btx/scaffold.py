from pathlib import Path

PROJECT_FOLDERS = [
    "docs",
    "src",
    "tests",
    "scripts",
    "notebooks",
    "data/raw",
    "data/processed",
]


def create_project(name: str):
    root = Path(name)

    if root.exists():
        print(f"❌ Project '{name}' already exists.")
        return

    for folder in PROJECT_FOLDERS:
        (root / folder).mkdir(parents=True, exist_ok=True)

    (root / "README.md").write_text(f"# {name}\n")
    (root / "requirements.txt").write_text("")
    (root / ".gitignore").write_text(
        ".venv/\n__pycache__/\n*.pyc\n.vscode/\n"
    )

    print(f"✅ Project '{name}' created successfully!")