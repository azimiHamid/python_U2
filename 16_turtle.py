from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red")
timmy.forward(450)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column("city_name", ["Kabul", "Mazar", "Bamyan", "Ghazni", "Herat"])
# table.add_column("population", ["7M", "3M", "2.5M", "3.5M", "4M"])
# table.align = "l"
# print(table)