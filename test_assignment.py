import pytest
from datetime import datetime
from assignment import (
    check_age_21,
    check_grade_level,
    check_date_of_birth,
    check_the_list_of_cars,
    check_if_you_can_drive,
    check_weather,
    check_if_you_can_play_game,
    check_study_time_or_play_time,
    make_the_input_store_in_variable,
    check_if_the_number_is_even
)

def test_check_age_21():
    assert check_age_21({'age': 21}) == True
    assert check_age_21({'age': 25}) == True
    assert check_age_21({'age': 18}) == False

def test_check_grade_level():
    assert check_grade_level({'grade': 9}) == 'freshman'
    assert check_grade_level({'grade': 10}) == 'sophomore'
    assert check_grade_level({'grade': 11}) == 'junior'
    assert check_grade_level({'grade': 12}) == 'senior'
    assert check_grade_level({'grade': 8}) == 'Invalid'

def test_check_date_of_birth():
    current_year = datetime.now().year
    assert check_date_of_birth({'birth_year': 1990}) == True
    assert check_date_of_birth({'birth_year': current_year}) == True
    assert check_date_of_birth({'birth_year': 1800}) == False

def test_check_the_list_of_cars():
    assert check_the_list_of_cars({'cars': ['Toyota', 'Honda', 'Ford']}) == True
    assert check_the_list_of_cars({'cars': ['Toyota', 'Toyota', 'Toyota']}) == False
    assert check_the_list_of_cars({'cars': ['Toyota', 'Honda']}) == False

def test_check_if_you_can_drive():
    assert check_if_you_can_drive({'can_drive': 'yes'}) == True
    assert check_if_you_can_drive({'can_drive': 'no'}) == True
    assert check_if_you_can_drive({'can_drive': 'maybe'}) == False

def test_check_weather():
    assert check_weather({'weather': 'sunny'}) == True
    assert check_weather({'weather': 'rainy'}) == True
    assert check_weather({'weather': 'foggy'}) == False
    assert check_weather({'weather': 'wind'}) == True

def test_check_if_you_can_play_game():
    # This test might fail randomly. It is better to check if the return type is correct.
    result = check_if_you_can_play_game({})
    assert result in ["You can play the game", "You can't play the game"]

def test_check_study_time_or_play_time():
    assert check_study_time_or_play_time({'study_or_play': 'study'}) == True
    assert check_study_time_or_play_time({'study_or_play': 'play'}) == True
    assert check_study_time_or_play_time({'study_or_play': 'sleep'}) == False

def test_make_the_input_store_in_variable():
    assert make_the_input_store_in_variable({'input': 'hello'}) == 'hello'
    assert isinstance(make_the_input_store_in_variable({'input': '123'}), str)

def test_check_if_the_number_is_even():
    assert check_if_the_number_is_even({'number': 4}) == True
    assert check_if_the_number_is_even({'number': 3}) == False
    assert check_if_the_number_is_even({'number': 0}) == True
