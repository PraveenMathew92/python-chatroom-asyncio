import unittest
from chatroom.ConnectionPool import ConnectionPool
from chatroom.User import User


class MyTestCase(unittest.TestCase):
    def test_user_joins_pool(self):
        pool = ConnectionPool()
        user = User("test-user-1")
        user.join(pool)
        self.assertTrue(user in pool.get_all_active_users())


if __name__ == '__main__':
    unittest.main()
