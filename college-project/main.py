from fastapi import FastAPI, HTTPException, status

from database import create_students_table
from models import create_student, get_student, get_students
from schemas import StudentCreate, StudentResponse


app = FastAPI(title="Students API")


create_students_table()


@app.post("/students", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def add_student(student: StudentCreate) -> StudentResponse:
    return create_student(student)


@app.get("/students", response_model=list[StudentResponse])
def list_students() -> list[StudentResponse]:
    return get_students()


@app.get("/students/{student_id}", response_model=StudentResponse)
def read_student(student_id: int) -> StudentResponse:
    student = get_student(student_id)
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    return student
