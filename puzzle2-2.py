from bisect import bisect_left, bisect_right

# Initialize an empty list for absolute differences
A = []
B = []
C = []
D = []
E = []

# Open the file and process each line
with open("data2-1.txt", "r") as file:

    for line in file:

        # Split the line into numbers
        A = line.split()

        # Create list of differences
        B = []
        for i in range(len(A) - 1):
            B.append(int(A[i + 1]) - int(A[i]))

        # Determine if line is ok or not and register in C
        # Check the first condition: At least one element equals 0 or is greater than 3
        condition_1 = any(x == 0 or abs(x) > 3 for x in B)

        # Check the second condition: Product of an element and the next is <= 0
        condition_2 = any(B[i] * B[i + 1] <= 0 for i in range(len(B) - 1))

        # Final result: Return 0 if any condition is met, else 1
        result = 0 if condition_1 or condition_2 else 1

        # If report is faulty and result = 0, check all sub reports without one entry and if only one max is ko we consider ok
        if result == 0:
            result2 = 0
            for k in range(len(A)):
                D = A[:]
                del D[k]
                E = []
                for m in range(len(D) - 1):
                    E.append(int(D[m + 1]) - int(D[m]))
                result2 += 0 if any(x == 0 or abs(x) > 3 for x in E) or any(E[l] * E[l + 1] <= 0 for l in range(len(E) - 1)) else 1
            if result2 > 0:
                result = 1

        C.append(result)

print(C)

# Sum these distances
sum = 0
for valid in C:
    sum += int(valid)
print(sum)