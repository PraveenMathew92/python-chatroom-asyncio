class ConnectionPool:
    def __init__(self):
        self.active_users = set()

    def get_all_active_users(self):
        return self.active_users

    def add_user(self, user):
        self.active_users.add(user)

    def remove_user(self, user):
        self.active_users.remove(user)
