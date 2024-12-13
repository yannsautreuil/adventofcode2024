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

# Rules with for each direct row delta, column delta, letter to write on map for direction
rules = {
  "up": [-1,0,"u"],
  "right": [0,1,"r"],
  "down": [1,0,"d"],
  "left": [0,-1,"l"]
}

def is_in_range(table, row, col):
    return 0 <= row < len(table) and 0 <= col < len(table[row])

position = found_index
direction = "up"
exit = False
count= 0
next_row = 0
next_column = 0
keys = list(rules.keys())
loop_blocker_count = 0

while exit == False:

    next_row = position[0] + rules[direction][0]
    #print(f"If going {direction} new row would be {next_row}")
    next_column = position[1] + rules[direction][1]
    #print(f"If going {direction} new column would be {next_column}")

    if is_in_range(list1,next_row,next_column):

        current_index = keys.index(direction)
        following_direction = keys[(current_index + 1) % len(keys)]
        following_following_direction = keys[(current_index + 2) % len(keys)] 
        #print(f"next direction is {following_direction} and next next would be {following_following_direction}")

        if list1[next_row][next_column] == '#':            
            direction = following_direction        
            #direction = rules[direction][2]
            #print(f"# faced so no position change and new direction is {direction}")
        else:
            # Update map with direction taken
            list1[position[0]][position[1]] = rules[direction][2]
            
            # lets check if new position would be a loop generator
            # if we apply following direction key map movement to current position, does it already contein marker of this direction -> loop?
            next_row_if_blocked = position[0] + rules[following_direction][0]
            next_column_if_blocked = position[1] + rules[following_direction][1]
            next_next_row_if_blocked = next_row_if_blocked + rules[following_direction][0]
            next_next_column_if_blocked = next_column_if_blocked + rules[following_direction][1]
            looping_character = rules[following_direction][2]
            #internal_security = 0
            while is_in_range(list1,next_next_row_if_blocked,next_next_column_if_blocked) :                
                
                if list1[next_row_if_blocked][next_column_if_blocked] == looping_character:
                    #print("BLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
                    loop_blocker_count += 1
                    break
                else:
                    #print(f"If turning next position value would be {list1[next_row_if_blocked][next_column_if_blocked]} thus not {rules[following_direction][2]}")      
                    #print(f"Next 2 locations in direction {direction} are {next_row_if_blocked} {next_column_if_blocked} and {next_next_row_if_blocked} {next_next_column_if_blocked}")
                    if list1[next_next_row_if_blocked][next_next_column_if_blocked] == '#' and list1[next_row_if_blocked][next_column_if_blocked] == rules[following_following_direction][2]:
                        loop_blocker_count += 1
                        break

                next_row_if_blocked += rules[following_direction][0]
                #print(f"If turing {following_direction} new row would be {next_row_if_blocked}")
                next_column_if_blocked += rules[following_direction][1]
                #print(f"If turning {following_direction} new column would be {next_column_if_blocked}")
                next_next_row_if_blocked += rules[following_direction][0]
                next_next_column_if_blocked += rules[following_direction][1]
                #internal_security += 1

            #Then update position to continue as expected
            position = [next_row,next_column]
            #print(f"New confirmed position is {position}")

    else:
        list1[position[0]][position[1]] = rules[direction][2]
        exit = True
        #print(f"New position would be out, so exit")

    # Security max iterations
    count += 1    
    if count == 10000:
        exit = True

for row in list1:
    print("".join(row))

print(f"Exit in {count} iterations")

totalX = sum(row.count('u') + row.count('r') + row.count('d') + row.count('l') for row in list1)
print(f"Total number of crossed tiles is {totalX}")
print(f"Ttotal loop creator is {loop_blocker_count}")
