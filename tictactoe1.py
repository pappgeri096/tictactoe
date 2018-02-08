import random
from random import randint
import os

class bcolors:
    HEADER = '\033[1;32;40m' # green letters w/ black background
    QUESTION = '\033[1;37;40m' # black background for questions w/ white letters
    BOARD = '\033[1;37;40m' # black background
    HINT = '\033[1;31;40m' # green letters
    DRAW = '\033[1;0;41m' # red
    ENDC = '\033[0m'

def settings(key=None, value=None):
    default = {
        "player_one": 0,
        "player_two": 0,
        "draws": 0,
        "rounds": 1,
        "current": 0,
        "choice": "X",
        "boards": 5
    }

    if not (key is None and value is None) and key in default:
        default[key] = value
    
    return default

def clear_terminal():
    return os.system('clear')

def set_symbols(store, player_one):
    player_one = player_one.upper()
    if player_one == "X":
        store.extend((player_one, "O"))
    else:
        store.extend((player_one, "X"))
    return store

def check_symbol(symbol):
    if symbol.upper() == "X" or symbol.upper() == "O":
        return True
    return False  

def create_board(size):
    size = size * size
    board = []
    for num in range(0, size):
        board.append(" ")
    
    return board

def phrases():
    return {
        "Symbol": "Choose your symbol",
        "Game_Over":color.DRAW + "Finito! Good job!" + color.ENDC,
        "Player_One":color.DRAW + "PLAYER ONE WIN!" + color.ENDC,
        "Player_Two":color.DRAW + "PLAYER TWO WIN!" + color.ENDC,
        "Player_Step":color.QUESTION + "What's your choice?" + color.ENDC,
        "Draw":color.DRAW + "DRAW! NO WINNER!" + color.ENDC,
        "Invalid_Input":color.DRAW + "Nope! Try again!" + color.ENDC,
        "AI_Help":color.HINT + "Try this pls: " + color.ENDC,
        "Too_Big":color.QUESTION + "Please choose between 1-" + str(settings()["boards"] * settings()["boards"]) + color.ENDC
        }

def check_number(value):
    try:
        value = int(value)
    except ValueError:
        return False
    return True

def ai():
    collect = []
    for num in range(0, len(board)):
        if check_board(num):
            collect.append(num)
    return collect[randint(0, len(collect) - 1)]

def header():
    print(color.HEADER + """
,--------.,--.            ,--.                    ,--------.              
'--.  .--'|  | ,---.    ,-'  '-. ,--,--. ,---.    '--.  .--',---.  ,---.  
   |  |   |  || .--'    '-.  .-'' ,-.  || .--'       |  |  | .-. || .-. : 
   |  |   |  |\ `--.      |  |  \ '-'  |\ `--.       |  |  ' '-' '\   --. 
   `--'   `--' `---'      `--'   `--`--' `---'       `--'   `---'  `----' """ + color.ENDC)

def check_board(number):
    number = int(number)
    if number <= (board_size * board_size) and number > 0:
        if board[number - 1] == "X" or board[number - 1] == "O":
            return False
        else:
            return True
    else:
        return False

''' def show_board():
    print(color.BOARD + "-------------------" + color.ENDC)
    print(color.BOARD + "|   ""  |  ""   |  ""   |" + color.ENDC)
    print(color.BOARD + "|  " + board[0] + "  |  " + board[1] + "  |  " + board[2] + "  |" + color.ENDC)
    print(color.BOARD + "|   ""  |  ""   |  ""   |" + color.ENDC)    
    print(color.BOARD + "-------------------" + color.ENDC)
    print(color.BOARD + "|   ""  |  ""   |  ""   |" + color.ENDC)
    print(color.BOARD + "|  " + board[3] + "  |  " + board[4] + "  |  " + board[5] + "  |" + color.ENDC)
    print(color.BOARD + "|   ""  |  ""   |  ""   |" + color.ENDC)
    print(color.BOARD + "-------------------" + color.ENDC)
    print(color.BOARD + "|   ""  |  ""   |  ""   |" + color.ENDC)
    print(color.BOARD + "|  " + board[6] + "  |  " + board[7] + "  |  " + board[8] + "  |" + color.ENDC)
    print(color.BOARD + "|   ""  |  ""   |  ""   |" + color.ENDC)
    print(color.BOARD + "-------------------" + color.ENDC) '''

def show_board():
    store_board = ""
    lining = ""
    print(color.BOARD + "-" + ("------"*board_size) + color.ENDC)

    for place in range(0, len(board)):
        if (place + 1) % board_size == 0:
            store_board += board[place] + "  |"
            lining += "  |"
            print(color.BOARD + lining + color.ENDC)
            print(color.BOARD + store_board + color.ENDC)
            print(color.BOARD + lining + color.ENDC)
            print(color.BOARD + "-" + ("------"*board_size) + color.ENDC)
            store_board = ""
            lining = ""
        elif (place + 1) % board_size == 1:
            store_board += "|  " + board[place] + "  |  "
            lining = "|  " + "   |   "
        else:
            store_board += board[place] + "  |  "
            lining += "  |   "


def check_winner(symbol, board, board_size):
    for index in range(len(board)):
        if board[index] == symbol and check_index(board, index + 1) == symbol and check_index(board, index - 1) == symbol and not (index % board_size == 0):
            return True
        elif board[index] == symbol and check_index(board, index - board_size) == symbol and check_index(board, index + board_size) == symbol:
            return True
        elif board[index] == symbol and check_index(board, index - (board_size - 1)) == symbol and check_index(board, index + (board_size - 1)) == symbol and index > board_size:
            return True
        elif board[index] == symbol and check_index(board, index - (board_size + 1)) == symbol and check_index(board, index + (board_size + 1)) == symbol and index < (board_size * board_size) - board_size:

            return True
    return False

def check_index(board, index):
    try:
        b = board[index]
    except IndexError:
        return False
    return board[index]   

def no_winner():
    if (player_one == player_two or
       (Draws == 3 and player_one == 0 and player_two == 0)):
        return True
    return False
    
def all_reserved():
    count = 0
    for item in board:
        if item == "X" or item =="O":
            count += 1
    
    if count == (settings()["boards"] * settings()["boards"]):
        return True
    return False

def last_round():
    if rounds > 3:
        return True
    return False

def user_input(ask):
    return input(ask)

def change_game_mode(mode):
    if(check_number(mode)):
        mode = int(mode)

    if mode == 1:
        return True
    return False


def board_size(size):
    if(check_number(size) and int(size) > 2):
        size = int(size)
        return size
    else:
        return 3

def change_player(current):
    if current == 1:
        return 0
    else:
        return 1

def duplicate_board():
    dupboard = []

    for i in board:
        dupboard.append(i)
    
    return dupboard

def artint_turn():
    if settings()["player_one"] == "X":
        return 0
    return 1

def artint():
    for i in range(0,25):
        board_duplicate = duplicate_board()
        if board_duplicate[i] == " ":
            board_duplicate[i] = choices[1]
            if check_winner(choices[1], board_duplicate, board_size):
                return i+1
    
    for i in range(0,25):
        board_duplicate = duplicate_board()
        if board_duplicate[i] == " ":
            board_duplicate[i] = choices[0]
            if check_winner(choices[0], board_duplicate, board_size):
                return i+1
                
    return randint(1,24)


    ''' for i in range(0,24):
        board_duplicate = duplicate_board()
        if board_duplicate[i] == " ":
            board_duplicate[i] = settings()["player_two"]
            if check_step(settings()["player_two"], board_duplicate, settings()["boards"]):
                return i  '''

color = bcolors()
header()


player_one = settings()["player_one"]
player_two = settings()["player_two"]
Draws = settings()["draws"]
rounds = settings()["rounds"]
current_player = settings()["current"]
choices = []
Phrases = phrases()

game_mode = input("1 or 2 player?")
board_size_ask = input("Board size?")
board_size = board_size(board_size_ask)
board = create_board(board_size)
single_player = change_game_mode(game_mode)
player_input = input((Phrases["Symbol"])).upper()

if not check_symbol(player_input):
    player_input = settings()["choice"]

if check_symbol(player_input):
    choices = set_symbols(choices, player_input)
    
    while True:
        if last_round(): 
            if no_winner():
                rounds = settings("rounds", (rounds-1))["rounds"]
                continue
            else:
                clear_terminal()
                print(Phrases["Game_Over"])

            if player_one > player_two:
                print(Phrases["Player_One"])         
            else:
                print(Phrases["Player_Two"])
            print(color.QUESTION + "PLAYER ONE: " + str(player_one) + " | draws: " + str(Draws) + " | PLAYER TWO: " + str(player_two) + color.ENDC)    
            break
                          
        header()
        show_board()
        print(color.QUESTION + "PLAYER ONE: " + str(player_one) + " | draws: " + str(Draws) + " | PLAYER TWO: " + str(player_two) + color.ENDC)
        print(color.QUESTION + "PLAYER " + choices[current_player] + " TURN | ROUND " + str(rounds) + color.ENDC)
        
        if single_player == True and current_player == artint_turn():
            player_input = artint()
        else:
            player_input = input(Phrases["Player_Step"])

        if check_number(player_input):

            if check_board(player_input):
                board[int(player_input) - 1] = choices[current_player]
               
                if check_winner(choices[current_player], board, board_size):
                    print(color.DRAW + "PLAYER " + choices[current_player] + " WIN!" + color.ENDC)
                    
                    if current_player == 0:
                        player_one += 1
                    else:
                        player_two += 1

                    rounds += 1
                    board = create_board(board_size)

                    continue
                
                current_player = change_player(current_player)
        
                if all_reserved():
                    print(Phrases["Draw"])
                    Draws += settings("draws", Draws+1)["draws"]
                    rounds +=  settings("rounds", rounds+1)["rounds"]
                    board = create_board(settings()["boards"])
                    continue

            else:
                print(Phrases["Invalid_Input"])
                continue
        elif player_input == "help":
            print(Phrases["AI_Help"] + str(ai()))
            continue
        else:
            print(Phrases["Too_Big"])
            continue
        