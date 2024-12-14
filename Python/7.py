# 7.	Write a program to reverse the given string using list

def reverse_string(input_string):
    # Convert the string to a list of characters
    char_list = list(input_string)
    
    # Reverse the list
    char_list.reverse()
    
    # Join the reversed list into a string and return it
    return ''.join(char_list)

# Input from the user
user_input = input("Enter a string to reverse: ")

# Reverse the string
reversed_string = reverse_string(user_input)

# Display the reversed string
print("Reversed String:", reversed_string)
