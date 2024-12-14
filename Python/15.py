# 14.	Using list, dictionary, tuple store details in database.


from pymongo import MongoClient, errors

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["employee_database"]
collection = db["employees"]

# List to store multiple employee records
employees_list = []

# Function to insert employee data into MongoDB using list and dictionary
def insert_employee(ename, eid, department):
    """Insert an employee into the MongoDB database."""
    
    # Check if the employee ID already exists (immutable tuple-like data)
    if collection.find_one({"eid": eid}):
        return "Employee with this ID already exists!"

    # Creating a dictionary for the employee details
    employee = {"ename": ename, "eid": eid, "department": department}
    
    # Adding the employee dictionary to the list
    employees_list.append(employee)
    
    try:
        # Insert into MongoDB
        collection.insert_one(employee)
        return "Employee added successfully!"
    except errors.PyMongoError as e:
        return f"Error inserting employee: {e}"

# Function to fetch all employees from the database
def fetch_all_employees():
    """Fetch and display all employee records."""
    try:
        employees = collection.find()
        for employee in employees:
            print(employee)
    except errors.PyMongoError as e:
        return f"Error fetching employees: {e}"

# Function to search an employee by ID
def search_employee_by_id(eid):
    """Search for an employee by their unique ID."""
    employee = collection.find_one({"eid": eid})
    if employee:
        return employee
    else:
        return "Employee not found."

# Function to delete an employee by ID
def delete_employee_by_id(eid):
    """Delete an employee record by ID."""
    result = collection.delete_one({"eid": eid})
    if result.deleted_count > 0:
        return f"Employee with ID {eid} deleted successfully."
    else:
        return "Employee not found to delete."


# Inserting employees into the database
print(insert_employee("John Doe", 101, "HR"))
print(insert_employee("Jane Smith", 102, "Finance"))
    
# Fetching all employees from the database
print("\nFetching all employees:")
fetch_all_employees()
    
# Searching for an employee by ID
print("\nSearching for employee with ID 101:")
print(search_employee_by_id(101))
    
# Deleting an employee by ID
print("\nDeleting employee with ID 101:")
print(delete_employee_by_id(101))
    
# Fetching all employees after deletion
print("\nFetching all employees after deletion:")
fetch_all_employees()
