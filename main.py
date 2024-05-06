from fastapi import FastAPI
from routers.patients import patient_router
from routers.doctors import doctor_router
from routers.appointment import appointment_router


app = FastAPI(
    title="Medical Appointment App - OPEN API 3.0",
    description="The application is to facilitate appointment bookings between Patients and Doctors",
    docs_url="/",
    contact={
        "name": "Ogunle Adedamola",
        "url": "https://github.com/19121992",
    }
    
)

app.include_router(patient_router)
app.include_router(doctor_router)
app.include_router(appointment_router)

