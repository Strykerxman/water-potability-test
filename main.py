from fastapi import FastAPI
from data_model import NewStudent, UpdateStudent

app = FastAPI(
    title="CRUD Operations",
    description="API for CRUD Operations"
)

Students = {
    1:{
        "name":"John",
        "age": 18
    }
}

@app.get("/")
def index():
    return "Welcome to CRUD Operations API"

@app.get("/students")
def get_students():
    return Students

@app.get("/student/{student_id}")
def get_student(student_id: int):
    if student_id not in Students:
        return f"error: Student {student_id} not found"
    return Students[student_id]

@app.post("/add-student")
def add_student(stu: NewStudent):
    if not Students:
        new_id = 1
    else:
        new_id = max(Students.keys()) + 1
    Students[new_id] = stu.model_dump()
    return Students[new_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, stu: UpdateStudent):
    if student_id not in Students:
        return f"error: Student {student_id} not found"
    if stu.name is not None:
        Students[student_id]["name"] = stu.name
    if stu.age is not None:
        Students[student_id]["age"] = stu.age
    return Students[student_id]

@app.delete("/delete-student/{student_id}")
def del_student(student_id: int):
    if student_id not in Students:
        return f"error: Student {student_id} not found"
    del Students[student_id]
