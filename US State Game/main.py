import turtle 
import pandas as pd
import csv

screen=turtle.Screen()
screen.title("U.S. State Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pd.read_csv("50_states.csv")
all_states=data.state.to_list()
guesses_states=[]
while len(guesses_states)<50:
    answer_state=screen.textinput(title=f"{len(guesses_states)}/50 States Correct",prompt="What's another state's name? ").title()

    if answer_state=="Exit":
        missing_states=[state for state in all_states if state not in guesses_states]
        miss=pd.DataFrame(missing_states)
        miss.to_csv("states_to_learn.csv")
                
        break
    if answer_state in all_states:
        guesses_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
        
