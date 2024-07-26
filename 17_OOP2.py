class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "hamid123")
user_2 = User("002", "sarah007")
user_3 = User("003", "Ahmad04")

user_1.follow(user_2)   # user_1 is following user_2
user_3.follow(user_2)   # user_3 is following user_2
user_2.follow(user_2)   # user_2 is following herself(sarah)
print(f"user_2's followers: {user_2.followers}")
print(f"user_2 is following: {user_2.following} people(herself)")
