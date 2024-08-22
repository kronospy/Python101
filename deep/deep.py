"""Here’s how to test your code manually:

Run your program with python deep.py. Type 42 and press Enter. Your program should output:"Yes"
Run your program with python deep.py. Type Forty Two and press Enter. Your program should output:"Yes"
Run your program with python deep.py. Type forty-two and press Enter. Your program should output"Yes"
Run your program with python deep.py. Type 50 and press Enter. Your program should output"No"
Be sure to vary the casing of your input and “accidentally” add spaces on either side of your input before pressing enter. Your program should behave as expected, case- and space-insensitively."""

# Check if the input matches any valid responses
def check_answer(x):
    return "Yes" if x in ["42", "forty-two", "forty two"] else "No"

# Request user input
x = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

# Call the function and print the result
print(check_answer(x))