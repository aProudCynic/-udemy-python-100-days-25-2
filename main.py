import pandas

STATES_FILE_PATH = '50_states.csv'

def load_states_from_file():
    return pandas.read_csv(STATES_FILE_PATH)
    
states_not_guessed = load_states_from_file()
while len(states_not_guessed) > 0:
    guess = input(f'Guess a state ({len(states_not_guessed)} left): ')
    state_guessed = states_not_guessed[states_not_guessed['state'] == guess]
    if not state_guessed.empty:
        print(f'{guess} is correct')
    else:
        print(f'{guess} is incorrect, try again')