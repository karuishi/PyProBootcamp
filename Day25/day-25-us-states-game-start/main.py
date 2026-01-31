import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape((image))

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
guessed_states = []    
    
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    
    if answer_state in states_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(state_data["x"].item(), state_data["y"].item()) # Recupera apenas o primeiro elemento (e não o índice + primeiro elemento)
        t.write(state_data["state"].item())

