import random

def generate_code():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]
def guessing():
    return list(input('Guess a 3 digit number'))
def match(code,guess):
    clues=[]
    if code == guess:
        return 'CODE CRACKED!'
    for ind,num in enumerate(guess):
        if num == code[ind]:
            clues.append('Match!')
        elif num in code:
            clues.append('Close!')
    if clues==[]:
        return ['Nope!']
    else:
        return clues
secret=generate_code()
report=[]
while report != 'CODE CRACKED!':
    guess=guessing()
    report=match(guess, secret)
    for clue in report:
        print(clue)
