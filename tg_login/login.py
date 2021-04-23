import os
import sys

from dotenv import load_dotenv
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

load_dotenv()


def login(API_ID, API_HASH):
    print(
        "\nYou are now going to login, and the session string will be displayed on screen. \nYou need to copy that for future use."
    )

    input("\nPress [ENTER] to proceed \n?")

    with TelegramClient(StringSession(), API_ID, API_HASH).start() as client:
        session_string = client.session.save()

        print("\n\nBelow is your session string ⬇️\n\n")
        print(session_string)
        print("\nAbove is your session string ⬆️\n\n")

    print(
        """

    - Keep this string safe! Dont leak it.

    - Anyone with this string can use it to login into your account and do anything they want to to do.

    - For more information about Telethon Session Strings
    \thttps://docs.telethon.dev/en/latest/concepts/sessions.html#string-sessions

    - You can deactivate this session by going to your
    \tTelegram App -> Settings -> Devices -> Active sessions

    """
    )
    return session_string
