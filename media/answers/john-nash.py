from random import sample , shuffle

MOUSE = "\U0001F401"
WALL = '+'
n = 5
MATRIX = []

mouse_row = 2
mouse_col = 2

for i in range(n): 
    row = []
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            row.append(WALL)
        else:
            row.append(' ') 
    MATRIX.append(row)

MATRIX[mouse_row][mouse_col] = MOUSE

numbers = [-2, -1, 1, 2, 3, 4, 5, 6]
positions = [
    (mouse_row-1, mouse_col-1), (mouse_row-1, mouse_col), (mouse_row-1, mouse_col+1),
    (mouse_row, mouse_col-1), (mouse_row, mouse_col+1), (mouse_row+1, mouse_col-1),
    (mouse_row+1, mouse_col), (mouse_row+1, mouse_col+1)
]

for pos, num in zip(positions, numbers):
    MATRIX[pos[0]][pos[1]] = num

for i in range(n):
    for j in range(n):
        print(f"{MATRIX[i][j]}", end="\t")
    print()






def train_mouse(mouse_row , mouse_col):
    pass





computer = 0

from random import sample , shuffle

point = 0
max_point = 21
lstrand = [-2, -1, 1, 2, 3, 4, 5, 6]

while True:
    num = input("Enter a integer number (-2 / +6): ")
    
    if num.isdigit() and int(num) >= -2 and int(num) <= 6:
        num = int(num)
        break
    print("Invalid input! Please enter a integer (-2 / +6).")

while True:
    if point < max_point:
        if num != 0:
            point += num
            print(f"Current point: {point}")

            if point < max_point:

                for i in lstrand:
                    shuffle(lstrand)
                    choice = sample(lstrand, 1)[0]

                if choice + lstrand[i] != 21:
                    print(f"Computer's choice is {choice}.")
                    point += choice

                else:
                    choice = sample(lstrand, 1)[0]
                    point += choice
                    print(f"Computer's choice is {choice}.")

                print(f"Current point: {point}")

                if point >= max_point:
                    print("Computer won!")
                    break
                else:
                    while True:
                        num = input("Enter a integer number (-2 / +6) : ")
                        if num.isdigit() and int(num) >= -2 and int(num) <= 6:
                            num = int(num)
                            break
                        print("Invalid input! Please enter a integer (-2 / +6).")
            else:
                print("Player won!")
                break
        else:
            print("Zero is not allowed! Please enter a integer (-2 / +6).")
            while True:
                num = input("Enter a integer number (-2 / +6) : ")
                if num.isdigit() and num.isdigit() and int(num) >= -2 and int(num) <= 6:
                    num = int(num)
                    break
                print("Invalid input! Please enter a integer (-2 / +6).")
    else:
        print("Game over")
        break

        
