# class without a constructor: it takes more time to assign every attributes of an object a value, So it's better to use constructor.
# class User:
#     pass


# # 1st user
# user_1 = User()
# user_1.id = "001"
# user_1.username = "hamid123"

# print(user_1.id)

# # 2nd user
# user_2 = User()
# user_2.id = "002"
# user_2.username = "sarah007"

# print(user_2.id)

# # 3rd user .... nth user ....
# user_3 = User()
# user_3.id = "003"
# user_3.name = "Ahmad52" # instead of username --> name

# print(user_3.name)



# class with constructor
# self is the object itself which is constructed by the constructor. for e.g. 
# user_1 = User()  ---> here user_1 is the object which is refered to self.
# user_2 = User()  ---> here user_2 is the object which is refered to self.
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # This is a default assigned attribute, noneed to required it while construction of an object, it attached to all the objects of thus class
        

user_1 = User("001", "hamid123")  # see, here we did all the previous attempts in class without constructor examples just in 1 line
print(user_1.id)
print(user_1.username)

user_2 = User("002", "sarah007")
print(user_2.id)
print(user_2.username)