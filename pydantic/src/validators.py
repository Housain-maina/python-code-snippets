from typing import Annotated
from pydantic import BaseModel, ValidationError
from pydantic.functional_validators import AfterValidator


def divisible_by_two(num: int) -> int:
    assert num % 2 == 0, f"{num} is not divisible by 2"
    return num


class Demo(BaseModel):
    number: Annotated[int, AfterValidator(divisible_by_two)]


try:
    print(Demo(number=24))
    """
        Returns: number=24
    """

    print(Demo(number=33))
    """
        Returns:
            1 validation error for Demo
            number
              Assertion failed, 33 is not divisible by 2 [type=assertion_error, input_value=33, input_type=int]
    """

except ValidationError as e:
    print(e)
