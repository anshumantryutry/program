from tkinter import *
import webbrowser

root = Tk()

root.title("Program")
root.geometry("1000x2000")

label = Label(root, text="What is it's name: ")
label.grid()
entry = Entry(root, width = 10)
entry.grid()
def clicked():
    if entry.get() == "piecetoapuzzle":
        label.configure(text = "Well done. Dont get too excited")
        webbrowser.open('https://github.com/anshumantryutry/arg/archive/refs/heads/main.zip')
    else:
        label.configure(text="No")

button = Button(root, text="Enter", fg='red', command=clicked)
button.grid()
root.mainloop()

