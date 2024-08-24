from tkinter import * # type: ignore

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
# Add padding
window.config(padx=50, pady=50)



# Label
my_label = Label(text="I am a label", font=("Arial", 24, "italic"))
# Tkinter Layouts
my_label.pack()
my_label.place(x=0, y=0)
my_label.grid(row=0, column=0)



# Button
def button_clicked():
    my_label["text"] = input.get()

button = Button(text="Click me", command=button_clicked)
button.grid(row=1, column=1)
button.config(padx=10, pady=10)



# Entry
input = Entry(width=30)
input.grid(row=2, column=2)


window.mainloop()