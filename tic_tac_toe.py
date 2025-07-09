"""Simple Tic-Tac-Toe game for the console.

The board is displayed using ASCII art. Players enter their moves using
coordinates in the form "row,col" where both row and column values start at 1.
"""

from typing import List

Board = List[List[str]]


def print_board(board: Board) -> None:
    """Print the current state of the game board."""
    print("   1   2   3")
    for i, row in enumerate(board):
        print(f"{i + 1}  {row[0]} | {row[1]} | {row[2]}")
        if i < 2:
            print("  ---+---+---")


def check_winner(board: Board, player: str) -> bool:
    """Return True if the given player has a winning line."""
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def get_move(player: str, board: Board) -> tuple[int, int]:
    """Prompt the player for a move and return a valid (row, col) tuple."""
    while True:
        move = input(f"Player {player}, enter your move (row,col): ")
        try:
            row_str, col_str = move.split(',')
            row, col = int(row_str), int(col_str)
        except ValueError:
            print("Invalid format. Please use row,col (e.g. 1,3).")
            continue

        if not (1 <= row <= 3 and 1 <= col <= 3):
            print("Coordinates must be between 1 and 3.")
            continue
        if board[row - 1][col - 1] != " ":
            print("That cell is already taken. Choose another one.")
            continue
        return row - 1, col - 1


def main() -> None:
    board: Board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row, col = get_move(current_player, board)
        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if all(cell != " " for r in board for cell in r):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
