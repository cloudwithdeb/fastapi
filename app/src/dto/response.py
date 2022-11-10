
from pydantic import BaseModel
from typing import List

class ResponseModel(BaseModel):

    data: List
    status: bool
    message: str