import random


def print_life(life):
    msg = f'You have {life} lives'
    return print(msg)


def guess(x):
    life = 2
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number and life > 0:
        life -= 1
        guess = int(input(f'Guess a number between 1 and {x}: '))

        if guess < random_number:
            print('Sorry , guess again.Too low.')
            print_life(life)
        elif guess > random_number:
            print('Sorry , guess again.Too high.')
            print_life(life)
        elif guess == random_number:
            print(
                f'Yay , congrats. You have guessed the number {random_number}')
        if life == 0:
            print("Gamer Over!")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f'Is {guess} too hight(H) , too low (L) or too Correct (c)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(
                f'Congrats!!The Computer guessed your number: {guess},Correctly ')
        else:
            print('Sorry,Value invalid feedback')


numbers = int(input('Choose the maximum amount of numbers you want to play: '))
# guess(numbers)
computer_guess(numbers)
