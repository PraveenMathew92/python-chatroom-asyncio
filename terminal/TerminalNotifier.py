import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from chatroom.Notifier import Notifier
from chatroom.User import User


class TerminalNotifier(Notifier):
    def __init__(self, writer):
        self.writer = writer

    def send_message(self, sender: User, message):
        self.writer.write(f'[{sender.name}] {message}'.encode())

    def new_user_notification(self, newuser: User):
        self.writer.write(f'[NEW USER] {newuser.name} has joined the chatroom\n'.encode())

    def user_removed_notification(self, user):
        self.writer.write(f'[USER LEFT] {user.name} has left the chatroom\n'.encode())
