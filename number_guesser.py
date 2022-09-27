# importing module random
import random

# Declaring variable topRange and setting it to the input of the user + 1 so the user input is correct
topRange = int(input("Welche soll die letztmögliche Ziffer sein?: "))
# Declaring the variable number and setting it to the randint function from the random module
number = random.randint(1, topRange + 1)

# Determining if the number was guessed correctly, too high or to low

running = True
while running:
    guess = int(input("Rate eine Zahl: "))

    if guess == number:
        print(f"\nDu hast es erraten! Die gesuchte Zahl war {number}")
        break
    elif guess < number:
        print("Zu niedrig!")
    else:
        print("Zu hoch!")