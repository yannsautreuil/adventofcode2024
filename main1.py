import re

total = 0

# Open the file in read mode
with open("input.txt", "r") as file:
    for line in file:
        # Strip whitespace characters (like newlines)
        line = line.strip()
        
        # Find all digits in the line
        digits = re.findall(r'\d', line)
        
        if digits:  # If there are digits in the line
            first_digit = int(digits[0])
            last_digit = int(digits[-1])
            total += first_digit + last_digit
            print(f"Line: {line}")
            print(f"First digit: {first_digit}, Last digit: {last_digit}")
        else:
            print(f"Line: {line} contains no digits.")
    print(f"Total is {total}")