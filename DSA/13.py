# 13.	Implement Bubble sort to sort a list of numbers.

def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the list
    for i in range(n):
        # Flag to optimize the algorithm (if no swaps, the list is sorted)
        swapped = False
        
        # Last i elements are already sorted, so we don't check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                swapped = True
        
        # If no elements were swapped, the list is sorted
        if not swapped:
            break

    return arr

# Main function to test the bubble_sort
def main():
    arr = [64, 34, 25, 12, 22, 11, 90]  # Example list
    print("Original list:", arr)
    
    sorted_arr = bubble_sort(arr)
    print("Sorted list:", sorted_arr)


main()
