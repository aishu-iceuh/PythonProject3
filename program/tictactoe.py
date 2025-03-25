board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

# Printing the game board
def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-------------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-------------")
    print(board[6] + "|" + board[7] + "|" + board[8])

# Take player input
def playerInput(board):
    while True:
        inp = int(input("Enter a number 1-9: "))
        if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
            board[inp - 1] = currentPlayer
            break
        else:
            print("Oops! The spot is either taken or invalid, try again!")

# Check for horizontal wins
def checkHorizontal(board):
    if board[0] == board[1] == board[2] and board[0] != "-":
        return board[0]
    elif board[3] == board[4] == board[5] and board[3] != "-":
        return board[3]
    elif board[6] == board[7] == board[8] and board[6] != "-":
        return board[6]
    return None

# Check for vertical wins
def checkVertical(board):
    if board[0] == board[3] == board[6] and board[0] != "-":
        return board[0]
    elif board[1] == board[4] == board[7] and board[1] != "-":
        return board[1]
    elif board[2] == board[5] == board[8] and board[2] != "-":
        return board[2]
    return None

# Check for diagonal wins
def checkDiagonal(board):
    if board[0] == board[4] == board[8] and board[0] != "-":
        return board[0]
    elif board[2] == board[4] == board[6] and board[2] != "-":
        return board[2]
    return None

# Check if there's a tie
def checkTie(board):
    if "-" not in board:
        printBoard(board)
        print("It's a tie!")
        return True
    return False

# Check if the game has been won
def checkWin(board):
    global winner
    winner = checkHorizontal(board) or checkVertical(board) or checkDiagonal(board)
    if winner:
        printBoard(board)
        print(f"The winner is {winner}")
        return True
    return False

# Switch player turn
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Main game loop
while gameRunning:
    printBoard(board)
    playerInput(board)
    
    if checkWin(board):
        gameRunning = False  # Stop the game if there's a winner
    
    if not gameRunning and not checkTie(board):
        gameRunning = False  # Stop the game if it's a tie

    if gameRunning:  # Switch player only if the game is still running
        switchPlayer()
