def draw_board(board):
    print("   |   |   ")
    print(" "+board[0]+" | "+board[1]+" | "+board[2]+" ")
    print("___|___|___")
    print("   |   |   ")
    print(" "+board[3]+" | "+board[4]+" | "+board[5]+" ")
    print("___|___|___")
    print("   |   |   ")
    print(" "+board[6]+" | "+board[7]+" | "+board[8]+" ")
    print("   |   |   ")

def check_win(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

def tic_tac_toe():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    player = "X"
    game_over = False

    while not game_over:
        draw_board(board)

        choice = input("Enter a number from 1-9 to place your mark: ")
        if board[int(choice) - 1] == "X" or board[int(choice) - 1] == "O":
            print("That space is already taken. Choose another!")
        else:
            board[int(choice) - 1] = player
            if check_win(board, player):
                draw_board(board)
                print("Congratulations! Player "+player+" wins!")
                game_over = True
            elif "1" not in board and "2" not in board and "3" not in board and \
                 "4" not in board and "5" not in board and "6" not in board and \
                 "7" not in board and "8" not in board and "9" not in board:
                draw_board(board)
                print("It's a tie!")
                game_over = True
            else:
                if player == "X":
                    player = "O"
                else:
                    player = "X"

tic_tac_toe()
