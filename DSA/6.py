# 6.	write an array to find second maximum number of an array

import array

# Function to find the second maximum number in an array
def find_second_max(arr):
    # If the array has fewer than 2 elements, return None
    if len(arr) < 2:
        return None
    
    # Initialize the maximum and second maximum values
    max_val = second_max_val = float('-inf')
    
    # Traverse the array
    for num in arr:
        if num > max_val:
            second_max_val = max_val  # Update second max
            max_val = num  # Update max
        elif num > second_max_val and num != max_val:
            second_max_val = num  # Update second max if it's not equal to max
    
    # Return the second max value or None if no second max exists
    if second_max_val == float('-inf'):
        return None
    return second_max_val

# Main function to test the find_second_max function
def main():
    # Create an array using the array module
    arr = array.array('i', [1, 2, 3, 4, 5])  # 'i' indicates array of integers

    # Find the second maximum number
    result = find_second_max(arr)

    if result is not None:
        print(f"The second maximum number in the array is: {result}")
    else:
        print("There is no second maximum number in the array.")


main()
