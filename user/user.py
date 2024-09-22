class User:
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password

    def __str__(self):
        return f"User: ID {self.user_id} Nume utilizator: {self.username} Email: {self.email} Password: {self.password}"
