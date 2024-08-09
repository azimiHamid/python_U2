import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "./utils_25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("./utils_25/50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", 
                                    prompt="What's another state's name? ").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("./utils_25/states_to_learn.csv", index=False)
        break
    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        # t.write(answer_state)     # OR: t.write(state_data.state.item())
        t.write(state_data.state.item())
    else:
        t = turtle.Turtle()
        t.color("red")
        t.hideturtle()
        t.write("OOPS! The state name you provided doesn't exist.", 
                align="center", 
                font=("Arial", 20, "bold"))
        screen.exitonclick()

# States to learn.csv


# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop() #keep our screen open
