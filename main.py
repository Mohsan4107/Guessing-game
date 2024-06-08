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
    
    print(f'Congratulations ! You have guess the correct number: {random_num}')