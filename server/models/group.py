from pydantic import BaseModel, Field
from typing import Optional, List, Dict

class NewGroup(BaseModel):
    group_name: str
    group_description: Optional[str] = None
    base_currency : Optional[str] = 'INR'

class AddMembersRequest(BaseModel):
    usernames: List[str] = Field(min_length=1, description='List of user_names of the memeber to be added')

class GroupData(BaseModel):
    group_name: str
    group_description: Optional[str]
    base_currency : str = 'INR'
    group_id: str
    owner_username: str
    members: List[str] = Field(description='List of user_names of the group members')
    expenses: Optional[List[str]] = Field( description='List of Expenses by the group members')
    member_balances: Optional[Dict[str, float]] = Field()

    total_expense: float = Field(ge=0, default=0.0)