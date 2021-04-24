import os
import sys
from logging import warn

from dotenv import load_dotenv
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

load_dotenv()


def login(API_ID, API_HASH):
    print(
        "\nYou are now going to login, and the session string will be sent securely to your telegram account. \nYou need to copy that for future use.\n\n"
    )
    print(
        "If you now login with your phone no, the session string will be saved in you Telgram's Saved Messages.\n"
    )
    print(
        "If you login with a bot account, the bot will send the session string to your username."
    )

    input("\nPress [ENTER] to proceed\n")

    with TelegramClient(StringSession(), API_ID, API_HASH).start() as client:
        session_string = client.session.save()
        message = f"Your session string is: \n\n`{session_string}`\n\nKeep this secret!"

        me = client.get_me()
        print(f"\n\n{me.username}\n\n")
        if me.bot:
            print(
                f"Bot account detected! Open your telegram app, and send /start to {me.username}"
            )
            input("Press [ENTER] after you have send /start\n\n")
            uname = input(
                "What is your telegram username ? \n(the username of the user account from which you sent /start to the bot just now ) \n: "
            )
            confirm = input("Please type your username again: ")
            if uname == confirm:
                input(
                    f"Are you sure your username is {uname} ? Press ENTER to continue. The session string will be sent to you."
                )
                client.send_message(uname, message)
                print(f"The session string has been succesfully sent to {uname}")
            else:
                print(
                    "The username you typed second time did not match with the first time! Quitting.\n\n You can start again!"
                )
                sys.exit(1)
        else:
            client.send_message("me", message)
            print("Open your saved messages in telegram to see your session string!")

        warning = """
        \n\n
        - Keep this string safe! Dont leak it.

        - Anyone with this string can use it to login into your account and do anything they want to to do.

        - For more information about Telethon Session Strings
        \thttps://docs.telethon.dev/en/latest/concepts/sessions.html#string-sessions

        - You can deactivate this session by going to your
        \tTelegram App -> Settings -> Devices -> Active sessions

        """

        print(warning)

    return session_string
