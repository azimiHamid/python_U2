import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Create a Label widget and use pack to place it in the window
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "italic"))
# my_label.pack(side="left")
# Use pack with expand=1 to make the label fill any extra space in the window
my_label.pack(expand=1)







window.mainloop()