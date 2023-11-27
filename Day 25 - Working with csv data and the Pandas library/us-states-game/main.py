import turtle
import pandas

TOTAL_STATES = 50
score = 0

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

df = pandas.read_csv("50_states.csv")

correct_states = []

while score < TOTAL_STATES:
    if score == 0:
        answer_state = screen.textinput(
            title="Guess the state", prompt="What's another state's name?").title()
    else:
        answer_state = screen.textinput(
            title=f"{score}/{TOTAL_STATES} States Correct", prompt="What's another state's name?").title()

    if answer_state == 'Exit':
        states_to_learn = list(set(df.state.tolist()) - set(correct_states))
        # Create a DataFrame from the list
        states_csv_df = pandas.DataFrame({'State': states_to_learn})
        # Save the DataFrame to a CSV file
        states_csv_df.to_csv('states_to_learn.csv', index=False)

        break
    elif answer_state not in correct_states:
        state_df = df[df.state == answer_state]

        if not state_df.empty:
            timmy = turtle.Turtle()
            timmy.penup()
            timmy.hideturtle()
            timmy.goto(int(state_df.x.iloc[0]), int(state_df.y.iloc[0]))
            timmy.write(f"{answer_state}", align="center",
                        font=("Courier", 10, "normal"))
            score += 1
            correct_states.append(answer_state)
