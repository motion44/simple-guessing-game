import random

number = random.randint(1, 10)

attempt = input("I'll pick a random number (1–10), try guessing it! ")
attempt = int(attempt)

if attempt == number:
    print("Correct!")
else:
    if attempt > number:
        print("Too high")
    else:
        print("Too low")
        
if attempt > 10:
    print("You need to pick a number between 1 and 10")
    
if attempt < 1:
    print("You need to pick a number between 1 and 10")
    
    guess2 = input("You have 2 more guesses: ")
    guess2 = int(guess2)

  # This is your second last guess.
    if guess2 == number:
        print("Correct!")
    else:
        if guess2 > number:
            print("Too high")
        else:
            print("Too low")
          
  # This is your last guess.
        guess3 = input("You have 1 more guess: ")
        guess3 = int(guess3)

        if guess3 == number:
            print("Correct!")
        else:
            print("You have run out of guesses!")
            print(f"The number was {number}")
