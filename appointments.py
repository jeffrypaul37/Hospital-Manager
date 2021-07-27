from tkinter import *
from tkcalendar import Calendar
from datetime import datetime
from datetime import date


import re
import sqlite3
import tkinter.messagebox

import pandas as pd
import datetime

from dateutil import rrule, parser
today = date.today()
date1 = '05-10-2021'
date2 = '12-31-2050'
datesx = list(rrule.rrule(rrule.DAILY, dtstart=parser.parse(date1), until=parser.parse(date2)))

conn = sqlite3.connect('database copy.db')

c = conn.cursor()

ids = []


class Application:
    def __init__(self, master):
        self.master = master

        
        self.left = Frame(master, width=800, height=720, bg='sea green')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side=RIGHT)

       
        self.heading = Label(self.left, text="Histolab Appointments", font=('arial 40 bold'), fg='black', bg='sea green')
        self.heading.place(x=0, y=0)
      
        self.name = Label(self.left, text="Patient's Name", font=('arial 18 bold'), fg='black', bg='sea green')
        self.name.place(x=0, y=100)

      
        self.age = Label(self.left, text="Age", font=('arial 18 bold'), fg='black', bg='sea green')
        self.age.place(x=0, y=140)

        
        self.gender = Label(self.left, text="Gender", font=('arial 18 bold'), fg='black', bg='sea green')
        self.gender.place(x=0, y=180)

      
        self.location = Label(self.left, text="Location", font=('arial 18 bold'), fg='black', bg='sea green')
        self.location.place(x=0, y=220)

         
        self.date = Label(self.left, text="Appointment Date", font=('arial 18 bold'), fg='black', bg='sea green')
        self.date.place(x=0, y=260)

  


      
        
        self.time = Label(self.left, text="Appointment Time", font=('arial 18 bold'), fg='black', bg='sea green')
        self.time.place(x=0, y=300)

        
        self.phone = Label(self.left, text="Phone Number", font=('arial 18 bold'), fg='black', bg='sea green')
        self.phone.place(x=0, y=340)

        
        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=250, y=100)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250, y=140)
        
        self.clicked=StringVar()
        self.clicked.set("Male")
        self.gender_ent = OptionMenu(self.left,self.clicked,*options)
        self.gender_ent.pack()
        self.gender_ent.place(x=250, y=180)

        self.location_ent=Entry(self.left,width=30)
        self.location_ent.place(x=250, y=220)

        self.clicked1=StringVar()
        self.clicked1.set(today)
        self.date_ent = OptionMenu(self.left,self.clicked1,*options1)
        self.date_ent.pack()
        self.date_ent.place(x=250, y=260)
        

        
        
        self.clicked2=StringVar()
        self.clicked2.set("10am-11am")
        self.time_ent = OptionMenu(self.left,self.clicked2,*options2)
        self.time_ent.pack()
        self.time_ent.place(x=250, y=300)
     
        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=250, y=340)

       
        self.submit = Button(self.left, text="Add Appointment", width=20, height=2, bg='steelblue', command=self.add_appointment)
        self.submit.place(x=300, y=380)
    
        
        sql2 = "SELECT ID FROM appointments"
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)
        
      
        self.new = sorted(ids)
        self.final_id = self.new[len(ids)-1]
        
        self.logs = Label(self.right, text="Logs", font=('arial 28 bold'), fg='white', bg='steelblue')
        self.logs.place(x=0, y=0)

        self.box = Text(self.right, width=50, height=40)
        self.box.place(x=20, y=60)

        
    
    def add_appointment(self):
   
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.clicked.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.clicked1.get()
        self.val6 = self.clicked2.get()
        self.val7 = self.phone_ent.get()
        pattern=re.compile("[7-9][0-9]{9}")
        pattern2=re.compile("[1-9]([0-9])*")
        pattern1=re.compile(r'([A-Z])(\s*[A-Z])*$')
        pattern.match(self.val7)

        
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '' or self.val6=='' or self.val7=='':
            print("ty",self.val3)
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
            print(self.val3)
        elif not(pattern1.match(self.val1)) or len(self.val1)<2:
                 tkinter.messagebox.showinfo("Warning","INVALID Name")
        elif not(pattern2.match(self.val2)) or len(self.val2)>=3:
                 tkinter.messagebox.showinfo("Warning","INVALID Age")

        elif not(pattern.match(self.val7)) or len(self.val7)>10:
            tkinter.messagebox.showinfo("Warning", "INVALID Phone Number")
        

            

        else:
           
            sql = "INSERT INTO 'appointments' (name, age, gender, location, scheduled_time, phone,date) VALUES(?, ?, ?, ?, ?, ?,?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val6, self.val7,self.val5))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Appointment for " + str(self.val1) + " has been created" )
            

            self.box.insert(END, '\n Appointment fixed for ' + str(self.val1) + '\n at ' + str(self.val5)+','+str(self.val6))
            self.name_ent.delete(0,END)
            self.age_ent.delete(0,END)
           
            self.location_ent.delete(0,END)
          
            self.phone_ent.delete(0,END)
            


root = Tk()

root.geometry("1200x720+0+0")
options=["Male","Female"]
options1=datesx
options2=["10am-11am","11am-12pm","1pm-2pm"]



b = Application(root)


root.resizable(False, False)


root.mainloop()
