import tkinter as tk
from tkinter import messagebox

# Define the Tic Tac Toe board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Define the player symbols
player1 = 'Player 2'
player2 = 'Player 1'
current_player = player1

# Define the winning combinations
winning_combinations = []

# Function to check if a player has won
def check_winner():
    for combination in winning_combinations:
        if board[combination[0][0]][combination[0][1]] == board[combination[1][0]][combination[1][1]] == board[combination[2][0]][combination[2][1]] != ' ':
            return True
    return False

# Function to check if the game is a draw
def check_draw():
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

# Function to make a move
def make_move(row, col):
    global current_player
    if board[row][col] == ' ':
        board[row][col] = current_player
        if current_player == player1:
            current_player = player2
            buttons[row][col].config(bg='yellow')  # Change button color to yellow for player 2
        else:
            current_player = player1
            buttons[row][col].config(bg='blue')  # Change button color to blue for player 1
        if check_winner():
            messagebox.showinfo("Tic Tac Toe", f"{current_player} wins!")
            reset_board()
        elif check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            reset_board()
    else:
        messagebox.showerror("Tic Tac Toe", "Invalid move!")

# Function to reset the board
def reset_board():
    global board, current_player
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = player1
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=' ', bg='white')

# Create the GUI
root = tk.Tk()
root.title("Tic Tac Toe")

buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        button = tk.Button(root, text=' ', font=('Arial', 24), width=3, height=2, command=lambda r=row, c=col: make_move(r, c))
        button.grid(row=row, column=col)
        buttons[row][col] = button

reset_button = tk.Button(root, text='Reset', font=('Arial', 12), command=reset_board)
reset_button.grid(row=3, column=1)

# Define the winning combinations
winning_combinations = [
    [(0, 0), (0, 1), (0, 2)],  # Row 1
    [(1, 0), (1, 1), (1, 2)],  # Row 2
    [(2, 0), (2, 1), (2, 2)],  # Row 3
    [(0, 0), (1, 0), (2, 0)],  # Column 1
    [(0, 1), (1, 1), (2, 1)],  # Column 2
    [(0, 2), (1, 2), (2, 2)],  # Column 3
    [(0, 0), (1, 1), (2, 2)],  # Diagonal 1
    [(0, 2), (1, 1), (2, 0)]   # Diagonal 2
]

root.mainloop()

