import typer
from rich import print

app = typer.Typer(
    help="🚀 Blocktracex Developer CLI"
)


@app.command()
def version():
    """Show the current CLI version."""
    print("[bold green]🚀 Blocktracex CLI v0.1.0[/bold green]")


@app.command()
def hello(name: str = "Founder"):
    """Say hello."""
    print(f"👋 Welcome to Blocktracex, {name}!")


if __name__ == "__main__":
    app()