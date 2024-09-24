import math

def print_board(board):
    print("\n".join([" | ".join(row) for row in board]))
    print("-" * 9)

def evaluate_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax_algorithm(board, is_bot_turn):
    if evaluate_winner(board, 'O'):  # Bot wins
        return 10
    if evaluate_winner(board, 'X'):  # Human wins
        return -10
    if is_draw(board):
        return 0

    scores = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O' if is_bot_turn else 'X'
                score = minimax_algorithm(board, not is_bot_turn)
                scores.append(score)
                board[i][j] = ' '  # Undo move

    return max(scores) if is_bot_turn else min(scores)

def find_best_move(board):
    optimal_score = float('-inf')
    best_move_position = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_score = minimax_algorithm(board, False)
                board[i][j] = ' '
                if move_score > optimal_score:
                    optimal_score = move_score
                    best_move_position = (i, j)

    return best_move_position

def is_move_legal(board, position):
    row, col = divmod(position - 1, 3)  # Convert 1-9 input to row, col
    return board[row][col] == ' '

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_turn = True

    position_map = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }

    while True:
        print_board(board)

        if evaluate_winner(board, 'X'):
            print("You win!")
            break
        elif evaluate_winner(board, 'O'):
            print("Bot wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        if player_turn:
            print("Your Turn (X)")
            try:
                position = int(input("Enter position (1-9): "))
                if position < 1 or position > 9:
                    print("Invalid input! Please enter a number between 1 and 9.")
                    continue
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            if is_move_legal(board, position):
                row, col = position_map[position]
                board[row][col] = 'X'
                player_turn = False
            else:
                print("Invalid move. Try again.")
        else:
            print("Bot's Turn (O)")
            move = find_best_move(board)
            if move:
                row, col = move
                board[row][col] = 'O'
            player_turn = True

print("--------------------------------")
print("\tTic Tac Toe")
print("\tMin Max Algorithm")
print("--------------------------------")
play_tic_tac_toe()
