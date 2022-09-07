import random
score_player = 0
score_computer = 0
life = 3
fim = False


def reset_var():
    global life
    life = 3
    return life


def print_life_player(life):
    msg = f'You have {life} lives'
    return print(msg)


def print_life_computer(life):
    msg = f'Computer have {life} lives'
    return print(msg)


def guess(x):
    global score_player
    global life
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number and life > 0:
        life -= 1
        guess = int(input(f'Guess a number between 1 and {x}: '))

        if guess < random_number:
            print('Sorry , guess again.Too low.')
            print_life_player(life)
        elif guess > random_number:
            print('Sorry , guess again.Too high.')
            print_life_player(life)
        elif guess == random_number:
            print(
                f'Yay , congrats. You have guessed the number {random_number}')
            score_player = score_player + 1
            return score_player

        if life == 0:
            print("Gamer Over!")


def computer_guess(x):
    global score_computer
    global life
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and life > 0:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f'Is {guess} too high(H) , too low (L) or too Correct (c): ').lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

        elif feedback == 'c':
            print(
                f'Congrats!!The Computer guessed your number: {guess},Correctly ')
            score_computer += 1
            return score_computer
        else:
            print('Sorry,Value invalid feedback')
        if life == 0:
            print("Gamer Over!")

        life = life - 1
        print_life_computer(life)


while fim == False:
    print()
    print('Score')
    print(f'PLayer:{score_player} , Computer:{score_computer}')
    print()
    print('who will guess?')
    print('1-You')
    print('2-Computer')
    print('3-Exit')
    resp = int(input())

    if resp == 1:
        numbers = int(
            input('Choose the maximum amount of numbers you want to play: '))
        guess(numbers)
        reset_var()
    elif resp == 2:
        numbers = int(
            input('Choose the maximum amount of numbers you want to play: '))
        computer_guess(numbers)
        reset_var()
    elif resp == 3:
        print('Bye!Thanks')
        fim = True
