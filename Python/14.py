# 13.	Accepts details of employee (ename ,eid, ..) from user and store in a database ,following operations are required,
#   1.search using id
#   2.delete specified employee  records
#   3.find duplicate records. 

from pymongo import MongoClient, errors

# Connect to MongoDB 
client = MongoClient("mongodb://localhost:27017/")
db = client["employee_database"]  # Database
collection = db["employees"]  # Collection

def insert_employee(ename, eid, department):
    """Inserts a new employee record into the database."""
    if collection.find_one({"eid": eid}):  # Check if employee with the given ID already exists
        return "Employee with this ID already exists!"
    
    employee = {"ename": ename, "eid": eid, "department": department}
    try:
        collection.insert_one(employee)
        return "Employee added successfully!"
    except errors.PyMongoError as e:
        return f"Error inserting employee: {e}"

def search_employee_by_id(eid):
    """Search for an employee by employee ID."""
    employee = collection.find_one({"eid": eid})
    if employee:
        return employee
    else:
        return "Employee not found."

def delete_employee_by_id(eid):
    """Delete an employee record by employee ID."""
    result = collection.delete_one({"eid": eid})
    if result.deleted_count > 0:
        return f"Employee with ID {eid} deleted successfully."
    else:
        return "Employee not found to delete."

def find_duplicate_records():
    """Find duplicate employee records by employee ID."""
    pipeline = [
        {"$group": {"_id": "$eid", "count": {"$sum": 1}}},
        {"$match": {"count": {"$gt": 1}}}
    ]
    duplicates = collection.aggregate(pipeline)
    return list(duplicates)

# Menu-driven interface to perform operations
def menu():
    print("1. Insert Employee")
    print("2. Search Employee by ID")
    print("3. Delete Employee by ID")
    print("4. Find Duplicate Records")
    print("5. Exit")

    while True:
        choice = input("Enter choice: ")
        
        if choice == '1':
            ename = input("Enter employee name: ")
            eid = int(input("Enter employee ID: "))
            department = input("Enter department: ")
            result = insert_employee(ename, eid, department)
            print(result)

        elif choice == '2':
            eid = int(input("Enter employee ID to search: "))
            result = search_employee_by_id(eid)
            print(result)

        elif choice == '3':
            eid = int(input("Enter employee ID to delete: "))
            result = delete_employee_by_id(eid)
            print(result)

        elif choice == '4':
            duplicates = find_duplicate_records()
            if duplicates:
                print("Duplicate Records found:")
                for duplicate in duplicates:
                    print(f"Employee ID: {duplicate['_id']}, Count: {duplicate['count']}")
            else:
                print("No duplicate records found.")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")

# Run the menu
menu()
