# 8.	Write a program to create singly linear linked list for insert delete search  operation

# Node class for LinkedList
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to the next node

# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None

    # Function to insert a new node at the end of the list
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # If list is empty, set head to the new node
        else:
            temp = self.head
            while temp.next:  # Traverse to the last node
                temp = temp.next
            temp.next = new_node  # Add the new node at the end

    # Function to delete a node by its value
    def delete(self, value):
        temp = self.head
        if temp is not None and temp.data == value:  # If head node needs to be deleted
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != value:  # Search for the node to delete
            prev = temp
            temp = temp.next
        
        if temp is None:  # If the node was not found
            print(f"Node with value {value} not found.")
            return
        
        prev.next = temp.next  # Unlink the node
        temp = None

    # Function to search a node by its value
    def search(self, value):
        temp = self.head
        index = 0
        while temp:
            if temp.data == value:
                return f"Node with value {value} found at index {index}"
            temp = temp.next
            index += 1
        return f"Node with value {value} not found."

    # Function to print the list
    def print_list(self):
        temp = self.head
        if temp is None:
            print("The list is empty.")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")  # End of the list

def main():
    sll = SinglyLinkedList()
    
    while True:
        print("\nMenu:")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Print List")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter value to insert: "))
            sll.insert(data)
        elif choice == 2:
            value = int(input("Enter value to delete: "))
            sll.delete(value)
        elif choice == 3:
            value = int(input("Enter value to search: "))
            print(sll.search(value))
        elif choice == 4:
            sll.print_list()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")


main()

