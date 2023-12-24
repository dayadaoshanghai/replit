import random

def ran():
    return random.randint(1, 90)

def prettyPrint(bingo):
    for row in bingo:
        print(" | ".join(str(x).rjust(5) for x in row))
    print()

def createCard(bingo):
    while True:
        count = 0
        num = int(input("guess number:"))
        for row in range(3):
            for col in range(3):
                if bingo[row][col] != "BINGO" and bingo[row][col] == num:
                    bingo[row][col] = "X"
                    prettyPrint(bingo)

        for row in bingo:
            for col in row:
                if col == "X":
                    count += 1
        if count >= 5:  # 修改胜利条件
            print("you win!")
            break

def generate_num():
    numbers = [ran() for _ in range(8)]
    numbers.sort()
    return numbers

def populate_grid(bingo):
    numbers = generate_num()
    i = 0
    for row in range(3):
        for col in range(3):
            if row == 1 and col == 1:
                bingo[row][col] = "BINGO"
            else:
                bingo[row][col] = numbers[i]
                i += 1

bingo = [[0 for _ in range(3)] for _ in range(3)]
populate_grid(bingo)
prettyPrint(bingo)
createCard(bingo)
