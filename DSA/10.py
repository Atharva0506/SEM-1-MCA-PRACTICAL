# 10.	Write a program to reverse stack using list

# Node class for LinkedList
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to the next node

# Stack class using LinkedList
class Stack:
    def __init__(self):
        self.top = None  # Initialize the stack with an empty top

    # Push operation to add an element to the stack
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top  # Point the new node to the current top
        self.top = new_node  # Update the top to the new node

    # Pop operation to remove the element from the top of the stack
    def pop(self):
        if self.top is None:  # If the stack is empty
            print("Stack is empty!")
            return None
        temp = self.top
        self.top = temp.next  # Move the top pointer to the next node
        temp = None  # Free the old top node

    # Peek operation to view the top element without removing it
    def peek(self):
        if self.top is None:  # If the stack is empty
            print("Stack is empty!")
            return None
        return self.top.data

    # Display the stack elements
    def display(self):
        if self.top is None:  # If the stack is empty
            print("Stack is empty!")
            return
        temp = self.top
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")  # End of the stack

    # Reverse the stack using recursion
    def reverse(self):
        if self.top is None:
            return
        data = self.pop()
        self.reverse()
        self._insert_at_bottom(data)

    # Helper function to insert an element at the bottom of the stack
    def _insert_at_bottom(self, data):
        if self.top is None:
            self.push(data)
            return
        temp = self.top
        self.pop()  # Remove the top element temporarily
        self._insert_at_bottom(data)  # Recursive call
        self.push(temp.data)  # Push the popped element back to the stack

# Main function to test the Stack operations
def main():
    stack = Stack()
    
    # Push some elements to the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)

    print("Original Stack:")
    stack.display()

    # Reverse the stack
    stack.reverse()

    print("\nReversed Stack:")
    stack.display()


main()
