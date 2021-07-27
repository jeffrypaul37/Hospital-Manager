
import sqlite3

import tkinter  as tk 
from tkinter import *
import tkinter

def call():
    global my_w
    my_w = tk.Tk()
    my_w.geometry("300x200")
    my_w.title("Upcoming Appointments")
    buildview(0)
    

def buildview(offset):

    my_conn = sqlite3.connect('database copy.db')
    r_set=my_conn.execute("SELECT count(*) as no from appointments where date >= CURRENT_DATE")
    data_row=r_set.fetchone()
    no_rec=data_row[0] 
    limit = 8;



    
    

    q="SELECT ID,name,date,scheduled_time from appointments where date >= CURRENT_DATE order by date,scheduled_time LIMIT "+ str(offset) +","+str(limit)
    r_set=my_conn.execute(q);
    e=Label(my_w ,width=10,text='ID',borderwidth=1, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=Label(my_w ,width=10,text='Name',borderwidth=1, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
 
    e=Label(my_w ,width=10,text='Date',borderwidth=1, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=Label(my_w ,width=10,text='Time',borderwidth=1, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
 
  
  
    i=1 
    for student in r_set: 
        for j in range(len(student)):
            e = Entry(my_w, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
        i=i+1
    while (i<=limit):  
        for j in range(len(student)):
            e = Entry(my_w, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, "")
        i=i+1
    
    back = offset - limit 
    next = offset + limit        
    b1 = tk.Button(my_w, text='Next >', command=lambda: buildview(next))
    b1.grid(row=12,column=2)
    b2 = tk.Button(my_w, text='< Prev', command=lambda:buildview(back))
    b2.grid(row=12,column=1)
    if(no_rec <= next): 
        b1["state"]="disabled" 
    else:
        b1["state"]="active" 
        
    if(back >= 0):
        b2["state"]="active"  
    else:
        b2["state"]="disabled"
    my_w.mainloop()



call()      

