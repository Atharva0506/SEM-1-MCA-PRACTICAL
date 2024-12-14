# 2.	Write program to convert a matrix to sparse matrix
import array

# Function to convert a matrix to a sparse matrix
def matrix_to_sparse(matrix):
    sparse_matrix = []
    
    # Get the number of rows and columns
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    # Traverse the matrix and add non-zero elements to the sparse matrix
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0:
                sparse_matrix.append((i, j, matrix[i][j]))  # Store (row, col, value)
    
    return sparse_matrix

# Function to display the sparse matrix
def display_sparse_matrix(sparse_matrix):
    print("Sparse Matrix (Row, Column, Value):")
    for item in sparse_matrix:
        print(item)

# Main function to demonstrate the matrix to sparse matrix conversion
def main():
    # Create a sample matrix (2D array)
    matrix = [
        [0, 0, 3, 0],
        [4, 0, 0, 5],
        [0, 6, 0, 0],
        [7, 0, 0, 0]
    ]
    
    # Convert the matrix to a sparse matrix
    sparse_matrix = matrix_to_sparse(matrix)
    
    # Display the sparse matrix
    display_sparse_matrix(sparse_matrix)


main()
