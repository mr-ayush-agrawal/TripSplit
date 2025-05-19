from datetime import datetime as dt

class Expense:
    def __init__(self, id, name, amount, date = dt.now().strftime("%d-%m-%Y"), expense_admin = None, bill_image = None):
        self.id = id
        self.name = name
        self.amount = amount
        self.date = date
        self.expense_admin = expense_admin
        self.bill_image = bill_image
        self.paid_by = {}
        self.split = {}

    def __repr__(self):
        return f"Expense(id={self.id}, name='{self.name}', amount={self.amount}, date='{self.date}')"
    
    def update_payees(self, user_map):
        '''
        user_map : dict
            {
                user_id : amount
            }
        '''
        total_amount = sum(user_map.values())
        if total_amount != self.amount:
            return 'Error: Total amount paid by users does not match the expense amount'
        self.paid_by = user_map

    def update_split(self, user_map):
        '''
        user_map : dict
            {
                user_id : amount
            }
        '''
        total_amount = sum(user_map.values())
        if total_amount != self.amount:
            return 'Error: Total amount split by users does not match the expense amount'
        self.split = user_map
    