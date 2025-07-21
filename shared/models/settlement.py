from pydantic import BaseModel
from typing import Optional

class NewSettlement(BaseModel):
    paid_by : str
    paid_to : str
    group_id : str
    settlement_id : Optional[str] = None
    amount : float
    # mode : str