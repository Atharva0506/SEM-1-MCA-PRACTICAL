# 9.	Write a program to create queue using linked list and manipulate it

# Node class for LinkedList
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to the next node

# Queue class using LinkedList
class Queue:
    def __init__(self):
        self.front = None  # Front of the queue
        self.rear = None   # Rear of the queue

    # Enqueue operation to add an element to the queue
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:  # If queue is empty
            self.front = self.rear = new_node
            return
        self.rear.next = new_node  # Add the new node at the end
        self.rear = new_node       # Update the rear pointer

    # Dequeue operation to remove an element from the queue
    def dequeue(self):
        if self.front is None:  # If queue is empty
            print("Queue is empty!")
            return
        temp = self.front
        self.front = temp.next  # Move the front pointer to the next node
        if self.front is None:  # If the queue is now empty, update the rear
            self.rear = None
        temp = None  # Free the old front node

    # Peek operation to view the front element without removing it
    def peek(self):
        if self.front is None:  # If queue is empty
            print("Queue is empty!")
            return
        return self.front.data

    # Display the elements in the queue
    def display(self):
        if self.front is None:  # If queue is empty
            print("Queue is empty!")
            return
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")  # End of queue

# Main function to test the Queue operations
def main():
    q = Queue()
    
    while True:
        print("\nMenu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter value to enqueue: "))
            q.enqueue(data)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            front = q.peek()
            if front is not None:
                print(f"Front element is: {front}")
        elif choice == 4:
            q.display()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

main()
