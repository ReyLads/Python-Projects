import random

print("Hi! Welcome to the number guessing game!\n"
      "You have 10 tries to guess the number.\n"
      "I'll tell you if you're too high or too low.\n"
      "Let's begin!")

number_to_guess = random.randrange(1,100)

attempt_limit = 10
attempt_counter = 0

while attempt_counter < attempt_limit:
    attempt_counter += 1
    player_guess = int(input("Enter your guess: "))

    if player_guess == number_to_guess:
        print(f"You guessed it! The number was {number_to_guess}")
        break

    elif attempt_counter >= attempt_limit and player_guess != number_to_guess:
        print(f"Sorry, you didn't guess the number and you've used all your attempt limit. The number was {number_to_guess}.")

    elif player_guess < number_to_guess:
        print("Too low!")

    elif player_guess > number_to_guess:
        print("Too high!")
