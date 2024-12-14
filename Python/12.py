# 12.	Write a python program that  create 3 threads and implements synchronisation.

import threading
import time

# Shared resource
shared_counter = 0

# Lock object for synchronization
lock = threading.Lock()

# Function to increment the counter
def increment_counter(thread_name):
    global shared_counter
    for _ in range(5):
        # Acquire the lock before accessing the shared resource
        lock.acquire()
        try:
            print(f"{thread_name} is incrementing the counter.")
            shared_counter += 1
            print(f"{thread_name} updated counter: {shared_counter}")
        finally:
            # Release the lock after updating the shared resource
            lock.release()
        time.sleep(1)

# Creating 3 threads
thread1 = threading.Thread(target=increment_counter, args=("Thread 1",))
thread2 = threading.Thread(target=increment_counter, args=("Thread 2",))
thread3 = threading.Thread(target=increment_counter, args=("Thread 3",))

# Starting the threads
thread1.start()
thread2.start()
thread3.start()

# Waiting for all threads to complete
thread1.join()
thread2.join()
thread3.join()

print(f"Final counter value: {shared_counter}")
