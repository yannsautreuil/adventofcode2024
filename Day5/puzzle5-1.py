# Read the file
with open("data5-1.txt","r") as file:

    # First split the file in 2 sub parts jsing empty line as separator
    part1, part2 = file.read().split("\n\n")

# Process first part split by pipe
list1 = [line.split("|") for line in part1.strip().split("\n")]
list1.sort(key=lambda x: (x[0], x[1]))

# Process second part split by comma
list2 = [line.split(",") for line in part2.strip().split("\n")]

# Print for debug
#print(list1)
#print(list2)

# Init model list with 2 elements of first pair
A = [list1[0][0],list1[0][1]]
#print(A)
total = 0
increment = 0

# Then add new elements in the above list by checking each pair

for pair in list1[1:]:

    inserted = False
    updated = False
    #print(f"Considering {pair}")

    # If first element of pair already exist in the list being built and we need to insert element 2 of pair
    if pair[0] in A:
        if pair[1] in A:
            increment = 0
            #print(f"Since {pair[0]} and {pair[1]} already exists in {A} then nothing to do")
        else:
            updated = True
            #print(f"Since {pair[0]} exists in {A} at position {A.index(pair[0])} we will try to insert {pair[1]} after {pair[0]} and before some other element")
            # Then let's try to insert it to the right of it, and before an element of current list if rule exists
            for index in range(A.index(pair[0])+1,len(A)):
                if [pair[1],A[index]] in list1 and inserted == False:
                    #print(f"Since {[pair[1],A[index]]} condition exists then we insert {pair[1]} before {A[index]}")
                    A.insert(index,pair[1])
                    inserted = True
            if inserted == False:
                #print(f"Since no condition exists starting with {pair[1]} and ending with one element in current list then we insert {pair[1]} at the end")
                A.insert(len(A),pair[1])                   
    
    # Else means necessarily second element alredy exist in the list being built and we need to insert element 1 of pair
    else:
        updated = True
        #print(f"Since {pair[0]} does not exist then {pair[1]} must exist in {A} we will try to insert {pair[0]} before {pair[1]} and after some other element")
        # Then let's try to insert second element of pair to the left of first element, and after an element of current list if rule exists
        for rindex in range(A.index(pair[1]),0,-1):
            if [A[rindex],pair[0]] in list1 and inserted == False:
                #print(f"Since {[A[rindex],pair[0]]} condition exists then we insert {pair[0]} after {A[rindex]}")
                A.insert(rindex,pair[0])
                inserted = True
        if inserted == False:
            #print(f"Since no condition exists starting with one element in current list and ending with {pair[0]} we insert {pair[0]} at the beginning")
            A.insert(0,pair[0])

    #if updated == True:
    #    print(f"Enriched list {A}")  

print(f"Final template is : {A}")

for sequence in list2:

    #print(f"Checking {sequence}")
    #print(f"Stripping template {A}")

    # Remove from long template what is not useful because not in parsed list before compare
    stripped = [x for x in A if x in sequence]
    # If any element in parsed list which is never mentioned in conditions thus not in template, then parasite, we remove before comapred
    updatedSequence = [y for y in sequence if y in A]

    #print(f"Stripped template {stripped}")

    # If this is a match because cleaned template and cleaned parsed list, then we sum middle element of original parsed list (for sure always odd)
    if updatedSequence == stripped:
        #print(f"{sequence} is in stripped template {stripped}")
        increment = int(sequence[round(len(sequence)/2-0.1)])
        print(f"Middle element is {increment}")
        total += increment
    #else:
    #    print(f"{sequence} is NOT in stripped template {stripped}")

print(total)
    