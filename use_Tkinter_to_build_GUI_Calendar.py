from tkinter import *
from tkcalendar import *

root=Tk()

def selectDate():
    myDAte=myCal.get_date()
    selectDate=Label(text=myDAte)
    selectDate.pack(padx=2,pady=2)

myCal=Calendar(root,date_pattern="dd/mm/yyyy")
myCal.pack(padx=15,pady=15)

open_cal=Button(root,text="Select Date",command=selectDate)
open_cal.pack(padx=15,pady=15)

root.geometry("300x300")
root.title("Calendar")
root.configure(background="lightblue")
# root.resizable(False,False)

root.mainloop()