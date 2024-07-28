from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)
    
    
def move_backwards():
    tim.backward(10)
    
    
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    

def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
# screen.onkey(key='space', fun=move_forwards)
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
