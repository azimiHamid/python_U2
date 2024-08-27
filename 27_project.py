# Mile to Km Converter
from tkinter import * # type: ignore

def miles_to_km():
    miles = float(input.get())
    km = round(miles * 1.609, 2)
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title('Miles to KM Converter')
window.config(padx=20, pady=20)


input = Entry(width=10)
input.grid(row=0 , column=1)


miles_label = Label(text='Miles')
miles_label.grid(row=0 , column=2)

is_equal_label = Label(text='is equal to')
is_equal_label.grid(row=1 , column=0)

kilometer_result_label = Label(text='0')
kilometer_result_label.grid(row=1 , column=1)

kilometer_label = Label(text='Km')
kilometer_label.grid(row=1 , column=2)

calculate_btn = Button(text='Calculate', command=miles_to_km)
calculate_btn.grid(row=2 , column=1)


window.mainloop()
