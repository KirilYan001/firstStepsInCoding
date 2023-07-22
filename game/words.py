import random

WORDS = ('kiko', 'indecifrabile', 'facilmente', 'chiamata', 'miserabie', 'lacerata')
MAX_GUESSES = 4
RESPONSE_CONDITION = False

print('Wellcome')
print('you have to be smart to play this game')
print()

word = random.choice(WORDS)
scrambled_words = ''.join(random.sample(word, len(word)))

for guess in range(MAX_GUESSES):
    print('scrambled_words:',scrambled_words)
    answer = input('Enter your guess: ')

    if answer == word:
        print('Nice you are not dumb')
        RESPONSE_CONDITION = True
        break
    else:
        print("YOU ARE DUMB!")

if not RESPONSE_CONDITION:
    print('YOU ARE SO DUMB MAN LEARN ITALIAN,This is the word Dumb monkey', word)
