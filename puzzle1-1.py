# Initialize an empty list for absolute differences
A = []
B = []
C = []

# Open the file and process each line
with open("data1-1.txt", "r") as file:

    for line in file:

        # Split the line into two numbers
        a, b = map(int, line.split())
        A.append(a)
        B.append(b)

# Sort lists
A.sort()
print(A)
B.sort()
print(B)

# Compare gaps and store into 3rd table
for a, b in zip(A, B):
    C.append(abs(a - b))
print(C)

# Sum these distances
sum = 0
for delta in C:
    sum += int(delta)
print(sum)