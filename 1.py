from project_num_1 import get_integer_input, winner, computer_move, overture, select_random_symbol
game_overture = overture()

while True:
    game_mode: int = get_integer_input("Enter 1 to play against another player or 2 to play against the computer: ")
    while game_mode not in [1, 2]:
        print("Invalid input! Please enter 1 or 2.")
        game_mode: int = get_integer_input("Enter 1 to play against another player or 2 to play against the computer: ")

    player1_name = input("Player1: enter your name :")

    if game_mode == 1:
        player2_name = input("Player2: enter your name :")

    user_choice = get_integer_input(f"{player1_name} Enter 1 to be 'X' or 2 to be 'O' or enter 3 for random symbol: ")
    while user_choice not in [1, 2, 3]:
        print("Invalid input! Please enter 1 or 2 or 3.")
        user_choice = get_integer_input("Enter 1 to be 'X' or 2 to be 'O' or enter 3 for random symbol: ")

    if user_choice == 1:
        player1_symbol = "X"
    elif user_choice == 2 :
        player1_symbol = "O"
    else:
        player1_symbol = select_random_symbol()

    if player1_symbol == "X":
        player2_symbol = "O"
    else:
        player2_symbol = "X"

    print(f"{player1_name} is {player1_symbol}.")

    if game_mode == 1:
        print(f"{player2_name} is {player2_symbol}.")
    else:
        print(f"The computer will play as {player2_symbol}.")

    arr = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
    ]

    turn = player1_symbol
    while True:
        print("-------------------------------")
        for row in arr:
            print(" ".join(row))
        print("-------------------------------")

        if game_mode == 1 or turn == player1_symbol:
            print(f"{turn} is turn.")
            row = get_integer_input("Enter the row (0, 1, 2): ")
            column = get_integer_input("Enter the column (0, 1, 2): ")

            if 0 <= row < 3 and 0 <= column < 3:
                if arr[row][column] == "_":
                    arr[row][column] = turn
                else:
                    print("That spot is already taken. Try again.")
                    continue
            else:
                print("Invalid position. Please choose a row and column between 0 and 2.")
                continue
            print("-------------------------------")
        else:
            print(f"The computer ({turn}) is making a move...")
            row, column = computer_move(arr)
            arr[row][column] = turn
            print(f"The computer placed its symbol at row {row}, column {column}.")

        game_winner = winner(arr)
        if game_winner is not None:
            for row in arr:
                print(" ".join(row))
            print(f"{game_winner} wins!")
            break

        is_full = True
        for row in arr:
            for cell in row:
                if cell == "_":
                    is_full = False
                    break
            if not is_full:
                break

        if is_full:
            for row in arr:
                print(" ".join(row))
            print("It's a draw!")
            break

        turn = player2_symbol if turn == player1_symbol else player1_symbol

    replay = input("Play another game? Enter '1' for yes, any other key to exit: ")
    if replay != "1":
        break

print("Thanks for playing Tic Tac Toe!")
