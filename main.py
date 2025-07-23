from fastapi import FastAPI

app = FastAPI()

#question 1
@app.get("/hello")
def hello():
    return "Hello world"
