import imp
from fastapi import FastAPI, Path


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
