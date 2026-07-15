# Store student marks
marks = [70, 85, 60, 90, 75]

# Read a value at a given index
print("Value at index 2:", marks[2])

# Update a value
marks[2] = 95

print("\nAfter updating:")
print(marks)

# Traverse and print all values
print("\nAll marks:")
for mark in marks:
    print(mark)

# Find the maximum value
maximum = marks[0]

for i in range(1, len(marks)):
    if marks[i] > maximum:
        maximum = marks[i]

print("\nMaximum value:", maximum)

# Insert a value manually
new_value = 80
index = 2

print("\nBefore insertion:")
print(marks)

# Increase array size
marks.append(0)

# Shift elements to the right
for i in range(len(marks) - 1, index, -1):
    marks[i] = marks[i - 1]

# Insert the new value
marks[index] = new_value

print("\nAfter insertion:")
print(marks)

# Time Complexity
# Read - O(1)
# Update - O(1)
# Traverse - O(n)
# Maximum - O(n)
# Insert - O(n)

