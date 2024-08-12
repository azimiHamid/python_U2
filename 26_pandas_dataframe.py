#   ✅ How to loop over a pandas DataFrame ?
import pandas

student_dict = {
    "student": ["Hamid", "Sarah", "Hadi", "Hamayoon"],
    "score": [98, 92, 88, 85]
}

# 🥴 Looping through dictionaries
for (key,value) in student_dict.items():
    # print(key)
    pass



student_data_frame = pandas.DataFrame(student_dict)

# Loop through a Data Frame
for (key, value) in student_data_frame.items():
    # print(value)
    pass

# Loop through a Data Frame using pandas iterrows() method
for (index, row) in student_data_frame.iterrows():
    if row.student == "Hamid":
        print(row.score)
    print(row.student.upper())
