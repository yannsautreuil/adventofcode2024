# Initialize
word = "XMAS"
reverse = word[::-1]
print(f"Searching file for {word} and {reverse}")
total = 0

# Read the file and store its content into a 2D table
with open("data4-1.txt", "r") as file:
    table = [list(line.strip()) for line in file]

# Get the dimensions of the 2D list
num_rows = len(table)               # Number of rows
num_columns = len(table[0]) if num_rows > 0 else 0  # Number of columns (assuming uniform row length)
print(f"File has Rows: {num_rows}, Columns: {num_columns}")

# Parse most of the table for all cases match
for i in range(num_rows-3):
    for j in range(num_columns-3):
        increment = 0
        horizontal = table[i][j]+table[i][j+1]+table[i][j+2]+table[i][j+3]
        vertical = table[i][j]+table[i+1][j]+table[i+2][j]+table[i+3][j]
        diagonal = table[i][j]+table[i+1][j+1]+table[i+2][j+2]+table[i+3][j+3]
        if horizontal == word:
            increment += 1
        if horizontal == reverse:
            increment += 1
        if vertical == word:
            increment += 1
        if vertical == reverse:
            increment += 1
        if diagonal == word:
            increment += 1
        if diagonal == reverse:
            increment += 1
        total += increment

# Parse only the remaining right column for vertical matches
for i in range(num_rows-3):
    for j in range(num_columns-3,num_columns):
        increment = 0
        vertical = table[i][j]+table[i+1][j]+table[i+2][j]+table[i+3][j]
        if vertical == word:
            increment += 1
        if vertical == reverse:
            increment += 1
        total += increment

# Parse only the remaining bottom lines for horizontal matches
for i in range(num_rows-3,num_rows):
    for j in range(num_columns-3):
        increment = 0
        horizontal = table[i][j]+table[i][j+1]+table[i][j+2]+table[i][j+3]
        if horizontal == word:
            increment += 1
        if horizontal == reverse:
            increment += 1
        total += increment

# Parse remaining diagonal
for i in range(num_rows-3):
    for j in range(3,num_columns):
        increment = 0
        diagonal = table[i][j]+table[i+1][j-1]+table[i+2][j-2]+table[i+3][j-3]
        if diagonal == word:
            increment += 1
        if diagonal == reverse:
            increment += 1
        total += increment

print(total)
