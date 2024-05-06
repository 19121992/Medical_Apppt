from pydantic import BaseModel

class Patient(BaseModel):
    id: int
    name:str
    age: int
    sex: str
    weight: int
    height: int
    phone: str
    
    
class PatientUpdate(BaseModel):
    name:str
    age: int
    sex: str
    weight: int
    height: int
    phone: str
    

patient = [
    Patient(id=2, name="Susan", age=26, sex="F", weight=68, height=175, phone="+2348056789123"),
    Patient(id=3, name="Harry", age=48, sex="M", weight=70, height=150, phone="+2347012345678"),
    Patient(id=4, name="John", age=24, sex="F", weight=55, height=165, phone="+2347087654321"),
    Patient(id=5, name="Nancy", age=52, sex="M", weight=85, height=185, phone="+2348098765432"),
    Patient(id=6, name="peter", age=33, sex="F", weight=90, height=148, phone="+2348023456789"),
    Patient(id=7, name="Samson", age=41, sex="M", weight=70, height=165, phone="+2348123456789")
]
