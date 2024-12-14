# 6.	Write a program for exception handling with file handling operations

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File Content:\n", content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def write_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print(f"Content successfully written to '{filename}'.")
    except PermissionError:
        print(f"Error: Permission denied to write to the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def append_to_file(filename, content):
    try:
        with open(filename, 'a') as file:
            file.write(content)
            print(f"Content successfully appended to '{filename}'.")
    except PermissionError:
        print(f"Error: Permission denied to append to the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Writing to a file
    write_to_file('example.txt', 'This is a sample content.\n')

    # Appending to the file
    append_to_file('example.txt', 'Adding more content to the file.\n')

    # Reading from the file
    read_file('example.txt')

main()
