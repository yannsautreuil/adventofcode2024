# Read the file
with open("data6-1.txt","r") as file:
    list1 = [list(line.strip()) for line in file]

print(list1)
initial_value = '^'
for i, row in enumerate(list1):
    if initial_value in row:
        found_index =[i, row.index(initial_value)]
        break

print(f"Starting position is {found_index}")

rules = {
  "up": [-1,0,"right"],
  "right": [0,1,"down"],
  "down": [1,0,"left"],
  "left": [0,-1,"up"]
}

def is_in_range(table, row, col):
    return 0 <= row < len(table) and 0 <= col < len(table[row])

position = found_index
direction = "up"
exit = False
count= 0
next_row = 0
next_column = 0

while exit == False:

    list1[position[0]][position[1]] = 'X'

    next_row = int(int(position[0])+int(rules[direction][0]))
    print(f"If going {direction} new row would be {next_row}")
    next_column = int(int(position[1])+int(rules[direction][1]))
    print(f"If going {direction} new column would be {next_column}")

    if is_in_range(list1,next_row,next_column):

        if list1[next_row][next_column] == '#':            
            direction = rules[direction][2]
            print(f"# faced so no position change and new direction is {direction}")
        else:
            position = [next_row,next_column]
            print(f"New confirmed position is {position}")

    else:
        exit = True
        print(f"New position would be out, so exit")

    # Security max iterations
    count += 1    
    if count == 10000:
        exit = True

for row in list1:
    print("".join(row))

print(f"Exit in {count} iterations")

totalX = sum(row.count('X') for row in list1)
print(f"Total number of X is {totalX}")
