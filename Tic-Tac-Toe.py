import random

def print_board(board):
    # print Tic-Tac-Toe board
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check if the board is full
def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)

# See the list of empty cells on the board
def get_empty_cells(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]


def minimax(board, depth, is_maximizing):
    # computer's optimal move selection
    if check_win(board, "X"):
        return -10 + depth
    if check_win(board, "O"):
        return 10 - depth
    if is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = float("-inf")
        for row, col in get_empty_cells(board):
            board[row][col] = "O"
            eval = minimax(board, depth + 1, False)
            board[row][col] = " "
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for row, col in get_empty_cells(board):
            board[row][col] = "X"
            eval = minimax(board, depth + 1, True)
            board[row][col] = " "
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    # Getting the best move
    best_move = None
    best_eval = float("-inf")
    for row, col in get_empty_cells(board):
        board[row][col] = "O"
        eval = minimax(board, 0, False)
        board[row][col] = " "
        if eval > best_eval:
            best_eval = eval
            best_move = (row, col)
    return best_move

# Main game loop
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human_player = "X"
    computer_player = "O"

    print("Welcome to Tic-Tac-Toe!")
    print("You are X, and the computer is O.")
    while True:
        print_board(board)
        if not is_board_full(board):
            if human_player == "X":
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
            else:
                print("Computer is thinking...")
                row, col = get_best_move(board)
        else:
            print("It's a draw!")
            break

        if board[row][col] == " ":
            board[row][col] = human_player if human_player == "X" else computer_player
            if check_win(board, human_player):
                print_board(board)
                print("You win!")
                break
            elif check_win(board, computer_player):
                print_board(board)
                print("Computer wins!")
                break
        else:
            print("That cell is already taken. Try again.")

        # Swap human and computer players for the next turn
        human_player, computer_player = computer_player, human_player

if __name__ == "__main__":
    main()