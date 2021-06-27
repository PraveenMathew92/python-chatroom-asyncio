import unittest
from unittest.mock import Mock

from chatroom.ChatRoom import ChatRoom
from chatroom.User import User


class MyTestCase(unittest.TestCase):
    def test_user_joins_chatroom(self):
        chat_room = ChatRoom()
        user = User("test-user-1")
        user.join(chat_room)
        self.assertTrue(user in chat_room.get_all_active_users())

    def test_user_leave_joined_chatroom(self):
        chat_room = ChatRoom()
        user = User("test-user-1")
        user.join(chat_room)
        user.leave()
        self.assertFalse(user in chat_room.get_all_active_users())

    def test_user_send_message(self):
        message = "Message from the user"
        chatroom = ChatRoom()
        test_user_1 = User("test-user-1")
        test_user_2 = User("test-user-2")
        test_user_1.join(chatroom)
        test_user_2.join(chatroom)
        notifier = Mock()

        chatroom.add_user_notifier(test_user_2, notifier)

        test_user_1.send_message(message)

        notifier.send_message.assert_called_with(test_user_1, message)


if __name__ == '__main__':
    unittest.main()
