# TicTacToe Game with AI (Player vs Computer)

# Step 1: Create the board
board  = [' ' for _ in range(9)]
def print_board():
    print("\n")
    for i in range(3):
        print(f"{board[i*3]} / {board[i*3+1]} / {board[i*3+2]}")
        if i < 2:
            print("---------")
def check_winner(player):
    win_patterns  = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]               # Diagonal
    ]
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False
def is_draw():
    return " " not in board
def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Invalid move, try again.")
        except (ValueError, IndexError):
            print("Invalid input, please enter a number between 1 and 9.")
            import random 
def computer_move():
 empty_positions = [i for i in range(9) if board[i] == " "]
 move = random.choice(empty_positions)
board[move] = "O"
def play_game():
 print("Welcome to Tic Tac Toe!")
 print_board()
 while True:
     player_move()
     print_board()
     if check_winner('X'):
         print("Congratulations! You win!")
         break
     if is_draw():
         print("It's a draw!")
         break
     computer_move()
     print("Computer's move:")
     print_board()
     if check_winner('O'):
         print("Computer wins! Better luck next time.")
         break
     if is_draw():
         print("It's a draw!")
         break