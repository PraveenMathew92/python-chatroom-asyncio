from chatroom.Notifier import Notifier


class ChatRoom:
    def __init__(self):
        self.users_with_notifiers = {}

    def get_all_active_users(self):
        return self.users_with_notifiers.keys()

    def add_user(self, user):
        add_user_notification_sender = lambda notifier: notifier.new_user_notification(user)
        self.__send_notification_to_all_users(add_user_notification_sender)
        self.users_with_notifiers[user] = None

    def remove_user(self, user):
        del self.users_with_notifiers[user]
        remove_user_notifiaction_sender = lambda notifier: notifier.user_removed_notification(user)
        self.__send_notification_to_all_users(remove_user_notifiaction_sender)

    def add_user_notifier(self, user, notifier: Notifier):
        self.users_with_notifiers[user] = notifier

    def send_message(self, sender, message):
        message_sender = lambda notifier: notifier.send_message(sender, message)
        self.__send_notification_to_all_users(message_sender)

    def __send_notification_to_all_users(self, notifier_function_caller):
        notifiers = filter(None, self.users_with_notifiers.values())
        for notifier in notifiers:
            notifier_function_caller(notifier)
