from fastapi import FastAPI, HTTPException
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "LLM Automation Agent is running"}

@app.post("/run")
def run_task(task: str):
    return {"task": task, "status": "Task execution started"}

@app.get("/read")
def read_file(path: str):
    try:
        with open(path, "r") as file:
            return {"content": file.read()}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

