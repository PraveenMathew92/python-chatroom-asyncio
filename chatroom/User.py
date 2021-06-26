from chatroom.ConnectionPool import ConnectionPool


class User:
    def __init__(self, name: str):
        self.name = name
        self.pool: ConnectionPool = None

    def join(self, pool: ConnectionPool):
        pool.add_user(self)
        self.pool = pool

    def leave_pool(self):
        self.pool.remove_user(self)