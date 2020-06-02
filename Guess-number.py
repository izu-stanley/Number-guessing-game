"""
Number guessing game written by Uchegbu Somtochukwu on June 2nd 2020

"""

import random


def mini_game():
    print('This is a game where you will have to guess a random number generated by the computer\n'
          'The random number will be in range of 1 to 30\n'
          'For every wrong guess you get a hint of the number you did not guess rightly\n'
          'At the end if you get the number correctly the game ends\n'
          'When you feel you are tired of playing, to exit the game input 1234\n'
          'If you wish to restart there is option for you')
    while True:
        number = int(input('Enter your number: '))
        random_number = random.randint(0, 30)

        if number in range(0, 30):
            def random_guess_even():
                if random_number % 2 == 0:
                    value = random_number - number
                    if value in range(0, 10):
                        print('wrong guess,  random number within the range of numbers 1 and 10')
                    elif value in range(10, 20):
                        print('wrong guess,  random number the random number is even and in range of numbers 11 and 20')
                    elif value in range(20, 30):
                        print('wrong guess,  random number the number is even and in range of numbers 21 to 30')

            def random_guess_odd():
                if random_number % 2 == 1:
                    value = random_number - number
                    if value in range(0, 10):
                        print('Wrong guess. Hint: random number is an odd within the range of numbers 1 and 10')
                    elif value in range(10, 20):
                        print('Wrong guess. Hint: random number is odd and within the range of numbers 11 and 20')
                    elif value in range(20, 30):
                        print('Wrong number. Hint: random number is within the range of  numbers 21 and 30')

            def negative_number():
                value = random_number - number
                if value in range(-100, 1):
                    print('Not correct')

            negative_number()
            random_guess_even()
            random_guess_odd()

        elif number == 1234:
            print('Thank you for your time')
            quit()
        elif number not in range(0, 30):
            print('Not in range of random numbers to be generated')
        else:
            print('Correct guess')
            retry = input('Enter yes to retry enter no to abort program')
            if retry == 'yes':
                True
            elif retry == 'no':
                print('Thank you for your time')
                quit()
            else:
                print('Invalid input')
                True


mini_game()
