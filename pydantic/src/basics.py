from typing import Literal
from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int
    gender: Literal["male", "female"]


person = Person(name="Hussaini", age=12, gender="male", active=True)
print(person)
"""
    Returns: name='Hussaini' age=12 gender='male'
"""

print(person.model_dump_json())
"""
    Returns: {"name":"Hussaini","age":12,"gender":"male"}
"""
