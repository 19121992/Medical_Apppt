from pydantic import BaseModel
from enum import Enum

class Status(str, Enum):
    is_available = "True"
    not_available = "False"

class Doctors(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    is_available: Status = Status.is_available
    
    def set_availability(self, availability: Status):
        self.is_available = availability


    
class DoctorsUpdate(BaseModel):
    name: str
    specialization: str
    phone: str


class DoctorStatus(BaseModel):
    is_available: Status
    
    

doctors: list[Doctors] = [
    Doctors(id=1, name="Jokomba", specialization="Orthopedics", phone="+2348037373822", is_available=Status.is_available),
    Doctors(id=2, name="Adetola", specialization="Pediatrics", phone="+2348084847787", is_available=Status.is_available),
    Doctors(id=3, name="Bantai", specialization="Psychiatry", phone="+2347023456789", is_available=Status.is_available),
    Doctors(id=4, name="Saheedat", specialization="Ophthalmology", phone="+2348123456789", is_available=Status.not_available),
    Doctors(id=5, name="Nwosu", specialization="Neurology", phone="+2348023456789", is_available=Status.is_available),
    Doctors(id=6, name="Steven", specialization="Cardiology", phone="+2349037484949", is_available=Status.is_available)
]
