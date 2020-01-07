import random
try_to_guess = random.randint(1,50)
while True:
    try:
        myGuess = int(input("Your first guess (enter an integer): "))
    except:
        print("You entered string. Try again.")
        continue
    break
a, b = 0, 51
guessed = False
i = 0
while guessed is False and i != 7:
    if myGuess == try_to_guess:
        print(f'You win. The guessed number was {try_to_guess}')
        guessed = True
    elif myGuess > try_to_guess:
        print('Your guess is less then GN')
        i += 1
        b = myGuess
        myGuess = (a+b)//2
    else:
        print('Your guess is more then GN')
        i += 1
        a = myGuess
        myGuess = (a+b)//2
if i > 6:
    print(f'You losse. The guessed number was {try_to_guess}')