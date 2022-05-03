#Create a program to produce the interface. Click the button to chnage its background color to yellow.

from tkinter import *
window = Tk()

window.geometry('450x350+30+20')
window.title("Special Midterm Exam in OOP")

btn = Button(window, text="<---Click to change color of the button")
btn.place(x=135, y= 165)

btn = Button(window, text="Color", fg="red", bg="#0000ff", activebackground="#0000ff")
btn.place(x=75, y=165)

window.mainloop()
