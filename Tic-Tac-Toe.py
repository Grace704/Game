import random
def display_board(board):
    print(" ",str(board[0]),"|",str(board[1]),"|",str(board[2]))
    print(" -----------")
    print(" ",str(board[3]),"|",str(board[4]),"|",str(board[5]))
    print(" -----------")
    print(" ",str(board[6]),"|",str(board[7]),"|",str(board[8]),"\n")

def player_move(board, player_symbol):
    while True:
        move = input("Player "+ str(player_symbol)+ " please enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            move = int(move)
            if board[move - 1] == ' ':
                n1=random.randint(1,100)
                n2=random.randint(1,100)
                ans=int(input("What is "+str(n1)+" + "+str(n2)+ " equals to?"))
                if ans ==int(n1+n2):
                    board[move - 1] = player_symbol
                    break
                else:
                    print("Unfortunately, wrong answer. You need to wait a round")
                    break
            else:
                print("That position is already occupied! Please find another one.")
        else:
            print("Improper input! Please enter a number between 1 and 9.")

def check_win(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]

    for j in win_conditions:
        if board[j[0]] == board[j[1]] == board[j[2]] != ' ':
            return True
    return False
blocks=[]
def main():
    board = [' '] * 9
    symbols = ['X', 'O']
    current_player = 0

    print("Welcome to math Tic-Tac-Toe!")
    for i in range(1,10):
        blocks.append(i)
    display_board(blocks)

    while True:
        player_move(board, symbols[current_player])
        display_board(board)
        if check_win(board):
            print("Player "+str(symbols[current_player])+" wins!")
            break
        elif ' ' not in board:
            print("It's a tie!")
            break
        current_player = (current_player + 1) % 2
answer=int(input("Do you want to play math Tic-Tac-Toe with your friend? \n1. Yes\n2. No\n"))
if answer==1:
    main()