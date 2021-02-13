import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

t = turtle.Turtle()
t.penup()
t.hideturtle()

states_df = pd.read_csv("50_states.csv")

states_df.state = states_df.state.str.lower()

states_list = states_df.state.to_list()

correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"Guess the States {len(correct_guesses)}/{len(states_list)}", prompt="What's another state's name?")
    if answer_state is None:
        break

    else:
        answer_state = answer_state.lower()

        if answer_state in states_list:
            t.goto(int(states_df[states_df.state == answer_state].x), int(states_df[states_df.state == answer_state].y))
            t.write(f"{answer_state.title()}", align="center", font=("Arial", 6, "bold"))
            correct_guesses.append(answer_state)

missed_states = [state.title() for state in states_list if state not in correct_guesses]

print("Here are the state's you missed:")
print(missed_states)


screen.exitonclick()
