# Initialize
word = "MAS"
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
for i in range(num_rows-2):
    for j in range(num_columns-2):
        if table[i][j] in ("M","S") and table[i+1][j+1] == "A":
            if ((table[i][j] == "M" and table[i+2][j+2] == "S") or (table[i][j] == "S" and table[i+2][j+2] == "M")) and ((table[i+2][j] == "M" and table[i][j+2] == "S") or (table[i+2][j] == "S" and table[i][j+2] == "M")):
                total+=1

print(total)
