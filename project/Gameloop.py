import random
import time

print("Hi, Welcome to the guessing game. I am going to pick a number between 1 and 100.")
time.sleep(3)
print("Picking a number...")
time.sleep(2)
guess = int(input("What is your guess?: "))
correct_number = random.randint(1,100)
guess_count = 1

while guess != correct_number:    #runs until condition is true when you're under how many times it'll loop
   # time.sleep(1)
    guess_count += 1
    if guess < correct_number:
        guess = int(input("Wrong. You need to guess higher.  What's you're guess?: "))
    else:
        guess = int(input("Wrong. You need to guess lower.  What's you're guess?: "))


print(f'Congrats! The right answer is {correct_number}. It took you {guess_count} guesses.')