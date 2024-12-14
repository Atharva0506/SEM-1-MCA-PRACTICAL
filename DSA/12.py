# 12.	Write python program to implement of Queues Using Arrays

import array

class Queue:
    def __init__(self, size):
        self.size = size           # Maximum size of the queue
        self.queue = array.array('i', [0] * size)  # Array to store queue elements
        self.front = -1            # Front of the queue
        self.rear = -1             # Rear of the queue

    # Check if the queue is full
    def is_full(self):
        if self.rear == self.size - 1:
            return True
        return False

    # Check if the queue is empty
    def is_empty(self):
        if self.front == -1:
            return True
        return False

    # Add an element to the queue (enqueue)
    def enqueue(self, data):
        if self.is_full():
            print("Queue is Full!")
        else:
            if self.front == -1:
                self.front = 0  # If the queue is empty, set front to 0
            self.rear += 1
            self.queue[self.rear] = data
            print(f"Enqueued {data} to the queue.")

    # Remove an element from the queue (dequeue)
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!")
        else:
            removed_element = self.queue[self.front]
            print(f"Dequeued {removed_element} from the queue.")
            self.front += 1
            # Reset the queue if all elements are dequeued
            if self.front > self.rear:
                self.front = self.rear = -1

    # Peek at the front element of the queue
    def peek(self):
        if self.is_empty():
            print("Queue is Empty!")
        else:
            print(f"Front element is {self.queue[self.front]}.")

    # Display all elements in the queue
    def display(self):
        if self.is_empty():
            print("Queue is Empty!")
        else:
            print("Queue elements: ", end="")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

# Main function to test the Queue implementation
def main():
    size = int(input("Enter the size of the queue: "))
    q = Queue(size)
    
    # Perform queue operations
    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter element to enqueue: "))
            q.enqueue(data)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            q.peek()
        elif choice == 4:
            q.display()
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.")


main()
