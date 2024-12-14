# 3.	Write Python program to demonstrate Implementing stack using list

# Stack class using list
class Stack:
    def __init__(self):
        self.stack = []  # Initialize an empty list to represent the stack

    # Push operation: Add element to the stack
    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed to stack.")

    # Pop operation: Remove and return the top element from the stack
    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"{item} popped from stack.")
            return item
        else:
            print("Stack is empty, cannot pop.")
            return None

    # Peek operation: Return the top element without removing it
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty, cannot peek.")
            return None

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display the current stack
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Current stack:", self.stack)


# Main function to demonstrate stack operations
def main():
    # Create a Stack object
    stack = Stack()

    # Display initial stack
    stack.display()

    # Push elements to the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # Display the stack
    stack.display()

    # Peek the top element
    print("Top element:", stack.peek())

    # Pop elements from the stack
    stack.pop()
    stack.pop()

    # Display the stack after popping elements
    stack.display()

    # Try popping from an empty stack
    stack.pop()


main()

