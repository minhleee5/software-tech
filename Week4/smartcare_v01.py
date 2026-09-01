#task 1

appointments = []

input_patient_name1 = str(input("Please enter your (patient) name: "))
input_prac_name1 = str(input("Please enter your (practitioner) name: "))
input_appointment_time1 = str(input("Please enter your (appointment) time: "))

def book_appointment(input_patient_name, input_prac_name, input_appointment_time):
    if not input_patient_name:
        raise ValueError("Patient name cannot be empty")
    appointment = {
        "Patient" : input_patient_name,
        "Practitioner" : input_prac_name,
        "Time" : input_appointment_time
    }
    appointments.append(appointment)

def print_appointments():
    if not(appointments):
        raise ValueError("No appointments were found")
        return
    for appointment in appointments:
        print(f"Patient: {input_patient_name}, Practitioner: {input_prac_name}, Time: {input_appointment_time}")

print("welcome to SmartCare: Community Clinic Appointment Booking System!")
print_appointments()