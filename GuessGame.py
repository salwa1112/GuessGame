import random
while True:
    print("Guess a number between 1 and 10, Enter 0 to quit the game at any time")
    # generate random int between 1 to 10
    guess = random.randint(1, 10)
    UserInput = int(input('Enter your guess: '))
    if UserInput == 0:
        break
    while (UserInput != guess):
        if UserInput < guess and UserInput != 0:
            print('Your guess is very low!!')
        elif UserInput > guess and UserInput != 0:
            print('Your guess is very high!!')
        UserInput = int(input('Want to try again? Enter your new guess: '))
        if UserInput == 0:
            break
    if UserInput == guess:
        print('You guess the correct number!!')
    answer = input("Do you want to continue or exit, Y for continue, N for exit? (Y/N): ")
    if answer.upper() == "Y":
        continue
    else:
        break
