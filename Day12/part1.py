
def file_to_table(param1:str):
    lineCount = 0
    with open(param1, "r") as file:
        table = [list(line.strip()) for line in file]
    return table

def is_in_range(table, row, col):
    return 0 <= row < len(table) and 0 <= col < len(table[row])

def update_table_with_groups(table:list):
    category_table = []
    category_with_index_table = []
    for i in range(len(table)):
        row_handled = 0
        for j in range(len(table[i])):
            #print(f"{i}{j} old: {table[i][j]}")
            case_managed = False
            if case_managed == False and table[i][j] not in category_table:
                category_table.append(table[i][j])
                category_with_index_table.append([table[i][j],str(1)])
                table[i][j] = table[i][j] + str(1)
                #print(f"{i}{j} new: {table[i][j]}")
                case_managed = True
                row_handled += 1
            if case_managed == False and is_in_range(table, i, j-1) and len(table[i][j-1]) > 1 and table[i][j] == table[i][j-1][:1]:
                table[i][j] = table[i][j-1]
                #print(f"{i}{j} left: {table[i][j]}")
                case_managed = True
                row_handled += 1
            if case_managed == False and is_in_range(table, i-1, j) and len(table[i-1][j]) > 1 and table[i][j] == table[i-1][j][:1]:
                table[i][j] = table[i-1][j]
                #print(f"{i}{j} up: {table[i][j]}")
                case_managed = True	
                row_handled += 1
        if row_handled < len(table[i]):
            #print(f"row {i} not complete")
            for j in range(len(table[i]),-1,-1):
                if is_in_range(table, i, j) and len(table[i][j]) == 1:
                    if is_in_range(table, i, j+1) and table[i][j] == table[i][j+1][:1]:
                        table[i][j] = table[i][j+1]
                        #print(f"{i}{j} right: {table[i][j]}")
                    else:
                        if table[i][j] not in category_table:
                            category_table.append(table[i][j])
                            category_with_index_table.append([table[i][j],str(1)])
                            table[i][j] = table[i][j] + str(1)
                            #print(f"{i}{j} new: {table[i][j]}")
                        else:
                            # Filter sublists where the first element matches the target and get the associated values
                            associated_values = [sublist[1] for sublist in category_with_index_table if sublist[0] == table[i][j]]
                            # Check if the target exists and find the maximum value
                            max_value = int(max(associated_values))
                            category_with_index_table.append([table[i][j],str(max_value+1)])
                            table[i][j] = table[i][j] + str(max_value +1)
                            #print(f"{i}{j} new: {table[i][j]}")
    return table
    
def calculate_fence(table:list):
    parcels_superficy = []
    parcels_fence = []
    for i in range(len(table)):
        for j in range(len(table[i])):
            add = 0
            if any(sublist[0] == table[i][j] for sublist in parcels_superficy) == False:
                parcels_superficy.append([table[i][j],1])
                parcels_fence.append([table[i][j],0])
            else:
                # Update the value associated with the target
                for sublist in parcels_superficy:
                    if sublist[0] == table[i][j]:
                        sublist[1] +=1
                        break  # Exit the loop once the value is updated
            if (is_in_range(table, i-1, j) and table[i][j] != table[i-1][j]) or (is_in_range(table, i-1, j) == False):
                add+=1
            if (is_in_range(table, i, j-1) and table[i][j] != table[i][j-1]) or (is_in_range(table, i, j-1) == False):
                add+=1
            if (is_in_range(table, i, j+1) and table[i][j] != table[i][j+1]) or (is_in_range(table, i, j+1) == False):
                add+=1
            if (is_in_range(table, i+1, j) and table[i][j] != table[i+1][j]) or (is_in_range(table, i+1, j) == False):
                add+=1
            # Update the value associated with the target
            for sublist in parcels_fence:
                if sublist[0] == table[i][j]:
                    sublist[1] += add
                    break  # Exit the loop once the value is updated
            #print(f"{i}{j} : {add}")
    #print(parcels_superficy)
    #print(parcels_fence)
    total = 0
    for i in range(len(parcels_superficy)):
        total += parcels_superficy[i][1] * parcels_fence[i][1]
    return total

def product_table(a:list,b:list):
    total = 0
    for i in range(len(a)):
        total += a[i][1] * b[i][1]
    return total

file_path = "Day12\input.txt"
newtable = update_table_with_groups(file_to_table(file_path))
print(f"updated Table: {newtable}")
total = calculate_fence(newtable)
print(f"total: {total}")
