import random

# Get the upper range for the random number
top_of_range = input("Enter the upper limit for the random number: ")
if top_of_range.isdigit() and int(top_of_range) > 0:
    top_of_range = int(top_of_range)
else:
    print("Please enter a valid positive number next time.")
    quit()

# Initialize variables
guess_count = 0
random_number = random.randint(0, top_of_range)

# Start the guessing game
while True:
    guess_count += 1
    guess_num = input(f"Enter your guess (attempt #{guess_count}): ")
    
    if guess_num.isdigit():
        guess_num = int(guess_num)
    else:
        print("Invalid input. Please enter a number.")
        continue

    if guess_num == random_number:
        print("Congratulations! You guessed it right!")
        break
    elif guess_num < random_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

# Display the result
print(f"You guessed the number in {guess_count} attempts!")
