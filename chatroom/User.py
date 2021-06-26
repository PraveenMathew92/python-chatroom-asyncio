from chatroom.ConnectionPool import ConnectionPool


class User:
    def __init__(self, name: str):
        self.name = name

    def join(self, pool: ConnectionPool):
        pool.add_user(self)
