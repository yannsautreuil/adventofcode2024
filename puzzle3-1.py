import re

# Initialize
pattern = r"mul\((\d+),(\d+)\)"
total = 0

# Open the file and process each line
with open("data3-1.txt", "r") as file:

    for line in file:

        # Collect all matches
        matches = re.findall(pattern,line)

        # Sum products of all matches
        total += sum(int(x) * int(y) for x,y in matches)

# Total total for all lines
print(total)
