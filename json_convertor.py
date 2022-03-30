'''This module is used for converting a txt file in json format to a list,
or a list to a json format txt file and save it'''
import os.path
import json
import traceback

def read_and_load(file_name,converted_list):
    '''Read a txt file contain a json object parse it to a list,
    if the file is not exist create one.
    it takes two arguments one is the file name, the other is the list
    it will return True if the file is exist and loaded,
    return False if the file is not exist or fail to read and parsing to the list'''
    #Check if the file exist
    file_exists = os.path.exists(file_name)
    if file_exists:
        # Read the file
        with open(file_name,"r",encoding="utf-8") as list_file:
            json_text = list_file.read()
        # Parse it to a list
            try:
                jdata = json.loads(json_text)
                for item in jdata:
                    converted_list.append(item)
                return True
            except Exception:
                print(traceback.format_exc())
                return False
        # Create a txtfile
    try:
        with open(file_name,"x",encoding="utf-8") as list_file:
            list_file.close()
    except Exception:
        print(traceback.format_exc())
    return False

def convert_and_save(list_to_convert):
    '''Convert the list to a json object and save it to the file'''
    with open("game_list_file.txt","w",encoding="utf-8") as list_file:
        list_file.write(json.dumps(list_to_convert))
