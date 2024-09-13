import random
from datetime import datetime

def check_age_21(user_input: dict) -> bool:
    """
    Takes a dictionary input for age, returns True if the age is 21 or older.
    """
    age = user_input.get('age', 0)
    if isinstance(age, int) and age >= 21:
        return True
    return False

def check_grade_level(user_input: dict) -> str:
    """
    Takes a dictionary input for grade and returns the corresponding grade level (freshman, sophomore, etc.).
    """
    grade_level_map = {9: 'freshman', 10: 'sophomore', 11: 'junior', 12: 'senior'}
    grade = user_input.get('grade', None)
    if grade in grade_level_map:
        return grade_level_map[grade]
    return "Invalid"

def check_date_of_birth(user_input: dict) -> bool:
    """
    Takes a dictionary input for year of birth, returns True if the year is between 1900 and the current year.
    """
    current_year = datetime.now().year
    birth_year = user_input.get('birth_year', 0)
    if 1900 <= birth_year <= current_year:
        return True
    return False

def check_the_list_of_cars(user_input: dict) -> bool:
    """
    Takes a dictionary input of cars, returns True if there are at least 3 different models.
    """
    cars = user_input.get('cars', [])
    return len(set(cars)) >= 3

def check_if_you_can_drive(user_input: dict) -> bool:
    """
    Takes a dictionary input of drive response, returns True if response is valid.
    """
    can_drive = user_input.get('can_drive', "").lower()
    return can_drive in ['yes', 'no']

def check_weather(user_input: dict) -> bool:
    """
    Takes a dictionary input of weather, returns True if weather condition is valid.
    """
    valid_weather_conditions = ['sunny', 'rainy', 'snowy', 'wind']
    weather = user_input.get('weather', "").lower()
    return weather in valid_weather_conditions

def check_if_you_can_play_game(user_input: dict) -> str:
    """
    Randomly returns if you can play the game or not based on a random boolean.
    """
    return "You can play the game" if random.choice([True, False]) else "You can't play the game"

def check_study_time_or_play_time(user_input: dict) -> bool:
    """
    Takes a dictionary input for study or play time, returns True if input is valid.
    """
    valid_times = ['study', 'play']
    study_or_play = user_input.get('study_or_play', "").lower()
    return study_or_play in valid_times

def make_the_input_store_in_variable(user_input: dict) -> str:
    """
    Takes a dictionary input, and stores it in a variable. 
    """
    return user_input.get('input', "")

def check_if_the_number_is_even(user_input: dict) -> bool:
    """
    Takes a dictionary input of a number, returns True if the number is even.
    """
    number = user_input.get('number', 0)
    return number % 2 == 0
