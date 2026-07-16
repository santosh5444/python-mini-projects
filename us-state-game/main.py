from turtle import Turtle,Screen
import pandas as pd

screen=Screen()
turtle=Turtle()
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data=pd.read_csv("50_states.csv")

states_data=data["state"].to_list()
guessed_states=[]

while len(guessed_states)<50:

    user_guess=screen.textinput(title=(f"{len(guessed_states)}/50 guessed correct") ,prompt="whats the states name?").title()
    if user_guess=="Exit":
        missing_states=[elements for elements in states_data if elements not in guessed_states]
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv("need to learn that u missed .csv")
        break

    elif user_guess in states_data:
        new_pen=Turtle()
        new_pen.penup()
        new_pen.hideturtle()
        state_data=data[data.state==user_guess]
        new_pen.goto(state_data.x.item(),state_data.y.item())
        new_pen.write(user_guess)
        guessed_states.append(user_guess)
screen.exitonclick()