import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from chatroom.Notifier import Notifier
from chatroom.User import User

class TerminalNotifier(Notifier):
    def __init(self, writer):
        self.writer = writer

    def send_message(self, sender: User, message):
        pass

    def new_user_notification(self, newuser: User):
        pass

    def user_removed_notification(self, user):
        pass