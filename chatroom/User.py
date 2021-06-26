from chatroom.ChatRoom import ChatRoom


class User:
    def __init__(self, name: str):
        self.name = name
        self.chatroom: ChatRoom = None

    def join(self, chatroom: ChatRoom):
        chatroom.add_user(self)
        self.chatroom = chatroom

    def leave(self):
        self.chatroom.remove_user(self)

    def send_message(self, message):
        self.chatroom.send_message(self, message)