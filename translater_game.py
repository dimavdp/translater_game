from __future__ import print_function, unicode_literals
import os
import time

from random import shuffle
from pyfiglet import Figlet
from colorama import init, Fore, Back, Style
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError

f = Figlet(font='slant')
init(autoreset = True)
print (Fore.GREEN + Back.BLACK + Style.BRIGHT + f.renderText('eng | jap') + '\n@dimavdp / @XinDV\n')
correct_answers = 0
incorrect_answers = 0

def clear():
    os.system('clear')

def exit():
    os._exit(0)

'''
COLORAMA COLORS

Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''

dictionary = {}
with open('japanese_library.txt') as fileobj:
    for line in fileobj:
        key, value = line.split(':')
        dictionary[key] = value

guess_dict = list(dictionary.items())
shuffle(guess_dict)


style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})

class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end

print("Hi. It's a simple game: I'll give you a word in English, and you'll translate it in Japanese character sets like: 'Hello' -> 'Konnichiwa'. You can answer as long, as you want, but after your guess you have 3 seconds to read right answer if you were wrong and be ready for next word. Your results will be displayed in the end. To start the quiz, you have to answer a few questions. Good luck!\n")

questions = [
    {
        'type': 'input',
        'name': 'HowManyWords',
        'message': 'How many words do you want to guess?',
        'validate': NumberValidator,
        'filter': lambda val: int(val)
    },
    {
        'type': 'confirm',
        'name': 'ReadyToStart',
        'message': 'Are you ready to start?',
        'default': False
    }
]

answers = prompt(questions)
print('\n')
#pprint(answers)

if answers['ReadyToStart'] == True:
    number_of_questions = answers['HowManyWords']
    start = time.time()
    for i in range(number_of_questions):
        question = guess_dict.pop(0)
        print("English: ", question[0])
        answer = input("Japanese:  ")
        if answer == question[1]:
            print(Fore.GREEN + 'correct!\n')
            correct_answers += 1
            time.sleep(3)
        else:
            print(Fore.RED + 'false! right answer is: ', question[1], '\n')
            incorrect_answers += 1
            time.sleep(3)
        clear() # the shell
else:
    exit()

print(Fore.GREEN + Back.BLACK + Style.BRIGHT + 'Your results')
print('\n----------------------------------------------------')
print("It took", Fore.GREEN + str((time.time() - start) - number_of_questions * 3), "seconds for you to answer.")
print('Correct answers: ', Fore.GREEN + str(correct_answers),
      '\nIncorrect answers: ', Fore.RED + str(incorrect_answers))
print('----------------------------------------------------\n\n')

'''
\\\\\\\\\\\\\\\\\\\\
TO DO:
1)add_word()
2)delete_word

print(dictionary)

def add_word():
    eng_word = input('word in english: ')
    jap_word = input('word in japanese: ')
    dictionary[eng_word] = jap_word
    with open('japanese_library', 'w') as fileobj:
        for key, value in dictionary.items():
            fileobj.write('%s:%s\n' % (key, value))
    fileobj.close()

def delete_word():
    eng_word = input('word to delete in english: ')
    dictionary.pop(eng_word)

add_word()
'''