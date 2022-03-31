'''Small program check if you have enough space in current disk to install a certain PC game
    1. Program will load a list of game from a txt file
    (if the file is not exist it will load some sample data)
    2. Program will ask you to choose a game from the list,
    and output whether or not your current disk have enough space to install it
    3. Program has the feature to add games into the list
    4. Program will save the game list into a txt file in json format afterwards
'''
import shutil
import sys
import json_convertor

# Create some sample game dict
game1 = {"name": "League of Legends","required storage":8}
game2 = {"name": "World of Warcraft","required storage":100}
game3 = {"name": "Fortnite","required storage":16}
game4 = {"name": "Super Mario Bros","required storage":0.2}
game5 = {"name": "Elden Ring","required storage":60}

# Create a game list
game_list = []

def add_games():
    '''Add sample games to the list'''
    game_list.append(game1)
    game_list.append(game2)
    game_list.append(game3)
    game_list.append(game4)
    game_list.append(game5)

def check_user_input(user_input):
    '''Check user's input and try to convert it to int, take a string input in return an int'''
    try:
        # Convert it into integer
        val = int(user_input)
        return val
    except ValueError:
        try:
            # Convert it into float
            val = float(user_input)
            return val
        except ValueError:
            # If user inputs 'q' return 0
            if user_input == "q":
                return 0
            # If user inputs 'a' return -2
            if user_input == "a":
                return -2
            # If user inputs anything else return -1
            return -1

def list_games():
    '''List all the games'''
    print(f'{"ID":3}{"Game":30}{"GB Storage":15}')
    print(f'{"":=<48}')
    index = 1
    for game in game_list:
        print(f'{str(index):3}{game.get("name"):30}{str(game.get("required storage"))+"GB":15}')
        index = index + 1

def get_system_free_storage():
    '''Get the value of free storage of your current disk'''
    free = shutil.disk_usage("/")[2]
    free_disk = free // (2**30)
    print(f"FreeSpace in your current disk: {free_disk} GB")
    #print("FreeSpace in your current disk: %d GB" % (free // (2**30)))
    return free // (2**30)

def print_invalid_message():
    '''Print message when user's input is not valid'''
    print("User input is not valid. Please try again!")

# Main Programe
GAME_MENU = True
if json_convertor.read_and_load("game_list_file.txt",game_list) is False:
    add_games()
while GAME_MENU:
    list_games()
    print("\n")
    menu_input = input("Please choose the game you want to install(a to add a game, q to quit): ")
    print("\n")
    checked_input = check_user_input(menu_input)
    if checked_input > 0 and checked_input - 1 < len(game_list) and type(checked_input) is int:
        selected_game = game_list[checked_input - 1]
        free_space = get_system_free_storage()
        required_space = selected_game.get("required storage")
        if  free_space >= required_space:
            print("Congrats! You have enough space to install the game "+
            selected_game.get("name"))
        else:
            space_need_to_free = required_space - free_space
            print("Oops, You don't have enough space to install the game "+
            selected_game.get("name"))
            print("You have to free at least " + str(space_need_to_free) +
            "GB to install the game "+ selected_game.get("name"))
    elif checked_input == 0:
        json_convertor.convert_and_save(game_list)
        sys.exit()
    elif checked_input == -2:
        input_game = input("Please enter the name of the game you wish to add: ")
        input_game_storage = input("Please enter the disk storage reqiurement for the game(GB): ")
        checked_input_game_storage= check_user_input(input_game_storage)
        if checked_input_game_storage > 0:
            add_game = {"name":input_game,"required storage":checked_input_game_storage}
            game_list.append(add_game)
            print("Game successfully added!")
        else:
            print_invalid_message()
    else:
        print_invalid_message()
    print("\n")
    user_input2 = input("Press Enter to continue or press q to exit: ")
    if user_input2 == "q":
        json_convertor.convert_and_save(game_list)
        sys.exit()
    else:
        print("\n")
