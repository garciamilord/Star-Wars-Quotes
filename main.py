# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
from tkinter import *


# top = Tkinter.Tk()
#
# def helloCallBack():
#    tkMessageBox.showinfo( "Hello Python", "Hello World")
#
# B = Tkinter.Button(top, text ="Hello", command = helloCallBack)
#
# B.pack()
# top.mainloop()

Star_Wars_Quote = ["“Someday I will be the most powerful Jedi ever.”", "A long time ago in a galaxy far, far away…","“You were the chosen one! It was said that you would destroy the Sith, not join them. You were to bring balance to the Force, not leave it in darkness.”",
                   "“I’ve been waiting for you, Obi-Wan.\nWe meet again, at last. The circle is now complete.\nWhen I left you, I was but the learner; now I am the master.”",
                   "“Let the past die. Kill it.”","“So this is how liberty dies…with thunderous applause.” ","“You’ll find I’m full of surprises.” ","“Fear is the path to the dark side.”","”Power! Unlimited Power!”" ]


root = Tk()

# specify size of window.
root.geometry("300x250")

# Create text widget and specify size.
T = Text(root, height=5, width=104,bg = "black", fg ="yellow")
l = Label(root, text ="Star Wars Quote of the Day")
l.config(font =("Courier", 12 ))

def helloCallBack():
   Text("Hello World")

def fun():
    Fact = random.choice(Star_Wars_Quote)
    return Fact
# Create button for Generate new Quote text.
b1 = Button(root, text ="Generate", command = fun)

b2 = Button(root, text = "Exit",
            command = root.destroy)

l.pack()
T.pack()
b1.pack()
b2.pack()

# Insert The Fact.
T.insert(END, fun())

root.mainloop()

