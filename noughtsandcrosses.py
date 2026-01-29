import random
import os.path
import json
random.seed()

def draw_board(board):
         print(f"|{board[0]}|{board[1]}|{board[2]}|\n")
         print(f"|{board[3]}|{board[4]}|{board[5]}|\n")
         print(f"|{board[6]}|{board[7]}|{board[8]}|")
board={0:'0', 1:'1', 2:'2', 3:'3', 4:'4',
           5:'5', 6:'6', 7:'7', 8:'8'}
draw_board(board)
    # develop code to draw the board

def welcome(board):
    name=input("Hello User,Please enter your name:")
    print(f"\n Hello {name} Welcome to Tic Tac Toe Game")
    # prints the welcome message
    # display the board by calling draw_board(board)
welcome(board)
def initialise_board(board):
    for i in range(len(board)):
        board[i]=' '
    # develop code to set all elements of the board to one space ' '
    return board
    
def get_player_move(board):
    
    
    try:
        choice=int(input("Choose a cell to put X in(0-8)"))
        cell=int(choice)
        if 0<= cell <=8:
            row=cell//3
            col=cell%3
    # develop code to ask the user for the cell to put the X in,
    # and return row and col
            return row, col
        else:
            print("Please enter a number between 0 and 8")
    except ValueError:
        print("Please input from cell (0-8)")
get_player_move(board)

def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    # and return row and col
    moves=[]
    for i in range(9):
        if board[i] == ' ':
            moves.append(i)
    if moves:
        choice=random.choice(moves)
        row=choice//3
        col=choice%3
    return row, col

def check_for_win(board, mark):
    conditions=[
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for spots in conditions:
        if board[spots[0]]==board[spots[1]]==board[spots[2]] == mark:
            return True
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    return False

def check_for_draw(board):
    for cell in board.values():
        if cell == ' ':
            return False
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    return True
        
def play_game(board):
    board=initialise_board(board)
    while True:
        draw_board(board)
        row,col=get_player_move(board)
        board[row*3+col]='X'
        if check_for_win(board, 'X'):
            draw_board(board)
            print("Congratulations, You Won!")
            return 1
        if check_for_draw(board):
            draw_board(board)
            print("Draw")
            return 0
        row,col=choose_computer_move(board)
        board[row*3+col]='O'

        if check_for_win(board,'O'):
            draw_board(board)
            print("Computer Won")
            return -1
        if check_for_draw(board):
            draw_board(board)
            print("Draw")
            return 0
    board=[' ']*9
play_game(board)
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    # then draw the board
    # then in a loop, get the player move, update and draw the board
    # check if the player has won by calling check_for_win(board, mark),
    # if so, return 1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # if not, then call choose_computer_move(board)
    # to choose a move for the computer
    # update and draw the board
    # check if the computer has won by calling check_for_win(board, mark),
    # if so, return -1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    #repeat the loop
                    
                
def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
     while True: 
        print()
        print("1 - Play the game")
        print("2 - Save score in file 'leaderboard.txt")
        print("3 - Load and display the scores from the 'leaderboard.txt")
        print("q - End the program")
        choice = input("Enter you choice : ")
    
        if choice in ["1", "2", "3", "q"]:
            return choice
        else:
            print("Invalid choice ya fat fucker!!!!!!!")

def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    if os.path.exists("file.txt"):
        try:
            with open("file.txt", "r") as da_file:
                leaders = json.load(da_file)
        except: 
            '''
            kun error catch garne tyo hal, main kura gardeko chu
            '''
            leaders = {}
    return leaders
    
def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    return


def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    pass


