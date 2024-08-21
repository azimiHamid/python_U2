from tkinter import * # type: ignore

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label
# Create a Label widget and use pack to place it in the window
my_label = Label(text="I am a label", font=("Arial", 24, "italic"))
my_label.pack()
# my_label.pack(side="left")
# Use pack with expand=1 to make the label fill any extra space in the window
# my_label.pack(expand=1)

my_label["text"] = "New Text"
my_label.config(text="Some Text")


# Button
def button_clicked():
    print("Button clicked!")

button = Button(text="Click me", command=button_clicked)
button.pack()




window.mainloop()