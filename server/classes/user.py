class User:
    def __init__(self, user_id: int, username: str, email: str, currency: str = "INR"):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.currency = currency

    def __repr__(self):
        return f"User({self.user_id}, {self.username}, {self.email}, {self.currency})"   