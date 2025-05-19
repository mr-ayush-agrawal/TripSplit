class Group:
    def __init__(self, group_id: int, group_name: str, owner_id: int):
        self.group_id = group_id
        self.group_name = group_name
        self.owner_id = owner_id
        self.members_id = [] # List of user ids
        self.total_expense = 0
        self.expenses = []
        self.member_balances = {}
    
    def __repr__(self):
        return f"Group({self.group_id}, {self.group_name})"

    def __str__(self):
        return f"Group Name: {self.group_name}\n Members: {self.members_id}"
    
    def add_member(self, user_id):
        if user_id not in self.members_id:
            self.members_id.append(user_id)
            return True
        return False
    def remove_member(self, user_id):
        if user_id in self.members_id:
            self.members_id.remove(user_id)
            return True
        return False
    def get_members(self):
        return self.members_id
    
    # still confused : should there be a logs function here or should be a separate entity

    # Exepsnse work is pending
    def add_expense(self, expense):
        pass
        # making a new expense object
        # self.expenses.append(new_expense)
        # self.total_expense += new_expense.amount
