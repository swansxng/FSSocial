import time


exit_game = False

ingame = True

white_pawn = '\u2659'
white_knight = '\u2658'
white_bishop = '\u2657'
white_rook = '\u2656'
white_queen = '\u2655'
white_king = '\u2654'
black_pawn = '\u265F'
black_knight = '\u265E'
black_bishop = '\u265D'
black_rook = '\u265C'
black_queen = '\u265B'
black_king = '\u265A'

base_position = [
    ['8', black_rook, black_knight, black_bishop, black_queen, black_king, black_bishop, black_knight, black_rook],
    ['7', black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn],
    ['6', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['5', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['4', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['2', white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn],
    ['1', white_rook, white_knight, white_bishop, white_queen, white_king, white_bishop, white_knight, white_rook],
    [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
]

def loading():
    print('SUPERCHESS 3000 PRO MAX (Trial version)')
    """print('Loading...', end='')
    for i in range(7):
        print('.', end='')
        time.sleep(0.5)
    for i in range(3):
        print('.', end='')
        time.sleep(1)
    print('')"""

def menu():
    loading()
    print('1. Play Chess')
    print('2. Exit')
    if input() == '1':
        print('Select your side:\n1.White\n2.Black')
        if input() == '1':
            return True
        else:
            return False
    else:
        exit()

def print_position(position):
    for elem in position:
        print(*elem)

def check_move(position, move):
    return True

while not exit_game:
    white_side = menu()
    position = base_position
    rule_writed = False
    while ingame:
        print_position(position)
        if not rule_writed:
            print("Write move or 'exit'")
        command = input()
        if input() == 'exit':
            break
        else:
            move = command
        if check_move(position, move):
            position[8].index(move[0])

