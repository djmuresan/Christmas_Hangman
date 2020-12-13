import random

print("This is a holiday-themed hangman. Try to find the word based of the difficulty you choose")

words = ['bells', 'cards', 'hymns', 'elves', 'grace', 'merry', 'feast', 'aroma', 'green', 'jesus', 'faith']
easy_words = ['elf', 'cap', 'eat', 'ask', 'eve', 'pew', 'bow', 'ate', 'box', 'awe', 'fig', 'nap', 'lap', 'fly', 'tag', 'fir', 'ice']
hard_words = ['festive', 'antlers', 'believe', 'goodies', 'angelic', 'blitzen', 'snowman', 'cookies', 'mittens', 'rituals', 'candles', 'rudolph', 'scarves', 'present']

clue = list('?????')
clue_easy = list('???')
clue_hard = list('???????')

diffculty = input('Choose difficulty type (type 1, 2, or 3)\n 1 Easy\n 2 Normal\n 3 Hard\n : ')
diffculty = int(diffculty)

if diffculty == 1:
    lives = 7
    clue = clue_easy
    words = easy_words
elif diffculty == 2:
    lives = 6
else:
    lives = 5
    clue = clue_hard
    words = hard_words

scrt_wrd = random.choice(words)
hrt = u'\u2764'
gssd_wrd_crrctly = False
count = 0

def update_clue(gssd_lttr, scrt_wrd, clue):
    global count
    index = 0
    while index < len(scrt_wrd):
        if gssd_lttr == scrt_wrd[index]:
            clue[index] = gssd_lttr
            count += 1
        index += 1

while lives > 0:
    print(clue)
    print('Lives left:  ' + hrt * lives)
    guess = input('Guess a letter in this word or the whole word:  ')

    if guess == scrt_wrd:
        gssd_wrd_crrctly = True
        break

    if guess in scrt_wrd:
        update_clue(guess, scrt_wrd, clue)
        print('That is a letter here, good job.')
        if count == len(scrt_wrd):
            gssd_wrd_crrctly = True
            break
    else:
        print('Incorrect, You lose a life. Try Again!  ')
        lives -= 1

if gssd_wrd_crrctly is True:
    print(f"Merry Christmas, You Won! the word was '{scrt_wrd}'.")
else:
    print('Bummer, You Lost! the word was ' + scrt_wrd)
