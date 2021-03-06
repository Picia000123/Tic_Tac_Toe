import random

board = [i for i in range(0, 9)]
player, computer = "", ""

tiles = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))
winmoves = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
table = range(1, 10)

def create_board():
    x = 1
    for i in board:
        end = " | "
        if x%3 == 0:
            end = " \n"
            if i != 1: end+= "--------------\n";
        char = " "
        if i in ("X", "O"): char = i;
        x += 1
        print(char, end = end)

def select_char():
    chars = ("X", "O")
    if random.randint(0, 1) == 0:
        return chars[::-1]
    return chars

def can_move(brd, player, move):
    if move in table and brd[move - 1] == move - 1:
        return True
    return False

def can_win(brd, player, move):
    places= []
    x = 0
    for i in brd:
        if i == player: places.append(x);
        x += 1
    win = True
    for tup in winmoves:
        win = True
        for y in tup:
            if brd[y] != player:
                win = False
                break
        if win == True:
            break
    return win
    return False

def make_move(brd, player, move, undo = False):
    if can_move(brd, player, move):
        brd[move - 1] = player
        win = can_win(brd, player, move)
        if undo:
            brd[move - 1] = move - 1
        return (True, win)
    return (False, False)

def computer_move():
    move = -1
    for i in range(1, 10):
        if make_move(board,computer, i, True)[1]:
            move = i
            break
    if move == -1:
        for i in range(1, 10):
            if make_move(board, player, i, True)[1]:
                move = i
                break
    if move == -1:
        for tup in tiles:
            for mv in tup:
                if move == -1 and can_move(board, computer, mv):
                    move = mv
                    break
    return make_move(board, computer, move)

def space_exist():
    return board.count("X") + board.count("O") != 9

player, computer = select_char()
print("Player is [%s] and computer is [%s]" % (player, computer))
result = "%%% Deuce ! %%%"
while space_exist():
    create_board()
    print("# Make your next move [1-9] : ", end = " ")
    move = int(input())
    moved, won = make_move(board, player, move)
    if not moved:
        print(" >> Invalid number, Try again ")
        continue
    if won:
        result = "*** Congratulations, You've won ! ***"
        break
    elif computer_move()[1]:
        result = "*** You've Lost ***"
        break;

create_board()
print(result)
