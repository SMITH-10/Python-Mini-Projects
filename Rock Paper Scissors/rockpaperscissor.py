import random
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
start=input("ARE YOU READY TO PLAY ROCk, PAPER , SCISSORS? (Y/N):")

if start == "Y":
    print("""Winning Possiblity:
          1. Rock win against Scissors 
          2. Paper win against Rock  
          3. Scissors win against Paper 
          4. Same Choice gives a Tie""")
    
def play():
    print("Press 1 for rock\nPress 2 for paper\nPress 3 for scissors")
    choice=int(input("Enter your choice:"))
    ab=[1,2,3]
    compchoice=random.choice(ab)
    if compchoice==choice:
        print("Tie")
        engine.setProperty('voice', voices[1].id)
        engine.say("It's a Tie")
        engine.runAndWait()

    elif compchoice==1 and choice==2:
        print("""Computer Choose Rock and You choose Paper
                 You Win""") 
        engine.setProperty('voice', voices[1].id)
        engine.say("You Win")
        engine.runAndWait()
        
    elif compchoice==1 and choice==3:
        print("""Computer Choose Rock and You choose Scissors
                You Lose""")
        engine.setProperty('voice', voices[1].id)
        engine.say("You Lose")
        engine.runAndWait()   
        
    elif compchoice==2 and choice==1:
        print("""Computer Choose Paper and You choose Rock
                You Lose""")
        engine.setProperty('voice', voices[1].id)
        engine.say("You Lose")
        engine.runAndWait()   
        
    elif compchoice==2 and choice==3:
        print("""Computer Choose Paper and You choose Scissors
                You Win""")
        engine.setProperty('voice', voices[1].id)
        engine.say("You Win")
        engine.runAndWait()
        
    elif compchoice==3 and choice==1:
        print("""Computer Choose Scissors and You choose Rock
                You Win""")
        engine.setProperty('voice', voices[1].id)
        engine.say("You Win")
        engine.runAndWait()

    elif compchoice==3 and choice==2:
        print("""Computer Choose Scissors and You choose Paper
                You Lose""")
        engine.setProperty('voice', voices[1].id)
        engine.say("You Lose")
        engine.runAndWait()   

play()
         


    


    






