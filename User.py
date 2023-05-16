class User:
    def __init__(self, login, password, role):
        self.login = login
        self.password = password
        self.role = role

    def __str__(self):
        return f"User(login='{self.login}')"

