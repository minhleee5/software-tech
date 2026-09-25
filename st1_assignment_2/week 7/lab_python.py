from enum import Enum
from datetime import datetime

class Patient:
    def __init__(self, Patient_ID, Patient_full_Name, Patient_contact):
        if not Patient_ID or not Patient_full_Name:
            print("Patient ID and Patient Full Name cannot be empty")
        self.Patient_ID: str = Patient_ID
        self.Patient_full_Name:str = Patient_full_Name
        self.Patient_contact:str = Patient_contact

    def request_appointment(self) -> None:
        pass

    def view_history(self) -> None:
        pass

class Practitioner:
    def __init__(self, Practitioner_ID, Practitioner_full_Name, Speciality):
        self.Practitioner_ID = Practitioner_ID
        self.Practitioner_full_Name = Practitioner_full_Name
        self.Speciality = Speciality

class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class Appointment:
    def __init__(self, appointment_id: str, date_time: datetime, patient: Patient, practitioner: Practitioner):
        if not appointment_id:
            raise ValueError("Appointment ID cannot be empty.")
        self.appointment_id: str = appointment_id
        self.date_time: datetime = date_time
        self.patient: Patient = patient
        self.practitioner: Practitioner = practitioner
        self.status: AppointmentStatus = AppointmentStatus.SCHEDULED

    def update_status(self, new_status: AppointmentStatus) -> None:
        if self.status == AppointmentStatus.CANCELLED:
            raise ValueError("Cannot update a cancelled appointment.")
        self.status = new_status

    def cancel(self) -> None:
        if self.status == AppointmentStatus.CANCELLED:
            raise ValueError("Appointment is already cancelled.")
        self.status = AppointmentStatus.CANCELLED

#test 1
# p = Patient("P1", "Alice Smith", "555-1234")
# pr = Practitioner("PR1", "Dr. Bob", "Cardiology")
# app = Appointment("A1", "2026-06-01", p, pr)
#
# app.cancel()
# print(app.status)