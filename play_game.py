from noughtsandcrosses import *

    
def main():
    board = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4',
           5:'5', 6:'6', 7:'7', 8:'8'}

    welcome(board)
    total_score = 0
    while True:
        choice = menu()
        if choice == '1':
            board = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4',
           5:'5', 6:'6', 7:'7', 8:'8'}
            score = play_game(board)
            total_score += score
            print('Your current score is:',total_score)
        if choice == '2':
            save_score(total_score)
        if choice == '3':
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good bye')
            return


    
# Program execution begins here
if __name__ == '__main__':
    main()
