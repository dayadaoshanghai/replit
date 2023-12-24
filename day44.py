import random

def ran():
    return random.randint(1, 90)

def prettyPrint(bingo):
    for row in bingo:
        # 这里只是把展示 bingo卡里面的元素转成为字符串,实际bingo列表中的元素仍未数字
        print(" | ".join(str(x).rjust(5) for x in row))


def createCard(bingo):
    while True:
        count = 0
        # 转换为数字,可以同类型比较
        num = int(input("guess number:"))
        print(num)
        for row in range(3):
            for col in range(3):
                
                if num == bingo[row][col]:
                    bingo[row][col] = "X"
                    prettyPrint(bingo)

        for row in bingo:
            for col in row:
                if col == "X":
                    count += 1
        if count >= 5:
            print("you win!")
            break

def generate_num():
    # Generate random numbers and sort them
    numbers = [ran() for _ in range(8)]
    numbers.sort()
    return numbers

# Populate the bingo grid
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

# Print the bingo grid
                # Initialize the bingo grid
bingo = [[0 for _ in range(3)] for _ in range(3)]
populate_grid(bingo)
prettyPrint(bingo)
createCard(bingo)
