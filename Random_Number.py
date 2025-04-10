import random

user = input("Enter a number: ")

if user.isdigit():
    user = int(user)
    if user <= 0:
        print("Enter a number Greater than 0")
        quit()
else:
     print("Enter a number next time") 
     quit()
        
random_number = random.randint(0, user)   
guess = 0

while True:
    guess += 1
    user_guesses = input("Its your turn to make a guess: ")
    if user_guesses.isdigit():
        user_guesses = int(user_guesses)
    else:
        print("Enter a number next time")
        continue
    
    if user_guesses > random_number:
        print("You are Guessing Greater number, Think SomeWhat low: ")   
        
    elif user_guesses < random_number:
        print("You are Guessing Lesser number, Think someWhat High: ")
        
    elif user_guesses == random_number:
        print("You're absolutely right!!!")
        break   
    else:
        print("Oops, that's incorrect. !!")    
    
print(f" Hurray You Got it !! after {guess} Guesses")    