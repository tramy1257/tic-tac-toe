#------------------------------------------
#                FUNCTIONS
#------------------------------------------
# Print the game board, input is a list of current pieces on each cell
def print_board(lst):
    return ' {} | {} | {} \n---|---|---\n {} | {} | {} \n---|---|---\n {} | {} | {} '.format(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6],lst[7],lst[8])

# Check if anyone have won with the current board, input is a list of current pieces on each cell
def check_win(lst):
    # Matching first row or column
    if lst[0]==lst[1]==lst[2] or lst[0]==lst[3]==lst[6]:
        if lst[0] == ' ':
            return 'False'
        else:
            return lst[0]
    # Matching diagonals or second row or second column
    elif (lst[0]==lst[4]==lst[8] or lst[2]==lst[4]==lst[6]) or (lst[1]==lst[4]==lst[7] or lst[3]==lst[4]==lst[5]):
        if lst[4] == ' ':
            return 'False'
        else:
            return lst[4]
    # Matching last row or last column
    elif lst[2]==lst[5]==lst[8] or lst[6]==lst[7]==lst[8]:
        if lst[8] == ' ':
            return 'False'
        else:
            return lst[8]
    return 'False'

# When a cell is chosen, verify input and return the position of the chosen cell
def choose_cell(_piece):
    loop = True
    cell_num = input(f"{NamePiece[_piece]}: Your turn! ----> ")
    while loop:
        if cell_num.isdigit():
            cell_num = int(cell_num)
            if cell_num not in range(1, 10):
                cell_num = input("Invalid cell number.Please try again ---> ")
            elif cell_num in playedCell:
                cell_num = input("Cell already played.Please try again ---> ")
            else:
                loop = False
        else:
            cell_num = input("Invalid cell number.Please try again ---> ")
    return cell_num

# Prompt and input verification for playing again
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
    input('\n\nPress Enter to start the game\n\n')

    # Print the cells number layout for reference
    print('\n\n-------- Cells Number Layout -----------')
    print(print_board(range(1, 10)))
    print('\n'*2)

    input('Press Enter to start the game\n\n')
    
    # Initialize game state
    gameBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # This list keeps track of the game
    playedCell = [] # Keeps track of occupied cells
    status = 'on-going'
    isX = True
    currentPiece = 'X'
    chosenCell = None
    counter = 0 # counting played cells

    print('----------------------------\n        GAME START\n----------------------------')

    print('\n\n')
    print(print_board(gameBoard))

    while status == 'on-going':
        if isX:
            currentPiece = 'X'
        else:
            currentPiece = 'O'

        # take turn:
        chosenCell = choose_cell(currentPiece) # Choose a cell
        gameBoard[chosenCell-1] = currentPiece # Replace the chosen cell with piece
        playedCell.append(chosenCell) # Add the cell to the played cell list
        counter += 1

        print('\n'*20)
        print(print_board(gameBoard))
        
        # Check for ending of current game
        if check_win(gameBoard) != 'False':
            print(f"\n\n-=-=-=-=-=-=-=-=-\nCongratulation! {NamePiece[currentPiece]}, you won!\n-=-=-=-=-=-=-=-=-=-")
            status = 'finished'
        else:
            if counter == 9:
                status = 'finished'
                print(f"\n\n-=-=-=-=-=-=-=-=-=-=-\n  This game is tied\n-=-=-=-=-=-=-=-=-=-=-")
            else:
                isX = not isX

    again = replay()

print('----------------------------\n        GAME ENDED\n----------------------------')
