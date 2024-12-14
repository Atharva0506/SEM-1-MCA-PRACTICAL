# 1.	Write a Python function for the Armstrong, palindrome, and prime numbers using 	switch cases.


def check_number_simple(number, check_type):
    if check_type == 'armstrong':
        digits = [int(d) for d in str(number)]
        power = len(digits)
        return number == sum(d ** power for d in digits)
    elif check_type == 'palindrome':
        s = str(number)
        return s == s[::-1]
    elif check_type == 'prime':
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    else:
        return "Invalid check type"

num = int(input("Enter a number: "))
print("Choose check type: armstrong, palindrome, prime")
check = input("Enter check type: ").strip().lower()

result = check_number_simple(num, check)
if result == "Invalid check type":
    print(result)
else:
    print(f"Is the number {num} a {check}? {'Yes' if result else 'No'}")
