import random

def ran():
    return random.randint(1, 90)

def prettyPrint(bingo):
    for row in bingo:
        print(" | ".join(str(x).rjust(5) for x in row))
    # for col in bingo:
    #     print(" ___ ".join(str(x).rjust(5) for x in col))
            

# Generate random numbers and sort them
numbers = [ran() for _ in range(8)]
numbers.sort()

# Initialize the bingo grid
bingo = [[0 for _ in range(3)] for _ in range(3)]
print(bingo)

# Populate the bingo grid
i = 0
for row in range(3):
    for col in range(3):
        if row == 1 and col == 1:
            bingo[row][col] = "BINGO"
        else:
            bingo[row][col] = numbers[i]
            i += 1

# Print the bingo grid
prettyPrint(bingo)
