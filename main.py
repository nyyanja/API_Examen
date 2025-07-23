from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

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