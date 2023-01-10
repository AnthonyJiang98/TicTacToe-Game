
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

player = "o"
winner = None
game_running = True

#printing the tictactoe board
def PrintBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])

#player input
def PlayerInput(board):
    player_input = int(input("Enter a number from 1-9. "))
    if player_input >= 1 and player_input <=9 and board[player_input-1] == "-":
        board[player_input-1] = player
    else:
        print("Sorry this spot is taken or you have entered an invalid number: " )

#win or tie
def CheckWin(board):
    #horizontal
    global game_running
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        print("winner: " + winner)
        game_running = False
        print(game_running)
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[1]
        print("winner: " + winner)
        game_running = False
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        print("winner: " + winner)
        game_running = False
    #vertical
    elif board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        print("winner: " + winner)
        game_running = False
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        print("winner: " + winner)
        game_running = False
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        print("winner: " + winner)
        game_running = False
    #diagonal
    elif board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        print("winner: " + winner)
        game_running = False
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        print("winner: " + winner)
        game_running = False
    #Tie
    elif "-" not in board:
        Winner = None
        print("Tie")
        game_running = False
    

#Switch player
def SwitchPlayer():
    global player
    if player == "o":
        player = "x"
    else:
        player = "o"



while game_running:
    PrintBoard(board)
    PlayerInput(board)
    CheckWin(board)
    SwitchPlayer()
    
#Final winning board or tie
PrintBoard(board)

