import json_convertor
import pytest

# Test read_and_load function
def test_take_in_empty_list_and_empty_file_name():
    test_list = []
    result = json_convertor.read_and_load("",test_list)
    assert result == False

def test_take_in_empty_list_only_and_the_file_exists_with_correct_json_format():
    test_list = []
    result = json_convertor.read_and_load("test_file_correct_json_format.txt",test_list)
    assert result == True

def test_take_in_empty_file_name_only():
    test_list = ["apple","orange","banana"]
    result = json_convertor.read_and_load("",test_list)
    assert result == False

def test_take_in_the_file_exists_with_incorrect_json_format():
    test_list = []
    result = json_convertor.read_and_load("test_file_incorrect_json_format",test_list)
    assert result == False

def test_take_in_a_list_with_same_format_with_and_the_file_exists_with_correct_json_format():
    test_list = [{"name": "It takes two", "required storage": 70}, {"name": "God of War", "required storage": 70}]
    result = json_convertor.read_and_load("test_file_correct_json_format.txt",test_list)
    assert result == True

def test_take_in_a_list_with_different_format_with_and_the_file_exists_with_correct_json_format():
    test_list = ["apple","orange","banana"]
    result = json_convertor.read_and_load("test_file_correct_json_format.txt",test_list)
    assert result == True