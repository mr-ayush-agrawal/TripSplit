from pydantic import BaseModel, Field, computed_field, model_validator
from typing import Optional, List, Dict
from datetime import datetime

class  NewExpense(BaseModel):
    title : str
    description : Optional[str] = Field(default= None, description="Info of the expense")
    amount_original : float = Field(ge=0)
    original_currency : Optional[str] = Field(default=None, description="Currency in which the expense is made")
    exchange_rate : Optional[float] = Field(
        default=1, 
        description="Conversion rate from original currency to the base currency of the group",
        example = "If the group base currency is INR and expense is done in USD then this would be 85"
    )
    paid_by_original : Dict[str, float] = Field(min_length=1, description='Expense paid by which user and how much, Minimum 1 user to pay') # user_id : amount paid
    borrowed_by_original : Dict[str, float] = Field(min_length=1, description='Expense borrowed by which user and how much, Minimum 1 user to pay')  # user_id : amount borrowed

    @model_validator(mode='after')
    def check_expense(cls, self):
        paid_by = self.paid_by_original
        borrowed_by = self.borrowed_by_original

        # Check all paid and borrowed values are >= 0
        for user, amount in {**paid_by, **borrowed_by}.items():
            if amount < 0:
                raise ValueError(f"Amount cannot be negative (found {amount} for user {user})")

        # Check total balance
        total_paid = sum(paid_by.values())
        total_borrowed = sum(borrowed_by.values())
        if abs(total_paid - total_borrowed) > 1e-6:
            raise ValueError('Total amount paid must equal total amount borrowed')

        return self

    
    @computed_field(return_type=Dict[str, float])
    @property
    def paid_by(self) -> Dict[str, float]:
        return {user_id: amount * self.exchange_rate for user_id, amount in self.paid_by_original.items()}

    @computed_field(return_type=Dict[str, float])
    @property
    def borrowed_by(self) -> Dict[str, float]:
        return {user_id: amount * self.exchange_rate for user_id, amount in self.borrowed_by_original.items()}
    
    @computed_field(return_type=float)
    @property
    def amount(self) -> float:
        return self.amount_original * self.exchange_rate


class Expense(NewExpense):
    expense_id : str
    group_id : str
    expense_owner : str #user_name of the user who created the expense