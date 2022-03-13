import random
print ("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Guess a number [between 1 and 9] ")

while chances < 5:
    guess = int(input("Enter your Guess: "))

    if guess == number:
        print("Congrats!!!! YOU WON")
        break

    elif guess < number:
        print("Your guess was too low, guess higher than", guess)

    else:
        print("Your guess was too high, guess lower than", guess)

    chances += 1

if not chances < 5:
    print("YOU LOOSE!!! The number is: ", number)
