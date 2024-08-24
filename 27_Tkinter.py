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
    my_label["text"] = input.get()

button = Button(text="Click me", command=button_clicked)
button.pack()

button['text'] = "don't click"
button.config(text='click here')



# Entry
input = Entry(width=30)
input.pack()




# listbox
def listbox_used(event):
    # gets current selection from listbox
    print(listbox.get(listbox.curselection()))
    
listbox = Listbox(height=4)
fruits = ["Apple", "Grape", "Banana", "Orange"]
for fruit in fruits:
    listbox.insert(fruits.index(fruit), fruit)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()




window.mainloop()