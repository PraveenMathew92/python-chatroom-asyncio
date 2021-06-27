from chatroom.Notifier import Notifier


class ChatRoom:
    def __init__(self):
        self.users_with_notifiers = {}

    def get_all_active_users(self):
        return self.users_with_notifiers.keys()

    def add_user(self, user):
        notifiers = filter(None, self.users_with_notifiers.values())
        for notifier in notifiers:
            notifier.new_user_notification(user)
        self.users_with_notifiers[user] = None

    def remove_user(self, user):
        del self.users_with_notifiers[user]

    def add_user_notifier(self, user, notifier: Notifier):
        self.users_with_notifiers[user] = notifier

    def send_message(self, user, message):
        notifiers = filter(None, self.users_with_notifiers.values())
        for notifier in notifiers:
            notifier.send_message(message)
