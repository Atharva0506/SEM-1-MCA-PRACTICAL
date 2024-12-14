# 9.	Demonstrate generators and decorators with suitable examples.

# Generator to yield numbers from 1 to 5
def my_generator():
    for i in range(1, 6):
        yield i

# Using the generator
gen = my_generator()
for num in gen:
    print(num)

# Simple decorator that prints the function name
def my_decorator(func):
    def wrapper():
        print(f"Executing function {func.__name__}")
        func()
    return wrapper

# Using the decorator
@my_decorator
def say_hello():
    print("Hello!")

say_hello()
