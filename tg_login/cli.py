from typing import Optional

import typer
from dotenv import load_dotenv

from tg_login import __version__
from tg_login.login import login

app = typer.Typer(add_completion=False)

load_dotenv()


def version_callback(value: bool):
    if value:
        print(__version__)
        raise typer.Exit()


@app.command()
def main(
    API_ID: int = typer.Option(
        ...,
        "--API_ID",
        help="API ID obtained from my.telegram.org",
        envvar="API_ID",
        prompt="Paste your API ID (input hidden)",
        hide_input=True,
    ),
    API_HASH: str = typer.Option(
        ...,
        "--API_HASH",
        help="API HASH obtained from my.telegram.org",
        envvar="API_HASH",
        prompt="Paste your API HASH (input hidden)",
        hide_input=True,
    ),
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        help="Show version and exit.",
    ),
):
    """ A command line tool to login into Telegram with user or bot accounts. """

    login(API_ID, API_HASH)
