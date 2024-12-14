# 2.	Using predefined functions perform  string operations .


def perform_string_operations(string, operation_type):
   if operation_type == 'uppercase':
       return string.upper()
   elif operation_type == 'lowercase':
       return string.lower()
   elif operation_type == 'reverse':
       return string[::-1]
   elif operation_type == 'length':
       return len(string)
   elif operation_type == 'isalnum':
       return string.isalnum()
   elif operation_type == 'capitalize':
       return string.capitalize()
   elif operation_type == 'title':
       return string.title()
   elif operation_type == 'startswith':
       prefix = input("Enter the prefix to check: ")
       return string.startswith(prefix)
   elif operation_type == 'endswith':
       suffix = input("Enter the suffix to check: ")
       return string.endswith(suffix)
   elif operation_type == 'find':
       substring = input("Enter the substring to find: ")
       return string.find(substring)
   elif operation_type == 'replace':
       old = input("Enter the substring to replace: ")
       new = input("Enter the new substring: ")
       return string.replace(old, new)
   else:
       return "Invalid operation type"


string = input("Enter a string: ")
print("Choose operation type: uppercase, lowercase, reverse, length, isalnum, capitalize, title, startswith, endswith, find, replace")
operation = input("Enter operation type: ").strip().lower()

result = perform_string_operations(string, operation)
print(f"Result of {operation} operation: {result}")	
