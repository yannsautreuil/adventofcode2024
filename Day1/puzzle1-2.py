from bisect import bisect_left, bisect_right

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

for a in A:
    # Find the range of `a` in B using binary search
    left_index = bisect_left(B, a)
    right_index = bisect_right(B, a)
    
    # Count occurrences of `a` in B
    count = right_index - left_index
    C.append(a * count)

print(C)

# Sum these distances
sum = 0
for proba in C:
    sum += int(proba)
print(sum)