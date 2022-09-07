from typing import List, Union
from pydantic import BaseModel

class User( BaseModel ):
    id: Union[int, None] = None
    name: str
    email: str
    age: int

class UserList( BaseModel ):
    users: List[ User ] 