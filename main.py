from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()

#question 1
@app.get("/hello")
def hello():
    return "Hello world"

#question 2
@app.get("/welcome",status-code = 200)
def welcome(name: str):
    return f"Welcome {name}"

#question 3
class Student(BaseModel):
    Reference: str
    FirstName: str
    LastName: str
    Age: int

@app.post("/students", status_code=201)
def add_students(new_students: List[Student]):
    students_db.extend(new_students)
    return students_db

#question 4
@app.get("/students")
def get_students():
    return students_db

#question 5
@app.put("/students")
def update_or_add_student(student: Student):
    for i, s in enumerate(students_db):
        if s.Reference == student.Reference:
            students_db[i] = student
            return {"message": "Student updated", "students": students_db}
    students_db.append(student)
    return {"message": "Student added", "students": students_db}

#question bonus
def get_students_authorized(authorization: Optional[str] = Header(None)):
    if authorization is None:
        raise HTTPException(status_code=401, detail="Unauthorized: Missing Authorization header")
    if authorization != "bon courage":
        raise HTTPException(status_code=403, detail="Forbidden: Invalid Authorization value")
    return students_db