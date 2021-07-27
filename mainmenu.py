from tkinter import *
from tkcalendar import Calendar
from datetime import datetime
from datetime import date

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno

import re
import sqlite3
import tkinter.messagebox
import pandas as pd

import pandas as pd
import datetime

from dateutil import rrule, parser
today = date.today()
date1 = '05-10-2021'
date2 = '12-31-2050'
datesx = pd.date_range(today, date2).tolist()

conn = sqlite3.connect('database copy.db')

c = conn.cursor()



ids = []



class Application:
    def __init__(self, master):
        self.master = master

        
        self.left = Frame(master, width=1000, height=800, bg='sea green')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=1000, height=800, bg='steelblue')
        self.right.pack(side=RIGHT)

       
        self.heading = Label(self.left, text="Appointments", font=('arial 40 bold'), fg='black', bg='sea green')
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

        self.allergies = Label(self.left, text="Allergies", font=('arial 18 bold'), fg='black', bg='sea green')
        self.allergies.place(x=0, y=380)
        self.all_ent = Entry(self.left, width=30)
        self.all_ent.place(x=250, y=380)
        self.all_ent.insert(0, 'NONE')

        self.chronic = Label(self.left, text="Chronic Conditions", font=('arial 18 bold'), fg='black', bg='sea green')
        self.chronic.place(x=0, y=420)
        self.chr_ent = Entry(self.left, width=30)
        self.chr_ent.place(x=250, y=420)
        self.chr_ent.insert(0, 'NONE')

        self.bg = Label(self.left, text="Blood Group", font=('arial 18 bold'), fg='black', bg='sea green')
        self.bg.place(x=0, y=460)
        self.clicked3=StringVar()
        self.clicked3.set("Select Blood Group")
        self.bg_ent = OptionMenu(self.left,self.clicked3,*options3)
        self.bg_ent.pack()
        self.bg_ent.place(x=250, y=460)
        
        
        
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
        self.clicked1.set("Select Date")
        self.date_ent = OptionMenu(self.left,self.clicked1,*options1)
        self.date_ent.pack()
        self.date_ent.place(x=250, y=260)
        

        
        
        self.clicked2=StringVar()
        self.clicked2.set("Select Time")
        self.time_ent = OptionMenu(self.left,self.clicked2,*options2)
        self.time_ent.pack()
        self.time_ent.place(x=250, y=300)
     
        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=250, y=340)

       
        self.submit = Button(self.left, text="Add Appointment", width=20, height=2, bg='steelblue', command=self.add_appointment)
        self.submit.place(x=270, y=500)

        self.submit = Button(self.left, text="View Appointments", width=20, height=2, bg='steelblue', command=self.view)
        self.submit.place(x=600, y=100)

        self.submit = Button(self.left, text="View/Update Patient Details", width=20, height=2, bg='steelblue', command=self.update)
        self.submit.place(x=600, y=200)

        self.submit = Button(self.left, text="Read Names", width=20, height=2, bg='steelblue', command=self.read)
        self.submit.place(x=600, y=300)

        self.submit = Button(self.left, text="Exit", width=20, height=2, bg='steelblue', command=self.quit)
        self.submit.place(x=600, y=400)

       
     
    
    
        
        sql2 = "SELECT ID FROM appointments"
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)
        
      
        self.new = sorted(ids)
        self.final_id = self.new[len(ids)-1]
        
        self.logs = Label(self.right, text="Logs", font=('arial 28 bold'), fg='white', bg='steelblue')
        self.logs.place(x=0, y=0)

        self.box = Text(self.right, width=62, height=45)
        self.box.place(x=20, y=60)

        
    
    def add_appointment(self):
       
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.clicked.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.clicked1.get()
        self.val6 = self.clicked2.get()
        self.val7 = self.phone_ent.get()
        self.val8 = self.all_ent.get()
        self.val9 = self.chr_ent.get()
        self.val10 = self.clicked3.get()
        pattern=re.compile("[7-9][0-9]{9}")
        pattern=re.compile("[7-9][0-9]{9}")
        pattern2=re.compile("[1-9]([0-9])*")
        pattern1=re.compile(r'([A-Z])(\s*[A-Z])*$')
        pattern.match(self.val7)

        
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '' or self.val6=='' or self.val7=='' or self.val10=='Select Blood Group' or self.val5=='Select Date' or self.val6=='Select Time':
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
         
            sql = "INSERT INTO 'appointments' (name, age, gender, location, scheduled_time, phone,date,Allergies,Chronic_Conditions,Blood_Group) VALUES(?, ?, ?, ?, ?, ?,?,?,?,?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val6, self.val7,self.val5,self.val8,self.val9,self.val10))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Appointment for " + str(self.val1) + " has been created" )
            

            self.box.insert(END, '\n Appointment fixed for ' + str(self.val1) + '\n at ' + str(self.val5)+','+str(self.val6))
            self.name_ent.delete(0,END)
            self.age_ent.delete(0,END)
           
            self.location_ent.delete(0,END)
          
            self.phone_ent.delete(0,END)
            self.clicked1.set("Select Date")
            self.clicked2.set("Select Time")
            self.clicked3.set("Select Blood Group")
            self.chr_ent.delete(0,END)
            self.all_ent.delete(0,END)
            self.all_ent.insert(0, 'NONE')
            self.chr_ent.insert(0, 'NONE')
            
          

    
    def view(self):
       import view
       view.call()
       

    
    def update(self):
       import update
       update.buildupdate()

 

    def read(self):
       import read
       read.buildread()

    def quit(self):

        answer = askyesno(title='Confirm Exit', message='Are you sure you want to exit?')
        if answer:
            root.destroy()

    
      

      
 
  
       
       
       
    
root = Tk()
root.title("Shalom Clinic")

#root.geometry("1200x720+0+0")
root.attributes('-fullscreen', True)
root.resizable(0, 0)

Top = Frame(root, bd=1,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=1)
Form.pack(side=TOP, pady=1)
lbl_title = Label(Top, text = "Shalom Clinic", font=('arial', 15))
lbl_title.pack(fill=X)

options=["Male","Female"]
options1=datesx
options2=["10:00:00","11:00:00","13:00:00"]
options3=["O+","O-","A+","A-","B+","B-","AB+","AB-"]

 



b = Application(root)


root.resizable(False, False)


root.mainloop()

