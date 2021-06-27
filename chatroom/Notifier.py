from chatroom.User import User


class Notifier:
    def send_message(self):
        pass

    def new_user_notification(self, newuser: User):
        pass

    def user_removed_notification(self, user):
        pass