from fastapi import FastAPI

app = FastAPI(title = "Train")


@app.get("/")
def hello_world():
    return "Hello world"
