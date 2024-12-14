#  11. 	Using at least 6 special character sequence  create matching patterns

import re

# Sample text
text = """
John's email is john.doe123@gmail.com
Mary's email is mary_smith@outlook.com
My phone number is 123-456-7890
I am learning Python at www.python.org
The date is 12/11/2024
My zip code is 90210
"""

# 1. \d: Matches any digit (0-9)
pattern_1 = r"\d+"  # Matches one or more digits
matches_1 = re.findall(pattern_1, text)
print(f"Digits: {matches_1}")

# 2. \w: Matches any alphanumeric character (a-z, A-Z, 0-9, _)
pattern_2 = r"\w+"  # Matches one or more word characters
matches_2 = re.findall(pattern_2, text)
print(f"Words: {matches_2}")

# 3. \s: Matches any whitespace character (spaces, tabs, line breaks)
pattern_3 = r"\s+"  # Matches one or more whitespace characters
matches_3 = re.findall(pattern_3, text)
print(f"Whitespaces: {matches_3}")

# 4. \b: Matches a word boundary (before and after a word)
pattern_4 = r"\bPython\b"  # Matches the word 'Python' as a whole word
matches_4 = re.findall(pattern_4, text)
print(f"Word Boundary (Python): {matches_4}")

# 5. ^: Matches the start of the string
pattern_5 = r"^John"  # Matches if 'John' is at the beginning of a line
matches_5 = re.findall(pattern_5, text)
print(f"Start of Line (John): {matches_5}")

# 6. $: Matches the end of the string
pattern_6 = r"90210$"  # Matches if '90210' is at the end of a line
matches_6 = re.findall(pattern_6, text)
print(f"End of Line (90210): {matches_6}")

