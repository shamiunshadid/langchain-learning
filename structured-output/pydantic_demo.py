from pydantic import BaseModel, EmailStr, Field

class Student(BaseModel):
    
    name: str
    age: int
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10)
    
    

new_student = {"name": "Lala", "age": 21, "email": "lala@bala.com", "cgpa": 5.5}

student = Student(**new_student)

print(student)