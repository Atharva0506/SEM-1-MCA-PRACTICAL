# 7.	Write a program to reverse the given string using list

# Node class for LinkedList
class Node:
    def __init__(self, data):
        self.data = data  # Data of the node
        self.next = None  # Next node reference
        self.prev = None  # Previous node reference

# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None

    # Function to insert characters at the end of the list
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # If list is empty, make new node the head
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
                temp.next = new_node  # Add new node at the end
            new_node.prev = temp  # Set the previous pointer

    # Function to reverse the linked list
    def reverse(self):
        current = self.head
        prev_node = None
        while current:
            # Swap the next and prev pointers for each node
            next_node = current.next
            current.next = prev_node
            current.prev = next_node
            prev_node = current
            current = next_node
        self.head = prev_node  # Update head to point to the new first node

    # Function to print the linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="")  # Print each character in the node
            temp = temp.next
        print()  # Newline after printing the list

# Function to reverse the string using linked list
def reverse_string(input_str):
    linked_list = DoublyLinkedList()

    # Insert each character into the linked list
    for char in input_str:
        linked_list.insert(char)

    # Reverse the linked list
    linked_list.reverse()

    # Print the reversed string
    linked_list.print_list()

# Main function
def main():
    input_str = input("Enter a string to reverse: ")
    print("Reversed string: ", end="")
    reverse_string(input_str)


main()
