# 15.	Write a program to implement adjacency matrix and display using linked list.

class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None

class AdjacencyList:
    def __init__(self):
        self.head = None
    # Add vertex to the linked list
    def add_vertex(self, vertex):
        new_node = Node(vertex)
        new_node.next = self.head
        self.head = new_node

    # Display the adjacency list (Linked List)
    def display(self):
        temp = self.head
        while temp:
            print(temp.vertex, end=" -> ")
            temp = temp.next
        print("None")

# Function to create and display adjacency matrix using linked lists
def create_adjacency_list(matrix):
    n = len(matrix)
    adj_list = [AdjacencyList() for _ in range(n)]

    # Traverse the matrix and add edges to the linked list representation
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                adj_list[i].add_vertex(j)
    print("Adjacency List representation:")
    for i in range(n):
        print(f"Vertex {i}: ", end="")
        adj_list[i].display()
def main():
    matrix = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    
    create_adjacency_list(matrix)


main()
