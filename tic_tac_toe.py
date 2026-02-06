from random import randrange

def display_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def enter_move(board):
    move = input("chose number from 1 to 9 : ")

    for row in range(3):
        for col in range(3):
            if board[row][col] == move:
                board[row][col] = "O"
                return

    print("Not True , try again")
    enter_move(board)

def make_list_of_free_fields(board):
    free = []

    for row in range(3):
        for col in range(3):
            if board[row][col] not in ["X", "O"]:
                free.append((row, col))

    return free

def victory_for(board, sign):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            return True
        if board[0][i] == board[1][i] == board[2][i] == sign:
            return True

    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True

    return False

def draw_move(board):
    free = make_list_of_free_fields(board)
    if free:
        row, col = free[randrange(len(free))]
        board[row][col] = "X"

board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

print("Tic Tac Toe GAME ")
print("The computer is (X)")

while True:
    display_board(board)

    if victory_for(board, "X"):
        print("I'm win! ~ o ~")
        break

    if not make_list_of_free_fields(board):
        print("It's a draw..")
        break

    enter_move(board)

    if victory_for(board, "O"):
        display_board(board)
        print("You win ! *-*")
        break

    draw_move(board)