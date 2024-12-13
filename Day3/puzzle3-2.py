import re

# Initialize
pattern = r"mul\((\d+),(\d+)\)"
total = 0

# Open the file and process each line
with open("data3-1.txt", "r") as file:

    content = file.read().replace('\n', '')

    # Step 1: Split the string by "do()"
    do_parts = content.split("do()")
    
    # Step 2: For each part, split it further by "don't()"        
    for part in do_parts:
        dont_subparts = part.split("don't()")
        # Collect all active matches knowing only matches of first sub elements are active
        matches = re.findall(pattern,dont_subparts[0])
        # Sum products of all matches
        total += sum(int(x) * int(y) for x,y in matches)     

# Total total for all lines
print(total)
