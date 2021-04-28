import pandas
from turtle import Screen, mainloop, bye

from pandas.core.frame import DataFrame
from state_display import StateDisplay

STATES_FILE_PATH = '50_states.csv'
US_STATE_MAP_FILE_PATH = 'blank_states_img.gif'
EXIT_KEYWORD = 'Exit'

def load_states_from_file():
    return pandas.read_csv(STATES_FILE_PATH)
    
screen = Screen()
screen.bgpic(US_STATE_MAP_FILE_PATH)

states_not_guessed = load_states_from_file()
correct_guesses = []
start_number_of_states = len(states_not_guessed)
game_over = False
while not game_over:
    
    guess = screen.textinput(f'{len(correct_guesses)}/{start_number_of_states} States Correct', f"What's another state name?: ").capitalize()
    if guess != EXIT_KEYWORD:
        state_guessed = states_not_guessed[states_not_guessed['state'] == guess]
        if not state_guessed.empty:
            states_not_guessed = states_not_guessed[states_not_guessed['state'] != guess]
            correct_guesses.append(state_guessed)
            StateDisplay(state_guessed)
    game_over = guess == EXIT_KEYWORD or len(states_not_guessed) > 0
states_not_guessed.to_csv('states_to_learn.csv')
bye()
mainloop()
