# get user input for a string
string_input = input("Enter a string: ")

# get the length of the string
length = len(string_input)
print("Length of the string:", length)

# convert string to uppercase
uppercase = string_input.upper()
print("Uppercase string:", uppercase)

# convert string to lowercase
lowercase = string_input.lower()
print("Lowercase string:", lowercase)

# check if string starts with a specific substring
substring = input("Enter a substring to check if it starts with: ")
if string_input.startswith(substring):
    print("String starts with", substring)
else:
    print("String does not start with", substring)

# check if string ends with a specific substring
substring = input("Enter a substring to check if it ends with: ")
if string_input.endswith(substring):
    print("String ends with", substring)
else:
    print("String does not end with", substring)

# find the index of a substring in the string
substring = input("Enter a substring to find the index of: ")
index = string_input.find(substring)
if index == -1:
    print("Substring not found")
else:
    print("Index of substring:", index)