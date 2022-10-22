from fastapi import FastAPI, Path
from typing import Optional


app = FastAPI()

students = {
    1: {
        "name": "Aloysius",
        "age": 28
    },
    2: {
        "name": "Alex",
        "age": 26
    }
}


@app.get("/")
def index():
    return {"message": "Hello world"}


@app.get("/get-students/{student_id}")
def get_students(student_id: int = Path(None,  description='ID of the students ', gt=0)):
    return students[student_id]


@app.get("/get-student-by-name")
def get_student_by_name(*, name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"message": "data not fount"}
