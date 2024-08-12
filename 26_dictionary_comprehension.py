# Dictionary Comprehension
    # 1. Creating dictionary from a list
        # new_dict = {new_key:new_value for item in list}
        
    # 2. Creating dictionary from an existing dictionary
        # new_dict = {new_key:new_value for (key,value) in dict.items()}
        
    # 3. Creating dictionary from an existing dictionary according to a condition
        # new_dict = {new_key:new_value for (key,value) in dict.items() if test}
    
import random

names = ["Ali", "Ahmad", "Hamid", "Sarah", "Hamayoon", "Hadi"]
students_score = {student:random.randint(1, 100) for student in names}
# print(students_score)

passed_students = {student:score for (student, score) in students_score.items() if score > 70}
print(passed_students)



# Exercise #1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_list = sentence.split()

result = {item:len(item) for item in word_list}
print(result)



# Exercise #2
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {key:(value*9/5)+32 for (key, value) in weather_c.items()}

print(weather_f)

