# 5.	Write a program to create doubly  linked list for insert delete search print operation using menu driven program
class Node:
    def __init__(self, data):
        self.data = data  # Node's data
        self.next = None  # Reference to next node
        self.prev = None  # Reference to previous node


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize head to None

    # Insert a node at the end of the list
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:  # If the list is empty, make the new node the head
            self.head = new_node
        else:
            temp = self.head
            while temp.next:  # Traverse to the last node
                temp = temp.next
            temp.next = new_node  # Add the new node at the end
            new_node.prev = temp  # Set the previous node to the current last node

    # Delete a node by value
    def delete(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                if temp.prev:  # If the node is not the first node
                    temp.prev.next = temp.next
                if temp.next:  # If the node is not the last node
                    temp.next.prev = temp.prev
                if temp == self.head:  # If it's the head node, update the head
                    self.head = temp.next
                temp = None  # Remove the node
                print(f"Node with value {value} deleted.")
                return
            temp = temp.next
        print(f"Node with value {value} not found.")

    # Search for a node by value
    def search(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                print(f"Node with value {value} found.")
                return
            temp = temp.next
        print(f"Node with value {value} not found.")

    # Print the list from head to tail
    def print_list(self):
        temp = self.head
        if not temp:
            print("The list is empty.")
            return
        print("List: ", end="")
        while temp:
            print(temp.data, end=" <-> " if temp.next else "")
            temp = temp.next
        print()

# Menu-driven program
def menu():
    dll = DoublyLinkedList()
    while True:
        print("\nDoubly Linked List Menu:")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Print")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter the value to insert: "))
            dll.insert(data)
        elif choice == 2:
            value = int(input("Enter the value to delete: "))
            dll.delete(value)
        elif choice == 3:
            value = int(input("Enter the value to search: "))
            dll.search(value)
        elif choice == 4:
            dll.print_list()
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


menu()
