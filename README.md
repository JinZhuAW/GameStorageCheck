# GameStorageCheck
Small program check if you have enough space in current disk to install a certain PC game

    1. Program will load a list of game from a txt file (if the file is not exist it will load some sample data).
    2. Program will ask you to choose a game from the list, and output whether or not your current disk have enough space to install it.
    3. Program has the feature to add games into the list.
    4. Program will save the game list into a txt file in json format afterwards.

File Description
1. game_storage_check.py: This file is the main program, it uses the module json_convertor.
2. json_convertor.py: This file is a module which is used to read open, and save a txt file and convert it to a json string format.
3. test_json_convertor.py: This file is the test file used to test json_convertor.py. More test scenarios will be added.
4. test_flie_correct_json_format.txt: The file is used for some test scenarios created above.
5. test_file_incorrect_json_format: The file is also used for some test scenarios created above.
