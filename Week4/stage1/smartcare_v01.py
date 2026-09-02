#task 1

appointments = []

# input_patient_name1 = str(input("Please enter your (patient) name: "))
# input_prac_name1 = str(input("Please enter your (practitioner) name: "))
# input_appointment_time1 = str(input("Please enter your (appointment) time: "))

def book_appointment(input_patient_name, input_prac_name, input_appointment_time):
    if not input_patient_name:
        raise ValueError("Patient name cannot be empty")
    appointment = {
        "Patient" : input_patient_name,
        "Practitioner" : input_prac_name,
        "Time" : input_appointment_time
    }
    appointments.append(appointment)

def display_appointments():
    if not appointments:
        raise ValueError("No appointments were found")
        return
    for appointment in appointments:
        print(f"Patient: {appointment['Patient']}, Practitioner: {appointment['Practitioner']}, Time: {appointment['Time']}")

print("welcome to SmartCare: Community Clinic Appointment Booking System!")
book_appointment('None', '', '2024-05-07 10:00 AM')
book_appointment('Bob', '', '2024 05-07 11:30 AM')
display_appointments()

# AI version

# Simple appointment manager created by AI
# appointments_db = []
#
#
# def create_appointment(patient_name, practitioner_name, appointment_time):
#   # Create a record for the appointment
#   appointment_record = {
#       "patient_name": patient_name,
#       "practitioner_name": practitioner_name,
#       "appointment_time": appointment_time,
#   }
#
#   # Save the record
#   appointments_db.append(appointment_record)
#   print(f"Successfully booked appointment for {patient_name}.")
#
#
# # Example usage
# create_appointment("Charlie Brown", "Dr. Lucy Van Pelt", "2024-07-21 02:00 PM")