# Important message

## This fork is no longer maintained, you can use a simple script that does the job: [telogin](https://github.com/tzagim/telogin)


# tg-login

A command line tool to login into Telegram with user or bot accounts and generate session string.

## Installation

We recommend using [pipx](https://github.com/pypa/pipx) for install tg-login

```shell
pip install pipx # install pipx first
pipx install tg-login # for dependancy isolation
```

## Usage

```shell
Usage: tg-login [OPTIONS]

  A command line tool to login into Telegram with user or bot accounts.

Options:
  --API_ID INTEGER  API ID obtained from my.telegram.org  [env var: API_ID;
                    required]

  --API_HASH TEXT   API HASH obtained from my.telegram.org  [env var:
                    API_HASH; required]

  -v, --version     Show version and exit.
  --help            Show this message and exit.
```

## Repl

You may run this `tg-login` online by using this repl.

[![run on repl](https://docs.replit.com/images/repls/run-on-replit.svg)](https://replit.com/@aahnik/tg-login)

Note:

- A python virtual environment is created before execution and deleted post execution.
- All sensitive user input is hidden.
- The session string is not printed on screen, but sent to user.
