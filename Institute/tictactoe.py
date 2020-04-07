from random import randrange

def DisplayBoard(board):
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#
    print ("+-------+-------+-------+")
    print ("|       |       |       |")
    print ("|   "+board[0][0]+"   |   "+board[0][1]+"   |   "+board[0][2]+"   |")
    print ("|       |       |       |")
    print ("+-------+-------+-------+")
    print ("|       |       |       |")
    print ("|   "+board[1][0]+"   |   "+board[1][1]+"   |   "+board[1][2]+"   |")
    print ("|       |       |       |")
    print ("+-------+-------+-------+")
    print ("|       |       |       |")
    print ("|   "+board[2][0]+"   |   "+board[2][1]+"   |   "+board[2][2]+"   |")
    print ("|       |       |       |")
    print ("+-------+-------+-------+")

def EnterMove(board):
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#
    move = input ("Enter your move: ")
    while not move in ("1","2","3","4","5","6","7","8","9"):
        move = input ("Invalid move. Enter your move: ") 
    move_location = ((int(move)-1)//3,(int(move)-1)%3)
    while not move_location in MakeListOfFreeFields(board):
        while not move in ("1","2","3","4","5","6","7","8","9"):
            move = input ("Invalid move. Enter your move: ") 
        move_location = ((int(move)-1)//3,(int(move)-1)%3)
    board[move_location[0]][move_location[1]]="O"
    DisplayBoard(board)
    
def MakeListOfFreeFields(board):
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#
    rtn_lst = []
    for i in range(3):
        for j in range(3):
            if board[i][j].isdigit():
                rtn_lst.append((i,j))
    return rtn_lst

def VictoryFor(board, sign):
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#
    winner = False
    for i in range (3):
        if board[i][0]==board[i][1]==board[i][2]==sign or board[0][i]==board[1][i]==board[2][i]==sign: winner = True
    if board[0][0] == board[1][1] == board[2][2] == sign or board[0][2] == board[1][1] == board[2][0] == sign: winner = True
    return winner

def DrawMove(board):
#
# the function draws the computer's move and updates the board
#
    valid_moves = MakeListOfFreeFields(board)
    rand = randrange(len(valid_moves))
    move = valid_moves[rand]
    board[move[0]][move[1]]="X"
    DisplayBoard(board)

#
# Mian program goes here
#
my_board = [["1","2","3"],["4","X","6"],["7","8","9"]]
DisplayBoard(my_board)
EnterMove(my_board)
DrawMove(my_board)
EnterMove(my_board)
if VictoryFor(my_board,"O"): print("You Win!")
DrawMove(my_board)
if VictoryFor(my_board,"X"): print("You Lose!")
EnterMove(my_board)
if VictoryFor(my_board,"O"): print("You Win!")
DrawMove(my_board)
if VictoryFor(my_board,"X"): print("You Lose!")
EnterMove(my_board)
if VictoryFor(my_board,"O"): print("You Win!")
DrawMove(my_board)
if VictoryFor(my_board,"X"): print("You Lose!")
else: print ("GAME OVER!")

