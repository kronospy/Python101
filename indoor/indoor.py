"""Run your program with python indoor.py. Type HELLO and press Enter. Your program should output hello.
Run your program with python indoor.py. Type THIS IS PYTHON and press Enter. Your program should output this is python.
Run your program with python indoor.py Type 40 and press Enter. Your program should output 50.
"""


# Prompt the user for input
user_input = input("Please enter some text: ")

# Check if the input is numeric
if user_input.isdigit():
    # Convert to integer and add 10
    v = int(user_input) + 10
    print(v)
else:
    # Output the input in lowercase
    print(user_input.lower())
