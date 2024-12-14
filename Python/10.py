# 10. Write a python program which demonstrate difference between search() and find()   function in re module.

import re

# Sample text
text = "Say My Name, intent does not matter only consequences"

# Using re.search() - returns the first match found
search_result = re.search(r"rain", text)
if search_result:
    print(f"re.search() found: {search_result.group()}")
else:
    print("re.search() did not find a match.")

# Using re.findall() - returns a list of all matches found
findall_result = re.findall(r"rain", text)
if findall_result:
    print(f"re.findall() found: {findall_result}")
else:
    print("re.findall() did not find any matches.")

