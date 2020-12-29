#------------------------------------------
#                FUNCTIONS
#------------------------------------------
def print_board(lst):
    return ' {} | {} | {} \n---|---|---\n {} | {} | {} \n---|---|---\n {} | {} | {} '.format(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6],lst[7],lst[8])

def check_win(lst):
    if lst[0]==lst[1]==lst[2] or lst[0]==lst[3]==lst[6]:
        if lst[0] == ' ':
            return 'False'
        else:
            return lst[0]
    elif lst[0]==lst[4]==lst[8] or lst[2]==lst[4]==lst[6]:
        if lst[4] == ' ':
            return 'False'
        else:
            return lst[4]
    elif lst[2]==lst[5]==lst[8] or lst[6]==lst[7]==lst[8]:
        if lst[8] == ' ':
            return 'False'
        else:
            return lst[8]
    return 'False'

def choose_cell(_piece):
    loop = True
    cell_num = int(input(f"{NamePiece[_piece]}: Your turn! ----> "))
    while loop:
        if cell_num not in range(1,10):
            cell_num = int(input("Invalid cell number.Please try again ---> "))
        elif cell_num in playedCell:
            cell_num = int(input("Cell already played.Please try again ---> "))
        else:
            loop = False
    return cell_num

def replay():
    rep = input("\n\nDo you want to play again?(Y/N) --->").upper()
    print('\n\n')
    loop = True
    while loop:
        if rep == 'Y':
            return True
        elif rep == 'N':
            return False
        else:
            rep = input("Invalid input! Do you want to play again?(Y/N) --->")



#--------------------------------------------
#                 THE GAME
#--------------------------------------------

again = True

while again:
    # Name and Piece Prompt
    NamePiece = {'X':'Player 1','O':'Player 2'}
    print('------ Player 1 Info ------')
    name = input("Please input Player 1's name -----> ")
    piece =  input(f"Welcome {name}. Please choose your piece: X or O ---->").upper()
    while piece != 'X' and piece != 'O':
        piece = input("Invalid piece. Please choose again: X or O ---->").upper()
    NamePiece[piece] = name
    print('\n------ Player 2 Info ------')
    name = input("Please input Player 2's name -----> ")
    if piece == 'X':
        NamePiece['O'] = name
        print(f"Welcome {name}, your piece is 'O'")
    else:
        NamePiece['X'] = name
        print(f"Welcome {name}, your piece is 'X'")
    #print(NamePiece)


    print('\n\n-------- Cells Number Layout -----------')
    print(print_board(range(1, 10)))
    print('\n'*2)
    input('Press Enter to start the game\n\n')

    gameBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # This list keeps track of the game
    playedCell = []
    status = 'on-going'
    isX = True
    currentPiece = 'X'
    chosenCell = None

    print('----------------------------\n        GAME START\n----------------------------')

    print('\n\n')
    print(print_board(gameBoard))

    while status == 'on-going':
        if isX:
            currentPiece = 'X'
        else:
            currentPiece = 'O'

        # take turn:
        chosenCell = choose_cell(currentPiece)
        gameBoard[chosenCell-1] = currentPiece
        playedCell.append(chosenCell)
        print('\n'*20)
        print(print_board(gameBoard))
        if check_win(gameBoard) != 'False':
            print(f"\n\n-=-=-=-=-=-=-=-=-\nCongratulation! {NamePiece[currentPiece]}, you won!\n-=-=-=-=-=-=-=-=-=-")
            status = 'finished'
        else:
            isX = not isX

    again = replay()

print('----------------------------\n        GAME ENDED\n----------------------------')