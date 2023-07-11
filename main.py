import random

board_numbers = {"1": " ", "2": " ", "3": " ",
                 "4": " ", "5": " ", "6": " ",
                 "7": " ", "8": " ", "9": " "}

player_picks = []
computer_picks = []


def print_board(board):
    print(f" {board['1']} | {board['2']} | {board['3']} ")
    print("-----------")
    print(f" {board['4']} | {board['5']} | {board['6']} ")
    print("-----------")
    print(f" {board['7']} | {board['8']} | {board['9']} ")


def pick_board_space():
    space = input("Pick a space: ")
    board_numbers[space] = "X"
    player_picks.append(space)

    computer_space = random.randint(1, 9)
    while True:
        if str(computer_space) not in player_picks and str(computer_space) not in computer_picks:
            board_numbers[str(computer_space)] = "O"
            computer_picks.append(str(computer_space))
            print_board(board_numbers)
            return False
        else:
            computer_space = random.randint(1, 9)


def game():
    game_playing = True
    while game_playing:
        pick_board_space()

        if board_numbers["1"] == board_numbers["2"] and board_numbers["1"] == board_numbers["3"] \
                and board_numbers["1"] != " ":
            if board_numbers["1"] == "X":
                print("You are the winner!")
            else:
                print("The computer wins!")
            game_playing = False
        elif board_numbers["4"] == board_numbers["5"] and board_numbers["4"] == board_numbers["6"] \
                and board_numbers["4"] != " ":
            if board_numbers["4"] == "X":
                print("You are the winner!")
            else:
                print("The computer wins!")
            game_playing = False
        elif board_numbers["7"] == board_numbers["8"] and board_numbers["7"] == board_numbers["9"] \
                and board_numbers["7"] != " ":
            if board_numbers["7"] == "X":
                print("You are the winner!")
            else:
                print("The computer wins!")
            game_playing = False
        elif board_numbers["1"] == board_numbers["4"] and board_numbers["1"] == board_numbers["7"] \
                and board_numbers["1"] != " ":
            if board_numbers["1"] == "X":
                print("You are the winner!")
            else:
                print("The computer wins!")
            game_playing = False
        elif board_numbers["2"] == board_numbers["5"] and board_numbers["2"] == board_numbers["8"] \
                and board_numbers["2"] != " ":
            if board_numbers["2"] == "X":
                print("You are the winner!")
            else:
                print("The computer wins!")
            game_playing = False
        elif board_numbers["3"] == board_numbers["6"] and board_numbers["3"] == board_numbers["9"] \
                and board_numbers["3"] != " ":
            if board_numbers["3"] == "X":
                print("You are the winner!")
            else:
                print("The computer wins!")
            game_playing = False
        elif board_numbers["1"] == board_numbers["5"] and board_numbers["1"] == board_numbers["9"] \
                and board_numbers["1"] != " ":
            if board_numbers["1"] == "X":
                print("You are the winner!")
            else:
                print("The computer wins!")
            game_playing = False
        elif board_numbers["3"] == board_numbers["5"] and board_numbers["3"] == board_numbers["7"] \
                and board_numbers["3"] != " ":
            if board_numbers["3"] == "X":
                print("You are the winner!")
            else:
                print("The computer wins!")
            game_playing = False

        for num in board_numbers:
            if board_numbers[num] == " ":
                game_playing = True
            else:
                game_playing = False


if __name__ == "__main__":
    game()
