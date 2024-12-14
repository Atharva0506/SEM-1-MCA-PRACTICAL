# 14.	Write a program to implement binary search using array.

# Function to perform Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid  # Target found, return the index
        
        # If target is smaller, ignore right half
        elif arr[mid] > target:
            high = mid - 1
        
        # If target is larger, ignore left half
        else:
            low = mid + 1
    
    return -1  # Target not found

# Main function to test binary search
def main():
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  # Example sorted array
    target = int(input("Enter the number to search: "))
    
    result = binary_search(arr, target)
    
    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found in the array.")


main()
