from pydantic import BaseModel, ConfigDict, Field


class CourseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str = Field(max_length=255)
    units: int = Field(ge=0, le=4)
    teacher_name: str = Field(max_length=50)


ai = CourseModel(title="Artificial Intelligence", units=3, teacher_name="Hussaini Usman")

print(ai.model_dump_json())
"""
    Returns: {"title":"Artificial Intelligence","units":3,"teacher_name":"Hussaini Usman"}
"""

algorithm = CourseModel(title="Algorithms Complexity and Analysis", units=3, teacher_name="Hussaini Usman", semester="first")

print(algorithm)
"""
    Returns:
        semester
            Extra inputs are not permitted [type=extra_forbidden, input_value='first', input_type=str]
"""

