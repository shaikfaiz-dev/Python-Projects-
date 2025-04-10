print("Welcome to the Quiz game :) ")
print("You will be asking 10 Que's >-- After the completion of your game you'll get your score based on your performence ")
playing = input("Do you want to play:? ")
if playing.lower() !="yes":
    quit()
else:
    print("Hurray Lets play ^_^ ")   
    
     
score = 0    
answer = input("Q: What Deos CPU stands for? (Ans): ")    
if answer.lower() == "central processing unit":
    print("Yes, Correct!!")
    score += 1
else:
    print("Incorrect !!")
    
answer = input("Q: What is the full form of RAM? (Ans): ")    
if answer.lower() == "random access memory":
    print("Yes, Correct!!")
    score += 1
else:
    print("Incorrect !!")  
    
answer = input("Q: What type of device is a keyboard? (Ans): ")    
if answer.lower() == "input device":
    print("Yes, Correct!!")
    score += 1
else:
    print("Incorrect !!")  
    
answer = input("Q: Who is the brain of the computer? (Ans): ")    
if answer.lower() == "cpu":
    print("Yes, Correct!!")
    score += 1
else:
    print("Incorrect !!")  

answer = input("Q: What does URL stand for? (Ans): ")    
if answer.lower() == "uniform resource locater":
    print("Yes, Correct!!")
    score += 1
else:
    print("Incorrect !!")  
 
answer = input("Q: What does HTML stand for? (Ans): ")    
if answer.lower() == "hyper text markup language":
    print("Yes, Correct!!")
    score += 1
else:
    print("Incorrect !!")  
    
answer = input("Q: What Deos CSS standas for? (Ans): ")    
if answer.lower() == "cascading style sheets":
    print("Yes, Correct!!")
    score += 1
else:
    print("Incorrect !!")  
 
answer = input("Q: What does AI stands for? (Ans): ")    
if answer.lower() == "artificial intelligence":
    print("Yes, Correct!!")
    score += 1
else:
    print("Incorrect !!")  
    
answer = input("Which technology has been evolved in tech industry most in between 2 years? (Ans): ")    
if answer.lower() == "artificial intelligence":
    print("Yes, Correct!!")
    score += 1
else:
    print("Incorrect !!")      
    
    
print(f"You have given {score} answer's correct so your percentage is {(score/9)*100:.2f}%")
print(f"You have given {score} ^o^ Answer's correct among the 9 so your score is ^-^  {score}")
            