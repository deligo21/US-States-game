import turtle
import pandas
from states_written import States_Written

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(725,491)
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 0
data = pandas.read_csv("./50_states.csv")
correct_guesses = []

while score <= 50:
    answer_state = screen.textinput(f"{score}/50", "What's another state's name?").title()
    
    if answer_state == "Exit":
        missing_states = [state for state in list(data.state) if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learns.csv")
        break
    
    if answer_state in list(data.state):
        correct_guesses.append(answer_state)
        state_correct = data[data.state == answer_state]
        score += 1
        state_w = States_Written(answer_state, int(state_correct.x), int(state_correct.y))
        