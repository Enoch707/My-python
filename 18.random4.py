#lets make a number guessing game together
import random
secret_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")
attempts = 0
guess = 0
while guess != secret_number:
    #note != means not equal to
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
else :
    print (f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")