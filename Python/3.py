# 3.	Using input ()  function accepts customer details  with validation (name,email,phone number)

import re
def validate_customer_details():
    while True:
        name = input("Enter your name: ")
        if name.isalpha() and len(name) > 0:
            break
        else:
            print("Invalid name. Please enter alphabetic characters only.")

    while True:
        email = input("Enter your email: ")
        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            break
        else:
            print("Invalid email. Please enter a valid email address.")

    while True:
        phone = input("Enter your phone number: ")
        if re.match(r'^\d{10}$', phone):
            break
        else:
            print("Invalid phone number. Please enter a 10-digit number.")

    print("\nCustomer Details:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")

validate_customer_details()
