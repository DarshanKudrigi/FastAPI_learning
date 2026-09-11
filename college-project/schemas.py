from pydantic import BaseModel, ConfigDict


class StudentCreate(BaseModel):
    name: str
    age: int
    course: str


class StudentResponse(StudentCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
