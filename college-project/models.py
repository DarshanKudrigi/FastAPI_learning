from contextlib import closing
from dataclasses import dataclass

from database import get_connection
from schemas import StudentCreate


@dataclass
class StudentRecord:
    id: int
    name: str
    age: int
    course: str


def create_student(student: StudentCreate) -> StudentRecord:
    with closing(get_connection()) as connection:
        cursor = connection.execute(
            "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
            (student.name, student.age, student.course),
        )
        connection.commit()
        student_id = cursor.lastrowid

    return StudentRecord(
        id=student_id,
        name=student.name,
        age=student.age,
        course=student.course,
    )


def get_students() -> list[StudentRecord]:
    with closing(get_connection()) as connection:
        rows = connection.execute(
            "SELECT id, name, age, course FROM students ORDER BY id"
        ).fetchall()

    return [StudentRecord(**dict(row)) for row in rows]


def get_student(student_id: int) -> StudentRecord | None:
    with closing(get_connection()) as connection:
        row = connection.execute(
            "SELECT id, name, age, course FROM students WHERE id = ?",
            (student_id,),
        ).fetchone()

    if row is None:
        return None

    return StudentRecord(**dict(row))
