from pydantic import BaseModel, Field, computed_field
from typing import List, Optional, Dict
from classes.user import User
from classes.expenses import Expense


class Group(BaseModel):
    group_id : str
    group_name : str
    group_description : str
    owner : User
    members : Optional[List[str]] = None
    expenses : Optional[List[Expense]] = None
    total_expense : float = Field(ge= 0, default=0)
    member_balances : Optional[Dict[str, float]] = None

    # Nees some validation for user_ids

    @computed_field
    @property
    def base_currency(self) -> str:
        return self.owner.currency


# class Group_test:
    
#     def __repr__(self):
#         return f"Group({self.group_id}, {self.group_name})"

#     def __str__(self):
#         return f"Group Name: {self.group_name}\n Members: {self.members_id}"
    
#     def add_member(self, user_id):
#         if user_id not in self.members_id:
#             self.members_id.append(user_id)
#             return True
#         return False
#     def remove_member(self, user_id):
#         if user_id in self.members_id:
#             self.members_id.remove(user_id)
#             return True
#         return False
#     def get_members(self):
#         return self.members_id
    
#     # still confused : should there be a logs function here or should be a separate entity

#     # Exepsnse work is pending
#     def add_expense(self, expense):
#         pass
#         # making a new expense object
#         # self.expenses.append(new_expense)
#         # self.total_expense += new_expense.amount
