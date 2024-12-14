# 5.	Write a program that accepts details of students from user  and store in the directory  ,store  details in ‘student.txt’

import os

# Function to accept student details
def get_student_details():
    name = input("Enter student's name: ")
    roll_number = input("Enter student's roll number: ")
    age = input("Enter student's age: ")
    course = input("Enter student's course: ")
    return name, roll_number, age, course

# Function to save details to a file
def save_student_details(student_details):
    # Check if the directory exists, if not, create it
    if not os.path.exists('students'):
        os.makedirs('students')

    # Path for student.txt
    file_path = 'students/student.txt'

    # Open the file in append mode to add details
    with open(file_path, 'a') as file:
        file.write(f"Name: {student_details[0]}, Roll Number: {student_details[1]}, Age: {student_details[2]}, Course: {student_details[3]}\n")

    print("Student details saved successfully!")

# Main function
def main():
    # Get student details
    student_details = get_student_details()

    # Save details to the file
    save_student_details(student_details)

main()
