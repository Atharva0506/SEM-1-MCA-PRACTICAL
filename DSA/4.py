# 4.	write a program to find Sum of Array

import array

# Function to find the sum of elements in an array using for loop
def sum_of_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Main function to demonstrate sum of array
def main():
    # Create an array using the array module
    arr = array.array('i', [1, 2, 3, 4, 5])  # 'i' indicates array of integers

    # Calculate the sum using for loop
    result = sum_of_array(arr)

    # Display the result
    print(f"The sum of the array is: {result}")


main()

