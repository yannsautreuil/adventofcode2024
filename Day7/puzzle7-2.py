
operand = ['+','*','']
result = []
total = 0

with open("data7-1.txt", "r") as file:
    for line in file:
        key, values = line.split(":")
        key = int(key.strip())
        values_list = [int(v) for v in values.strip().split()]
        #result.append([key, values_list])
        #condition_1 = any(x == 0 or abs(x) > 3 for x in values_list)
        #expression = "12+4*13"
        #result = eval(expression)
        list1 = [values_list[0]]        
        #print(values_list)
        for i in range(len(values_list)-1):
            list2 = []
            for a in list1:
                for b in operand:
                    #print(eval(f"{a}{b}{values_list[i+1]}"))
                    list2.append(eval(f"{a}{b}{values_list[i+1]}"))
            list1 = list2[:]
        #print(f"checking if equals {int(key)}")
        if any(c == int(key) for c in list1):
            total += int(key)
            #print("yes at least one")

print(total)