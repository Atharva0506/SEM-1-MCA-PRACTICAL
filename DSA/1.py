# 1.	Write python program to insert delete and display array elements
import array

# Function to insert elements into the array
def insert_element(arr, element):
    arr.append(element)
    print(f"Element {element} inserted successfully.")

# Function to delete an element from the array
def delete_element(arr, element):
    try:
        arr.remove(element)
        print(f"Element {element} deleted successfully.")
    except ValueError:
        print(f"Element {element} not found in the array.")

# Function to display the array
def display_array(arr):
    print("Array elements:", arr)

# Main function demonstrating the array operations
def main():
    # Create an array with type 'i' for integers
    arr = array.array('i', [10, 20, 30, 40, 50])
    
    print("Initial array:")
    display_array(arr)
    
    insert_element(arr, 60)
    insert_element(arr, 70)
    
    print("\nArray after insertion:")
    display_array(arr)
    
    delete_element(arr, 30)
    
    print("\nArray after deletion:")
    display_array(arr)
    
    delete_element(arr, 100)
    
    print("\nFinal array:")
    display_array(arr)


main()
