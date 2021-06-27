import asyncio

import sys, os, inspect


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from chatroom.ChatRoom import ChatRoom
from chatroom.User import User
from terminal.TerminalNotifier import TerminalNotifier

CHATROOM = ChatRoom()


async def server_connection(reader, writer):
    writer.write(b"> Enter username: ")
    username = await reader.readuntil(b"\n")

    terminal_notifier = TerminalNotifier(writer)
    user = User(username.decode().rstrip())
    user.join(CHATROOM)
    CHATROOM.add_user_notifier(user, terminal_notifier)

    while True:
        try:
            message = await reader.readuntil(b"\n")
            user.send_message(message.decode())
        except asyncio.exceptions.IncompleteReadError:
            user.leave()
            break


async def main():
    print("Starting Server")
    host = "0.0.0.0"
    port = 8888
    server = await asyncio.start_server(server_connection, host, port)

    async with server:
        print(f"Listening on {host}:{port}")
        await server.serve_forever()


asyncio.run(main())
