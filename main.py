from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import os
import csv

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Load student data from the specified CSV file
students = []
with open('q-fastapi.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            "studentId": int(row["studentId"]),
            "class": row["class"]
        })

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

@app.get("/api")
async def get_students(class_: Optional[List[str]] = Query(None)):
    if class_:
        filtered_students = [student for student in students if 
student["class"] in class_]
        return {"students": filtered_students}
    return {"students": students}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

