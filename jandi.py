import os
import json
import characters
import datetime

def main():
    config = read_config()
    git_init(config)
    file_init()
    word_array = characters.get_word_array(config['word'], config['weeksBefore'])
    for i in range(0, len(word_array)):
        for j in range(0, len(word_array[i])):
            if word_array[i][j] == True:
                print('*', end = "")
            else:
                print(' ', end = "")
        print()
    create_commites(word_array)
    
def read_config():
    config_file = open("config.json")
    config = json.load(config_file)
    word = config['word'].strip().upper()
    print(word)
    if len(config['word']) > 7:
        raise ValueError("Word cannot longer than 7 characters.")
    config['word'] = word
    return config

def git_init(config):
    os.system("git config user.name " + config['username'])
    os.system("git config user.email " + config['email'])
    os.system("git checkout --orphan new_brance")
    os.system("git add .")
    os.system("git commit -m \"init\"")
    os.system("git branch -D main")
    os.system("git branch -m main")

def create_commites(word_array):
    now_weekday = datetime.datetime.now().weekday()
    if now_weekday == 6:
        days_before = 1
    elif now_weekday == 5:
        days_before = 0
    else:
        days_before = now_weekday + 2

    for i in reversed(range(len(word_array[0]))):
        for j in reversed(range(7)):
            if word_array[j][i] == True:
                create_git_commit(days_before)
                create_git_commit(days_before)
            days_before += 1

def create_git_commit(days_before):
    file_change()
    os.system("git add .")
    os.system("git commit --date \"" + str(days_before) + " days ago\" -m \"https://github.com/s4ng/jandi\"")

def file_change():
    new_text = ''
    with open('change.txt', 'r') as f:
        lines = f.readlines()
        line = lines[0].strip()
        new_text += line + '1'
    with open('change.txt', 'w') as f:
        f.write(new_text)

def file_init():
    with open('change.txt', 'w') as f:
        f.write("1")

if __name__ == "__main__":
    main()
