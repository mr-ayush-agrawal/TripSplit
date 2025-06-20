from pydantic import BaseModel, Field
from typing import Optional

class NewGroup(BaseModel):
    group_name: str
    group_description: Optional[str] = None
    base_currency : Optional[str] = 'INR'

class GroupData(BaseModel):
    group_name: str
    group_description: Optional[str]
    base_currency : str = 'INR'
    group_id: str
    owner_username: str
    members: Optional[list[str]] = Field(default_factory=list, description='List of user_names of the group members')
    expenses: Optional[list[str]] = Field(default_factory=list, description='List of Expenses by the group members')
    member_balances: Optional[dict[str, float]] = Field(default_factory=dict)

    total_expense: float = Field(ge=0, default=0.0)