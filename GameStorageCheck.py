# Small program check if you have enough space in current disk to install a certain PC game
import shutil
import os.path
import json

# Create some sample game dict
game1 = {"name": "League of Legends","required storage":8}
game2 = {"name": "World of Warcraft","required storage":100}
game3 = {"name": "Fortnite","required storage":16}
game4 = {"name": "Super Mario Bros","required storage":0.2}
game5 = {"name": "Elden Ring","required storage":60}

# Create a game list
global gamelist
gamelist = []

# Add sample games to the list
def add_games():
    gamelist.append(game1)
    gamelist.append(game2)
    gamelist.append(game3)
    gamelist.append(game4)
    gamelist.append(game5)

# Check user's input
def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        return val
    except ValueError:
        # If user inputs 'q' return 0
        if input == "q":
            return 0
        # If user inputs 'a' return -2
        elif input == "a":
            return -2
        # If user inputs anything else return -1
        else:
            return -1

# List all the games
def list_games():
    print("{:<3} {:<30} {:<15}".format('ID','Game ','GB Storage '))
    print("{:<48}".format('============================================'))
    index = 1
    for x in gamelist:
        print("{:<3} {:<30} {:<15}".format(str(index) ,x.get("name"), str(x.get("required storage")) + "GB"))
        index = index + 1

# Get the value of free storage of your current disk
def get_system_free_storage():
    total, used, free = shutil.disk_usage("/")
    print("FreeSpace in your current disk: %d GB" % (free // (2**30)))
    return free // (2**30)

# Print message when user's input is not valid
def print_invalid_message():
    print("User input is not valid. Please try again!")

# Read a txt file contain a json object parse it to a list, if the file is not exist create one and load sample data to the list
def read_and_load():
    #Check if the file exist
    file_exists = os.path.exists('gamelistfile.txt')
    if file_exists: 
        # Read the file
        f = open("gamelistfile.txt","r")
        json_text = f.read()
        # Parse it to a list
        jdata = json.loads(json_text)
        for item in jdata:
            gamelist.append(item)
    else :
        # Create a txtfile
        f = open("gamelistfile.txt","x")
        # Load sample data
        add_games()
        
# Convert the game list to a json object and save it to the file
def convert_and_save():
    f = open("gamelistfile.txt","w")
    f.write(json.dumps(gamelist))

# Main Programe
menu = True
read_and_load()
while menu:
    print("PC Game List:")
    print("\n")
    list_games()
    print("\n")
    user_input = input("Please choose the game you want to install and play (a to add a game, q to quit):")
    print("\n")
    checked_input = check_user_input(user_input)
    if checked_input > 0 and checked_input - 1 < len(gamelist):
        selected_game = gamelist[checked_input - 1]
        free_space = get_system_free_storage()
        required_space = selected_game.get("required storage")
        if  free_space >= required_space:
            print("Congrats! You have enough space to install the game "+ selected_game.get("name"))
        else:
            space_need_to_free = required_space - free_space
            print("Oops, You don't have enough space to install the game "+ selected_game.get("name"))
            print("You have to free at least " + str(space_need_to_free) + "GB to install the game "+ selected_game.get("name"))
    elif checked_input == 0:
            convert_and_save()
            quit()
    elif checked_input == -2:
            input_game = input("Please enter the name of the game you wish to add:")
            input_game_storage = input("Please enter the disk storage reqiurement for the game (GB)")
            checked_input_game_storage= check_user_input(input_game_storage)
            if checked_input_game_storage > 0:
                add_game = {"name": input_game,"required storage":checked_input_game_storage}
                gamelist.append(add_game)
                print("Game successfully added!")
            else:
                print_invalid_message()               
    else:
        print_invalid_message()
    print("\n")
    user_input2 = input("Press Enter to continue or press q to exit: ") 
    if user_input2 == "q":
        convert_and_save()
        quit()
    else:
        print("\n")  
    
