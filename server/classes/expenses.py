from datetime import datetime 
from pydantic import BaseModel,Field, model_validator, computed_field
from typing import List, Optional, Dict


class Expense(BaseModel):
    expense_id : str
    group_id : str
    paid_by : Dict[str, float] = Field(min_length=1, description='Expense paid by which user and how much, Minimum 1 user to pay')  # user_id
    borrowed_by : Dict[str, float] = Field(min_length=1, description='Expense borrowed by which user and how much, Minimum 1 user to pay')  # user_id
    currency : Optional[str] = Field(default='INR', description='Currency in which the expense is done')
    conversion_rate: Optional[float] = Field(
        default=1, 
        description="Convsion rate from curreny to the base currency",
        example = "If base currency is INR and expense is done in USD then this would be 85"
    )
    date : datetime = datetime.now().strftime("%d-%m-%Y")
    expense_admin : str # UserId

    @computed_field
    @property
    def expense_amount(self):
        return sum(self.paid_by.values())

    @model_validator(mode= 'after')
    def check_expense(cls, values):
        if sum(values.paid_by.values()) != sum(values.borrowed_by.values()):
            raise ValueError('Total amount borrowed is not equal to Total amount paid')
        return values



# class Expense_test:
#     def __init__(self, id, name, amount, expense_admin = None, bill_image = None):
#         self.id = id
#         self.name = name
#         self.amount = amount
#         self.expense_admin = expense_admin
#         self.bill_image = bill_image
#         self.paid_by = {}
#         self.split = {}

#     def __repr__(self):
#         return f"Expense(id={self.id}, name='{self.name}', amount={self.amount}, date='{self.date}')"
    
#     def update_payees(self, user_map):
#         '''
#         user_map : dict
#             {
#                 user_id : amount
#             }
#         '''
#         total_amount = sum(user_map.values())
#         if total_amount != self.amount:
#             return 'Error: Total amount paid by users does not match the expense amount'
#         self.paid_by = user_map

#     def update_split(self, user_map):
#         '''
#         user_map : dict
#             {
#                 user_id : amount
#             }
#         '''
#         total_amount = sum(user_map.values())
#         if total_amount != self.amount:
#             return 'Error: Total amount split by users does not match the expense amount'
#         self.split = user_map
    