from database import *
from face_recognition_module import *
from qr_generator import *
from gate_pass import *

create_database()

name = input("Visitor Name: ")

phone = input("Phone Number: ")

purpose = input("Purpose of Visit: ")

photo = capture_face()

add_visitor(name, phone, purpose, photo)

qr_data = f"{name} | {phone}"

generate_qr(qr_data, f"gatepasses/{name}_qr.png")

gate_pass = create_gate_pass(name)

print("Visitor Registered Successfully")

print("Gate Pass Created")

print(gate_pass)
