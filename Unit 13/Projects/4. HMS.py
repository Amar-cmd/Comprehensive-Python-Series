# Hospital Management System (Beginner Friendly, Console Based)
# OOP: Inheritance + Encapsulation + classmethod + staticmethod
# Menu: match-case (Python 3.10+)

from dataclasses import dataclass, field
from typing import Dict, List


# -------------------- 1) Person (Base Class) --------------------
@dataclass
class Person:
    person_id: str
    name: str
    age: int
    phone: str

    def display_info(self) -> None:
        print(f"[{self.person_id}] {self.name} | Age: {self.age} | Phone: {self.phone}")


# -------------------- 2) Doctor(Person) --------------------
@dataclass
class Doctor(Person):
    specialization: str
    __available_slots: List[str] = field(default_factory=list, repr=False)  # private

    @staticmethod
    def is_valid_slot(slot: str) -> bool:
        # Simple HH:MM validation (beginner-friendly)
        if len(slot) != 5 or slot[2] != ":":
            return False
        hh, mm = slot.split(":")
        if not (hh.isdigit() and mm.isdigit()):
            return False
        hh, mm = int(hh), int(mm)
        return 0 <= hh <= 23 and 0 <= mm <= 59

    def get_slots(self) -> List[str]:
        # return a copy (safe)
        return list(self.__available_slots)

    def add_slot(self, slot: str) -> None:
        if not Doctor.is_valid_slot(slot):
            print("Invalid slot format. Use HH:MM (e.g., 10:30)")
            return
        if slot in self.__available_slots:
            print("Slot already exists.")
            return
        self.__available_slots.append(slot)
        self.__available_slots.sort()
        print("Slot added.")

    def book_slot(self, slot: str) -> bool:
        if slot in self.__available_slots:
            self.__available_slots.remove(slot)
            return True
        return False

    def display_doctor(self) -> None:
        self.display_info()
        print(f"Specialization: {self.specialization}")
        print(f"Available Slots: {self.get_slots()}")


# -------------------- 3) Patient(Person) --------------------
@dataclass
class Patient(Person):
    __medical_history: List[dict] = field(default_factory=list, repr=False)  # private
    appointments: List[str] = field(default_factory=list)

    def add_history(self, record: dict) -> None:
        # Example record: {"date":"2025-12-25","issue":"Fever"}
        if "date" not in record or "issue" not in record:
            print("Record must contain 'date' and 'issue'.")
            return
        self.__medical_history.append(record)
        print("History record added.")

    def get_history(self) -> List[dict]:
        return list(self.__medical_history)  # safe copy

    def display_patient(self) -> None:
        self.display_info()
        print(f"Appointments: {self.appointments}")


# -------------------- 4) Appointment --------------------
@dataclass
class Appointment:
    patient_id: str
    doctor_id: str
    date: str
    time_slot: str
    reason: str
    status: str = "Booked"
    appointment_id: str = field(init=False)

    appointment_count: int = 100  # class attribute (counter)

    def __post_init__(self):
        self.appointment_id = Appointment.generate_id()

    @classmethod
    def generate_id(cls) -> str:
        cls.appointment_count += 1
        return f"A{cls.appointment_count}"

    def display_appointment(self) -> None:
        print(
            f"[{self.appointment_id}] Patient:{self.patient_id} | Doctor:{self.doctor_id} | "
            f"{self.date} {self.time_slot} | Reason:{self.reason} | Status:{self.status}"
        )


# -------------------- 5) HospitalSystem (Management) --------------------
class HospitalSystem:
    def __init__(self):
        self.doctors: Dict[str, Doctor] = {}
        self.patients: Dict[str, Patient] = {}
        self.appointments: Dict[str, Appointment] = {}

    def add_doctor(self, doctor: Doctor) -> None:
        if doctor.person_id in self.doctors:
            print("Doctor ID already exists.")
            return
        self.doctors[doctor.person_id] = doctor
        print("Doctor added.")

    def add_patient(self, patient: Patient) -> None:
        if patient.person_id in self.patients:
            print("Patient ID already exists.")
            return
        self.patients[patient.person_id] = patient
        print("Patient added.")

    def find_doctor_by_specialization(self, spec: str) -> List[Doctor]:
        spec = spec.strip().lower()
        return [d for d in self.doctors.values() if d.specialization.lower() == spec]

    def book_appointment(self, patient_id: str, doctor_id: str, date: str, slot: str, reason: str) -> None:
        patient = self.patients.get(patient_id)
        if not patient:
            print("Patient not found.")
            return

        doctor = self.doctors.get(doctor_id)
        if not doctor:
            print("Doctor not found.")
            return

        if not Doctor.is_valid_slot(slot):
            print("Invalid slot format. Use HH:MM (e.g., 10:30)")
            return

        if not doctor.book_slot(slot):
            print("Slot not available.")
            return

        appt = Appointment(patient_id, doctor_id, date.strip(), slot.strip(), reason.strip())
        self.appointments[appt.appointment_id] = appt
        patient.appointments.append(appt.appointment_id)

        print(f"Appointment booked successfully. ID: {appt.appointment_id}")

    def cancel_appointment(self, appointment_id: str) -> None:
        appt = self.appointments.get(appointment_id)
        if not appt:
            print("Appointment not found.")
            return

        if appt.status == "Cancelled":
            print("Appointment already cancelled.")
            return

        appt.status = "Cancelled"

        # Return slot back to doctor (simple way)
        doctor = self.doctors.get(appt.doctor_id)
        if doctor:
            doctor.add_slot(appt.time_slot)

        print("Appointment cancelled.")

    def show_doctor_schedule(self, doctor_id: str) -> None:
        doctor = self.doctors.get(doctor_id)
        if not doctor:
            print("Doctor not found.")
            return
        print("\n--- Doctor Details ---")
        doctor.display_doctor()

        print("\nAppointments:")
        found = False
        for a in self.appointments.values():
            if a.doctor_id == doctor_id:
                a.display_appointment()
                found = True
        if not found:
            print("No appointments for this doctor.")

    def show_patient_history(self, patient_id: str) -> None:
        patient = self.patients.get(patient_id)
        if not patient:
            print("Patient not found.")
            return

        print("\n--- Patient Details ---")
        patient.display_patient()

        print("\nMedical History:")
        history = patient.get_history()
        if not history:
            print("No history records.")
        else:
            for rec in history:
                print(f"- {rec['date']}: {rec['issue']}")

        print("\nAppointments:")
        if not patient.appointments:
            print("No appointments.")
        else:
            for aid in patient.appointments:
                appt = self.appointments.get(aid)
                if appt:
                    appt.display_appointment()

    def list_appointments(self) -> None:
        if not self.appointments:
            print("No appointments.")
            return
        print("\n--- All Appointments ---")
        for appt in self.appointments.values():
            appt.display_appointment()


# -------------------- Helpers --------------------
def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Enter a valid number.")


# -------------------- Main Program --------------------
hs = HospitalSystem()

while True:
    print("\n--- Hospital Management System ---")
    print("1. Add Doctor")
    print("2. Add Patient")
    print("3. Book Appointment")
    print("4. Cancel Appointment")
    print("5. Show Doctor Slots/Schedule")
    print("6. Show Patient History")
    print("7. List All Appointments")
    print("8. Exit")

    choice = read_int("Enter choice: ")

    match choice:
        case 1:
            did = input("Doctor ID: ").strip()
            name = input("Name: ").strip()
            age = read_int("Age: ")
            phone = input("Phone: ").strip()
            spec = input("Specialization: ").strip()

            doc = Doctor(did, name, age, phone, spec)

            # Add some slots
            print("Add available slots (type 'done' to stop):")
            while True:
                s = input("Slot (HH:MM): ").strip()
                if s.lower() == "done":
                    break
                doc.add_slot(s)

            hs.add_doctor(doc)

        case 2:
            pid = input("Patient ID: ").strip()
            name = input("Name: ").strip()
            age = read_int("Age: ")
            phone = input("Phone: ").strip()

            pat = Patient(pid, name, age, phone)

            # Optional: add history
            add = input("Add medical history now? (y/n): ").strip().lower()
            if add == "y":
                date = input("Date (YYYY-MM-DD): ").strip()
                issue = input("Issue: ").strip()
                pat.add_history({"date": date, "issue": issue})

            hs.add_patient(pat)

        case 3:
            pid = input("Patient ID: ").strip()

            # doctor selection
            print("\nDoctor selection:")
            print("1) Enter Doctor ID manually")
            print("2) Find doctor by specialization (auto-pick first available)")
            dchoice = read_int("Choose: ")

            if dchoice == 1:
                did = input("Doctor ID: ").strip()
            elif dchoice == 2:
                spec = input("Specialization: ").strip()
                matches = hs.find_doctor_by_specialization(spec)
                if not matches:
                    print("No doctor found with that specialization.")
                    continue

                # pick first doctor who has at least 1 slot
                picked = None
                for d in matches:
                    if d.get_slots():
                        picked = d
                        break

                if not picked:
                    print("No doctor available with free slots in that specialization.")
                    continue

                did = picked.person_id
                print(f"Auto-selected Doctor: {picked.name} ({picked.specialization}) | ID: {did}")
            else:
                print("Invalid option.")
                continue

            date = input("Date (YYYY-MM-DD): ").strip()

            # show slots before asking
            doc = hs.doctors.get(did)
            if not doc:
                print("Doctor not found.")
                continue

            print("Available Slots:", doc.get_slots())
            slot = input("Choose slot (HH:MM): ").strip()
            reason = input("Reason: ").strip()

            hs.book_appointment(pid, did, date, slot, reason)

        case 4:
            aid = input("Appointment ID to cancel: ").strip()
            hs.cancel_appointment(aid)

        case 5:
            did = input("Doctor ID: ").strip()
            hs.show_doctor_schedule(did)

        case 6:
            pid = input("Patient ID: ").strip()
            hs.show_patient_history(pid)

        case 7:
            hs.list_appointments()

        case 8:
            print("Bye!")
            break

        case _:
            print("Invalid choice.")
