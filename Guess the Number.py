# An interactive game where users have to guess the number

# IMPORT
import random

# PRINT STATEMENT TO DISPLAY A WELCOME MESSAGE TO USER
print("WELCOME TO GUESS THE NUMBER")

secret_number = random.randint(1,100)
attempts = 0

# USING WHILE LOOPS TO MAKE THE GAME CONTINUE UNTIL USER CAN GUESS THE RIGHT NUMBER
while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
# IF OR ELIF STATEMENTS TO EXPLAIN THAT IF THE USER GUESSES THE CORRECT NUMBER THAN A CONGRATULATIONS MESSAGE WILL DISPLAY
        # IF USER GUESS IS TOO LOW OR TOO HIGH IT WILL LET THE USER KNOW
        # IF THE USER INPUTS ANYTHING BESIDES A NUMBER, THAN USER WILL SEE AN ERROR MESSAGE DISPLAY
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} tries!.")
            break
        elif guess < secret_number:
            print(f"Your guess is too low.")
        else:
            print(f"Your guess is too high.")

    except ValueError:
        print("Sorry, I didn't understand that.")
