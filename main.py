import random

def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_num:
            print('Sorry, number too low. Guess again.')
        elif guess > random_num:
            print('Sorry, number too high. Guess again')
    
    print(f'Congratulations ! You have guessed the correct number: {random_num}')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'The computer guessed the number: {guess} correctly!')

guess(8)
computer_guess(22)   