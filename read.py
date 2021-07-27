from tkinter import *
import sqlite3
import pyttsx3
from datetime import datetime
from datetime import date

def buildread():
 conn = sqlite3.connect('database copy.db')
 c = conn.cursor()


 number = []
 patients = []
 
 
 sql = "SELECT * FROM appointments where date >= CURRENT_DATE order by date,scheduled_time";
 res = c.execute(sql)
 for r in res:
    ids = r[0]
    name = r[1]
    number.append(ids)
    patients.append(name)


 class Application:
    def __init__(self, master):
        self.master = master

        self.x = 0
        
      
        self.heading = Label(master, text="Appointments", font=('arial 60 bold'), fg='green')
        self.heading.place(x=350, y=0)

       
        self.change = Button(master, text="Next Patient", width=25, height=2, bg='steelblue', command=self.func)
        self.change.place(x=500, y=600)

       
        self.n = Label(master, text="", font=('arial 200 bold'))
        self.n.place(x=500, y=100)

        self.pname = Label(master, text="", font=('arial 80 bold'))
        self.pname.place(x=300, y=400)
 
    def func(self):
        self.n.config(text=str(number[self.x]))
        self.pname.config(text=str(patients[self.x]))
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-50)
        engine.say('Patient number ' + str(number[self.x]) + str(patients[self.x]))
        engine.runAndWait()
        self.x += 1
 root = Tk()
 b = Application(root)
 root.title("Text-to-Speech")
 root.geometry("1366x768+0+0")
 root.resizable(False, False)
 root.mainloop()
