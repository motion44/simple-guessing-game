import random

guesses = 3

number = random.randint(1, 10)

while True:
    try:
        attempt = int(input("I'll pick a random number (1-10), try guessing it: "))
    
    except ValueError:
        print("Error.")

    else:
        if attempt == number:
            print("Correct.")
            break
        elif attempt != number:
            if attempt > 10 or attempt < 0:
                print("Please pick a valid number")
            else:
                if attempt > number:
                    print("Too high.")
                else:
                    print("Too low.")
                guesses -= 1
                print(f"You have {guesses} guesses left.")
                if guesses == 0:
                    print("You have run out of guesses.")
                    break
    finally:
        print("Attempt finished.")
