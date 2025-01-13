import random

def overture():
    print("Welcome to the Tic Tac Toe game.")
    print("Type 1 so we can proceed.")

    user: int = int(get_integer_input("Enter 1: "))
    while user != 1:
        print("Invalid input! Please enter the number 1.")
        user: int = get_integer_input("Enter 1 to proceed: ")

def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def computer_move(arr):
    empty_positions = [(i, j) for i in range(3) for j in range(3) if arr[i][j] == "_"]
    return random.choice(empty_positions)

def winner(arr):
    # Check rows and columns for a winner
    for i in range(3):
        if arr[i][0] == arr[i][1] == arr[i][2] and arr[i][0] != "_":
            return arr[i][0]
        if arr[0][i] == arr[1][i] == arr[2][i] and arr[0][i] != "_":
            return arr[0][i]

    # Check diagonals for a winner
    if arr[0][0] == arr[1][1] == arr[2][2] and arr[0][0] != "_":
        return arr[0][0]
    if arr[2][0] == arr[1][1] == arr[0][2] and arr[2][0] != "_":
        return arr[2][0]

    return None

def select_random_symbol():
    symbol = random.randint(1,2)
    if symbol == 1:
        return "X"
    else:
        return "O"






