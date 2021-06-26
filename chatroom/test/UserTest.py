import unittest
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


if __name__ == '__main__':
    unittest.main()
