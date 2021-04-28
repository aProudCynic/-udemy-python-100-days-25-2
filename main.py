import pandas
from turtle import Screen

from pandas.core.frame import DataFrame
from state_display import StateDisplay

STATES_FILE_PATH = '50_states.csv'
US_STATE_MAP_FILE_PATH = 'blank_states_img.gif'

def load_states_from_file():
    return pandas.read_csv(STATES_FILE_PATH)
    
screen = Screen()
screen.bgpic(US_STATE_MAP_FILE_PATH)

states_not_guessed = load_states_from_file()
correct_guesses = DataFrame()
start_number_of_states = len(states_not_guessed)
while len(states_not_guessed) > 0:
    
    guess = screen.textinput(f'{len(states_not_guessed)}/{start_number_of_states} left', f'Guess a state: ').capitalize()
    state_guessed = states_not_guessed[states_not_guessed['state'] == guess]
    if not state_guessed.empty:
        states_not_guessed = states_not_guessed[states_not_guessed['state'] != guess]
        correct_guesses.add(state_guessed)
        StateDisplay(state_guessed)
screen.exitonclick()
