import random
import json
import time
import datetime

#Add please
from os import path
from threading import Thread

import playsound #Needs to be installed

#Play the Drum Roll
def play():
    current_path = path.abspath('.\\')
    playsound.playsound(current_path+"\\" +'drum-roll-please-6386.mp3')


def get_settings(file):
    with open(file, 'r') as file:
        settings = json.load(file)
    if settings['students'] == settings['winners']:
        settings['winners'] = []
    if datetime.datetime.now().month!=12:
        raise ValueError('STOP! It is not even December!!')
    today = datetime.datetime.now().day
    if today<settings['day']:
        raise ValueError(f'STOP, you have to wait!! Today is only the {today}th, but you try to run the code for the {settings["day"]}th')
    return settings

def save_settings(s, file):
    with open(file, 'w') as file:
        json.dump(s, file)
    print('Settings saved')

def get_students_candidates(all_students, winners):
    """Filters out students that have not yet won

    Args:
        all_students (list): all students
        winners (list): all winners to date

    Returns:
        list: remaining students that have not yet won
    """
    students_candidates = []
    for student in all_students:
        if student not in winners:
            students_candidates.append(student)
    return students_candidates

def announcement(winner, day, n_sec=3):
    print(f'And the winner for {day}th of Decmeber is, ', end='', flush=True)

    play_thread = Thread(target=play)
    play_thread.start()
    time.sleep(1.5)
    for i in reversed(range(1,n_sec+1)):
        print(f'{i}... ', end='', flush=True)
        time.sleep(1)
    print(f'{winner}!!!', flush=True)

settings_file = 'settings.json'
settings = get_settings(settings_file)

,target_students = get_students_candidates(settings['students'], settings['winners'])
winner = random.choice(target_students)

settings['winners'].append(winner)
settings['day'] += 1

announcement(winner, settings['day'])
save_settings(settings, settings_file)
