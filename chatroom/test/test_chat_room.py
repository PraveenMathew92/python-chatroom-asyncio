import unittest
from unittest.mock import Mock

from chatroom.ChatRoom import ChatRoom
from chatroom.User import User


class MyTestCase(unittest.TestCase):
    def test_add_user_notifies_others(self):
        chatroom = ChatRoom()
        test_user_1 = User("test-user-1")
        test_user_2 = User("test-user-2")
        notifier = Mock()
        test_user_1.join(chatroom)
        chatroom.add_user_notifier(test_user_1, notifier)

        chatroom.add_user(test_user_2)
        notifier.new_user_notification.assert_called_with(test_user_2)


if __name__ == '__main__':
    unittest.main()
