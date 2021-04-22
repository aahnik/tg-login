import typer
from tg_login import __version__
from typing import Optional
from tg_login.login import login

app = typer.Typer(add_completion=False)

def version_callback(value: bool):
    if value:
        print(__version__)
        raise typer.Exit()

@app.command()
def main(

    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        help="Show version and exit.",
    ),
):
    """ A command line tool to login into Telegram with user or bot accounts. """

    # login()
    print("hello")

