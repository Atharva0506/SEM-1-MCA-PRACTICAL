# 13.	Create a database connectivity  which  implements validations.

from pymongo import MongoClient, errors
import re

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  
db = client["student_database"]  # Creating a database
collection = db["students"]  # Creating a collection

# Validations
def is_valid_email(email):
    """Validate email format using a regular expression."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

def is_valid_name(name):
    """Check if the name is a non-empty string."""
    return isinstance(name, str) and len(name) > 0

# Function to insert a new student with validation
def insert_student(name, email, age):
    # Validate name and email
    if not is_valid_name(name):
        return "Invalid name! Name must be a non-empty string."
    
    if not is_valid_email(email):
        return "Invalid email format!"
    
    # Check if email already exists
    if collection.find_one({"email": email}):
        return "Email already exists in the database!"
    
    # Insert into MongoDB
    student = {"name": name, "email": email, "age": age}
    try:
        collection.insert_one(student)
        return f"Student {name} added successfully!"
    except errors.PyMongoError as e:
        return f"Error inserting student: {e}"

# Example Usage
name = input("Enter student's name: ")
email = input("Enter student's email: ")
age = int(input("Enter student's age: "))

result = insert_student(name, email, age)
print(result)
