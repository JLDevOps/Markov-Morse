import re
import time

import pygame

from markov_chain import *

CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
        }

ONE_UNIT = 0.5
THREE_UNITS = 3 * ONE_UNIT
SEVEN_UNITS = 7 * ONE_UNIT
PATH = 'morse_sound_files/'


def verify(string):
    keys = CODE.keys()
    for char in string:
        if char.upper() not in keys and char != ' ':
            sys.exit('Error the character ' + char + ' cannot be translated to Morse Code')


def generate_morse_code(sentence_list):
    pygame.init()
    for i in range(len(sentence_list)):
        sentence = str(sentence_list[i])
        new_string = re.sub('[!@#$.,-;<>"/`~\']', '', sentence)
        verify(new_string)
        if new_string is not None:
            print new_string
            for char in new_string:
                if char == ' ':
                    print ' ' * 7,
                    time.sleep(SEVEN_UNITS)
                else:
                    print CODE[char.upper()],
                    pygame.mixer.music.load(PATH + char.upper() + '_morse_code.ogg')
                    pygame.mixer.music.play()
                    time.sleep(THREE_UNITS)


def generate_markov_morse(filename, file_format, num_of_sentences):
    list = generate_markov_text(filename, file_format, num_of_sentences)
    generate_morse_code(list)


def input_prompt():
    print 'Welcome to Alphabet to Morse Code Translator v.01\n'
    msg = raw_input('Enter Message: ')
    verify(msg)
    pygame.init()
    for char in msg:
        if char == ' ':
            print ' ' * 7,
            time.sleep(SEVEN_UNITS)
        else:
            print CODE[char.upper()],
            pygame.mixer.music.load(PATH + char.upper() + '_morse_code.ogg')
            pygame.mixer.music.play()
            time.sleep(THREE_UNITS)

## For testing purposes
if __name__ == "__main__":
    generate_markov_morse("sherlock", "txt", 1)
