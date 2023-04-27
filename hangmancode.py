import random
with open('words.txt') as f:
    words=f.read()
    words=words.split( )
    secret_word=random.choice(words)
length_word=len(secret_word)
print('Word list is being loaded from file...\n55900 words are loaded.\nGet Ready!! Welcome to the game Hangman!')
import Hangman

Hangman.hangman(secret_word)
