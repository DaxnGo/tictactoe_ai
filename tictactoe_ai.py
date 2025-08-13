# Tic-Tac-Toe with unbeatable AI (Minimax + Alpha-Beta)
# Run: python tictactoe_ai.py

import math

EMPTY = " "
HUMAN = "X"
AI = "O"
WIN_LINES = [
    (0,1,2),(3,4,5),(6,7,8),  # rows
    (0,3,6),(1,4,7),(2,5,8),  # cols
    (0,4,8),(2,4,6)           # diagonals
]

def print_board(b):
    print("\n")
    for r in range(3):
        row = " | ".join(b[r*3:(r+1)*3])
        print(" " + row)
        if r < 2:
            print("---+---+---")
    print("\n")

def print_positions():
    print("Positions:")
    pos = [str(i) for i in range(1,10)]
    print_board(pos)

def winner(b):
    for a, c, d in WIN_LINES:
        if b[a] != EMPTY and b[a] == b[c] == b[d]:
            return b[a]
    return None

def is_full(b):
    return all(s != EMPTY for s in b)

def available_moves(b):
    return [i for i, s in enumerate(b) if s == EMPTY]

def evaluate(b):
    w = winner(b)
    if w == AI:    return 1
    if w == HUMAN: return -1
    return 0

def minimax(b, depth, alpha, beta, maximizing):
    w = winner(b)
    if w or is_full(b):
        return evaluate(b)

    if maximizing:
        best = -math.inf
        for move in available_moves(b):
            b[move] = AI
            score = minimax(b, depth+1, alpha, beta, False)
            b[move] = EMPTY
            best = max(best, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for move in available_moves(b):
            b[move] = HUMAN
            score = minimax(b, depth+1, alpha, beta, True)
            b[move] = EMPTY
            best = min(best, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best

def best_move(b):
    best_score = -math.inf
    move_choice = None
    for move in available_moves(b):
        b[move] = AI
        score = minimax(b, 0, -math.inf, math.inf, False)
        b[move] = EMPTY
        if score > best_score:
            best_score = score
            move_choice = move
    return move_choice

def play():
    print("=== Tic-Tac-Toe (You vs Unbeatable AI) ===")
    print_positions()

    # Let the player choose symbol (optional). Defaults: HUMAN=X, AI=O
    choice = input("Do you want to be X and go first? (Y/n): ").strip().lower()
    human_first = (choice in ("", "y", "yes"))
    global HUMAN, AI
    if not human_first:
        HUMAN, AI = "O", "X"

    board = [EMPTY]*9
    turn = "HUMAN" if human_first else "AI"

    while True:
        print_board(board)

        if winner(board) or is_full(board):
            break

        if turn == "HUMAN":
            while True:
                try:
                    spot = int(input("Choose position 1-9: ")) - 1
                    if spot not in range(9):
                        print("Must be 1-9.")
                        continue
                    if board[spot] != EMPTY:
                        print("That spot is taken.")
                        continue
                    board[spot] = HUMAN
                    break
                except ValueError:
                    print("Please enter a number 1-9.")
            turn = "AI"
        else:
            move = best_move(board)
            board[move] = AI
            print(f"AI plays at {move+1}.")
            turn = "HUMAN"

    print_board(board)
    w = winner(board)
    if w == HUMAN:
        print("You win! 🎉")
    elif w == AI:
        print("AI wins. 😈")
    else:
        print("It's a draw. 🤝")

if __name__ == "__main__":
    play()
