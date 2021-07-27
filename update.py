
from tkinter import *
import tkinter.messagebox 
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno
def buildupdate():
 conn = sqlite3.connect('database copy.db')
 c = conn.cursor()
 

 class Application:
    def __init__(self, master):
        self.master = master
      
        self.heading = Label(master, text="Patient Details",  fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=150, y=0)

        self.name = Label(master, text="Enter Patient ID", font=('arial 18 bold'))
        self.name.place(x=0, y=60)

        
        self.namenet = Entry(master, width=30)
        self.namenet.place(x=280, y=62)

     
        self.search = Button(master, text="Search", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=350, y=102)
  
    def search_db(self):
        self.input = self.namenet.get()
     

        sql = "SELECT * FROM appointments WHERE ID LIKE ?"
        self.res = c.execute(sql, (self.input,))
        
        
        for self.row in self.res:
                self.name1 = self.row[1]
                self.age = self.row[2]
                self.gender = self.row[3]
                self.location = self.row[4]
                self.date = self.row[7]
                self.time = self.row[6]
                self.phone=self.row[5]
                self.allergy=self.row[8]
                self.chronic=self.row[9]
                self.bg=self.row[10]
        self.count=c.fetchone()
        c.execute(sql, (self.input,))
        self.count=c.fetchone()   
        if(self.count==None):
            tkinter.messagebox.showinfo("Warning", "Patient not found")        
        else:
            
      
            self.uname = Label(self.master, text="Patient's Name", font=('arial 18 bold'))
            self.uname.place(x=0, y=140)

            self.uage = Label(self.master, text="Age", font=('arial 18 bold'))
            self.uage.place(x=0, y=180)

            self.ugender = Label(self.master, text="Gender", font=('arial 18 bold'))
            self.ugender.place(x=0, y=220)

            self.ulocation = Label(self.master, text="Location", font=('arial 18 bold'))
            self.ulocation.place(x=0, y=260)

            self.udate = Label(self.master, text="Appointment Date", font=('arial 18 bold'))
            self.udate.place(x=0, y=300)

            self.utime = Label(self.master, text="Appointment Time", font=('arial 18 bold'))
            self.utime.place(x=0, y=340)

            self.uphone = Label(self.master, text="Phone Number", font=('arial 18 bold'))
            self.uphone.place(x=0, y=380)

            self.uall = Label(self.master, text="Allergies", font=('arial 18 bold'))
            self.uall.place(x=0, y=420)

            self.uchronic = Label(self.master, text="Chronic Conditions", font=('arial 18 bold'))
            self.uchronic.place(x=0, y=460)

            self.ubg = Label(self.master, text="Blood Group", font=('arial 18 bold'))
            self.ubg.place(x=0, y=500)


         
            self.ent1 = Entry(self.master, width=30)
            self.ent1.place(x=300, y=140)
            self.ent1.insert(END, str(self.name1))

            self.ent2 = Entry(self.master, width=30)
            self.ent2.place(x=300, y=180)
            self.ent2.insert(END, str(self.age))

            self.ent3 = Entry(self.master, width=30)
            self.ent3.place(x=300, y=220)
            self.ent3.insert(END, str(self.gender))

            self.ent4 = Entry(self.master, width=30)
            self.ent4.place(x=300, y=260)
            self.ent4.insert(END, str(self.location))

            self.ent5 = Entry(self.master, width=30)
            self.ent5.place(x=300, y=300)
            self.ent5.insert(END, str(self.date))

            self.ent6 = Entry(self.master, width=30)
            self.ent6.place(x=300, y=340)
            self.ent6.insert(END, str(self.time))

            self.ent7 = Entry(self.master, width=30)
            self.ent7.place(x=300, y=380)
            self.ent7.insert(END, str(self.phone))

            self.ent8 = Entry(self.master, width=30)
            self.ent8.place(x=300, y=420)
            self.ent8.insert(END, str(self.allergy))

            self.ent9 = Entry(self.master, width=30)
            self.ent9.place(x=300, y=460)
            self.ent9.insert(END, str(self.chronic))

            self.ent10 = Entry(self.master, width=30)
            self.ent10.place(x=300, y=500)
            self.ent10.insert(END, str(self.bg))

            
            self.update = Button(self.master, text="Update", width=20, height=2, bg='lightblue', command=self.update_db)
            self.update.place(x=400, y=540)

         
            self.delete = Button(self.master, text="Cancel Appointment", width=20, height=2, bg='red', command=self.delete_db)
            self.delete.place(x=150, y=540)
            
    def update_db(self):
        
        self.var1 = self.ent1.get() 
        self.var2 = self.ent2.get() 
        self.var3 = self.ent3.get() 
        self.var4 = self.ent4.get() 
        self.var5 = self.ent5.get() 
        self.var6 = self.ent6.get()
        self.var7 = self.ent7.get()
        self.var8 = self.ent8.get()
        self.var9 = self.ent9.get()
        self.var10 = self.ent10.get()

        query = "UPDATE appointments SET name=?, age=?, gender=?, location=?, phone=?,date=?, scheduled_time=? ,Allergies=?,Chronic_Conditions=?,Blood_Group=? WHERE ID LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var7, self.var5,self.var6, self.var8,self.var9,self.var10,self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Updated", "Successfully Updated.")

    def delete_db(self):
     
     answer = askyesno(title='Confirm Cancellation', message='Are you sure you want to cancel this appointment?')
     if answer:
       
       
        sql2 = "DELETE FROM appointments WHERE ID LIKE ?"
        c.execute(sql2, (self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Appointment Cancelled!")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()
        self.ent6.destroy()
        self.ent7.destroy()
        self.ent8.destroy()
        self.ent9.destroy()
        self.ent10.destroy()

    
     



 root = Tk()
 
 b = Application(root)
 root.geometry("1200x720+0+0")
 root.title("Update")
 root.resizable(False, False)
 root.mainloop()
