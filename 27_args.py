# <------------------------ *args ==> All the arguments ------------------------>
# *args: It takes all the arguments and put them inside a tuple.

def add(*args):
    #? print(args)
    #? print(args[3])
    sum = 0
    for n in args:
        sum += n
    return sum
    
print(add(3, 5, 7, 4, 6, 9))


# <------------------- **kwargs ==> Unlimited keyword arguments ---------------->
# **kwargs: It takes all the arguments in key-value pair format and put them inside a dictionary.

def calculat(**kwargs):
    #? print(kwargs)
    for key, value in kwargs.items():
        print(key, value)

#? calculate(add=3, multiply=4)


def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key, value)
    
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(2, add=3, multiply=4)



class Car:
    def __init__(self, **kwargs) -> None:
        self.make = kwargs['make']
        self.model = kwargs.get('model') # Using get is better, because it doesn't crash the program.
        self.color = kwargs.get('color')


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.color)
