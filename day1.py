file = "day1Input.txt"

column1 = []
column2 = []

# Read the file and process each line
with open(file, "r") as file:
    for line in file:
        # Split the line into two parts based on whitespace
        parts = line.strip().split(None, 1)  # None allows splitting on any whitespace
        if len(parts) == 2:  # Ensure there are exactly two columns
            column1.append(parts[0])
            column2.append(parts[1])

# Print the resulting lists
# print("Column 1:", column1)
# print("Column 2:", column2)

sortedColumn1=sorted(column1)
sortedColumn2=sorted(column2)

# print("Sorted column 1:", sortedColumn1)
totalSum = 0

for i in range(len(sortedColumn1)):
    print(sortedColumn1[i], sortedColumn2[i])
    totalSum = abs(int(sortedColumn1[i]) - int(sortedColumn2[i])) + totalSum
    print(totalSum)

similarityScore = 0

for i in range(len(column1)):
    print(column1[i])
    count = column2.count(column1[i])
    print(count)
    similarityScore = (int(column1[i]) * count) + similarityScore
    print(similarityScore)
