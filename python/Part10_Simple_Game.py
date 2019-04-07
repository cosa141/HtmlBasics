import random

def generate_code():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:3]

playing=True
def guessing():
    return list(input('Guess a 3 digit number'))

def match(code,guess):
    clues=[]
    if code == guess:
        return 'code CRACKED!'
        playing = False
    for ind,num in enumerate(guess):
        if num == code[ind]:
            clues.append('Match!')
        elif num in code:
            clues.append('Close!')
    if clues==[]:
        return 'Nope!'
    else:
        return clues

while playing==True:
    guess=guessing()
    report=match(digits, guess)
    for clue in report:
        print(clue)












































# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
