# from turtle import * # bad way ⛔

# import turtle as t  # use Alias when a module have a large name.
# terry = t.Turtle()

# import turtle
# timmy = turtle.Turtle()    # so boring to write many times : turtle.Turtle(). better approach is using from...import... syntax as bellow.

import random
from turtle import Turtle, Screen
tim = Turtle()
tim.pensize(3)
tim.pencolor("coral")

# tim.shape('turtle')
# tim.color("red")
# tim.forward(100)
# tim.right(90)
# tim.forward(100)



# challenge #1: Draw a square using turtle?
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)


# We also have some modules that should be installed first, then imported
# import heroes
# hero_arr = heroes.genarr(10)
# for hero in hero_arr:
#     print(hero)



# challenge #2: Draw dashed line square?
# def draw_dashed_line(length):
# def draw_dashed_line(length):
#     dash_length = 10
#     gap_length = 5
#     while length > 0:
#         tim.forward(dash_length)
#         tim.penup()
#         tim.forward(gap_length)
#         tim.pendown()
#         length -= (dash_length + gap_length)

# for _ in range(4):
#     draw_dashed_line(200)
#     tim.right(90)




# challenge #3: Draw different shapes?
# colors = ['red','green','blue','indianred','firebrick','ForestGreen']
# def draw_shape(number_of_sides):
#     angle = 360 / number_of_sides
#     for _ in range(number_of_sides):
#         tim.forward(100)
#         tim.right(angle)

# for number_of_sides in range(3, 11):
#     draw_shape(number_of_sides)
#     tim.color(random.choice(colors))




# challenge #4: Draw random walk?
colors = [
    'red', 'green', 'blue', 'indianred', 'firebrick', 'ForestGreen',
    'gold', 'darkorange', 'purple', 'deeppink', 'lightseagreen',
    'mediumslateblue', 'turquoise', 'darkviolet', 'hotpink', 'lightsalmon',
    'darkturquoise', 'navy', 'coral', 'chocolate', 'darkmagenta',
    'lightcoral', 'sienna', 'yellowgreen', 'crimson', 'mediumaquamarine'
]

directions = [0, 90, 180, 270]

tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))

tim.hideturtle()




screen = Screen()
screen.exitonclick()