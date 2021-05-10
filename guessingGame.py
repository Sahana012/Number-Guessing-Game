import random
chances = 0
number = random.randint(1, 9)

while chances < 5:
    guess = int(input("Enter your guess: "))
    
    if number == guess:
        print("You won!")
        break
        
    else:
        print("Nope! Try again!")
        
    chances = chances + 1
    
if not chances < 5:
    print("YOU LOSE!! The number is ", number)
