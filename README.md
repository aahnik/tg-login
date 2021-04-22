# tg-login

A command line tool to login into Telegram with user or bot accounts.

## Why

Why the need of a seperate tool like `tg-login` ?

## Installation

```shell
pip install tg-login
```

## Usage

```shell
Usage: tg-login [OPTIONS]

  A command line tool to login into Telegram with user or bot accounts.

Options:
  -v, --version  Show version and exit.
  --help         Show this message and exit.
```

The `API_ID` ,`API_HASH`, `BOT_TOKEN`, `PHONE_NO`, can be passed as CLI options, or can be set as environment variables.

Provide either `BOT_TOKEN` or `PHONE_NO`. If both are found, `tg-login` will use the bot account.

`tg-login` by default generates the session string and saves it in your Telegram's Saved Messages.

If the `--session=file` option is provided, it will generated a session file.

## Projects using `tg-login`

- [tgcf](https://github.com/aahnik/tgcf)

Open a PR to add your project here!

## Credits

Made with Telethon.
