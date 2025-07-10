from pydantic import BaseModel
from typing import Optional

class Feedback(BaseModel):
    user_name : Optional[str] = None
    topic: str
    description : str
    is_resolved : bool = False