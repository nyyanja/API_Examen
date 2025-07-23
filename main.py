from fastapi import FastAPI

app = FastAPI()

#question 1
@app.get("/hello")
def hello():
    return "Hello world"

#question 2
@app.get("/welcome",status-code = 200)
def welcome(name: str):
    return f"Welcome {name}"