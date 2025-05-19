class User:
    def __init__(self, user_id: int, name: str, email: str, currency: str = "INR"):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.currency = currency
        self.hashed_password = None
        self.base_currency = currency

    def __repr__(self):
        return f"User({self.user_id}, {self.name}, {self.email}, {self.currency})"