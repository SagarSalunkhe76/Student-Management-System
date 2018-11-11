import os
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from DBHandler_SMS import *
import socket
import requests

root1 = Tk()
root1.title("Welcome to Inventory")
root1.geometry("400x400+400+100")

photo=PhotoImage(file="SMS.gif")
photo=photo.subsample(1,1)
photoLabel=Label(root1,image=photo,borderwidth=0,highlightthickness=0)
photoLabel.image=photo
photoLabel.pack()

labelCity=Label(root1,text="Location",font=('arial',10,'bold'),width=20)
labelCity.pack(pady=5)
txtCity = Entry(root1,width=12,font=('arial',10,'bold'))
txtCity.pack(pady=5)
labelTemp=Label(root1,text="Temperature",font=('arial',10,'bold'),width=20)
labelTemp.pack(pady=5)
txtTemp = Entry(root1,width=12,font=('arial',10,'bold'))
txtTemp.pack(pady=5)




try:
    socket.create_connection(("www.google.com",80))
    res=requests.get("https://ipinfo.io")
    data=res.json()
    city=data['city']
    txtCity.config(state=NORMAL)
    txtCity.delete(0,END)
    txtCity.insert(0,city)
    txtCity.config(state=DISABLED)
    a1= "https://api.openweathermap.org/data/2.5/weather?units=metric"
    a2="&q="+city
    a3="&appid=3b752418ccdb63e695a103fa415f0c87"
    addr=a1+a2+a3
    res=requests.get(addr)
    data=res.json()
    main=data['main']
    temp=main['temp']
    txtTemp.config(state=NORMAL)
    txtTemp.delete(0,END)
    txtTemp.insert(0,temp)
    txtTemp.config(state=DISABLED)
    
except OSError as e:
    print("Check your internet connection",e)

def ShowSMS():
    root1.withdraw()
    root.deiconify()

root = Toplevel(root1)
root.title("Welcome to Student Management System")
root.geometry("400x400+400+100")
root.withdraw()

#root1.after(500,lambda:root.deiconify()) #splash the root1 for 1500 second
#root.after(500,lambda:root1.withdraw())


Root1Button=Button(root1,text="Student Management System!",font=('arial',15,'bold'),width=30,command=ShowSMS)
Root1Button.pack(pady=20)







#Main window GUI

def addFrameShow():
    root.withdraw()
    AddFrame.deiconify()

RootAddButton=Button(root,text="Add Record",font=('arial',10,'bold'),width=20,command=addFrameShow)
RootAddButton.pack(pady=20)

def viewFrameShow():
    root.withdraw()
    ViewFrame.deiconify()
    data=viewStudent()
    try:
        ViewFrameScrolledText.config(state=NORMAL)
        ViewFrameScrolledText.delete('1.0',END)
        ViewFrameScrolledText.insert(INSERT,data)
        ViewFrameScrolledText.config(state=DISABLED)
    except Exception:
        print("issue:", e)


RootViewButton=Button(root,text="View Record",font=('arial',10,'bold'),width=20,command=viewFrameShow)
RootViewButton.pack(pady=20)

def updateFrameShow():
    root.withdraw()
    UpdateFrame.deiconify()
    
RootUpdateButton=Button(root,text="Update Record",font=('arial',10,'bold'),width=20,command=updateFrameShow)
RootUpdateButton.pack(pady=20)

def deleteFrameShow():
    root.withdraw()
    DeleteFrame.deiconify()
    
RootDeleteButton=Button(root,text="Delete Record",font=('arial',10,'bold'),width=20,command=deleteFrameShow)
RootDeleteButton.pack(pady=20)

AddFrame = Toplevel(root)
AddFrame.title("Add Student Record into System")
AddFrame.geometry("400x400+400+100")
AddFrame.withdraw()

#Adding student record Frame in system GUI code

AddFrameHeading=Label(AddFrame,text="Please fill below details",font=('arial',10,'bold'),width=20)
AddFrameHeading.grid(row=0,column=2,columnspan=10,padx=2,pady=2,rowspan=2)

AddFrameRnoLabel=Label(AddFrame,text="Roll Number : ",font=('arial',10,'bold'),width=20)
AddFrameRnoLabel.grid(row=8,column=4,columnspan=3,padx=2,pady=2,rowspan=2)

AddFrameRnoTextEntry=Entry(AddFrame,bd=5,font=('arial',10,'bold'),width=20)
AddFrameRnoTextEntry.grid(row=8,column=7,columnspan=3,padx=5,pady=2,rowspan=2)

AddFrameNameLabel=Label(AddFrame,text="Student Name : ",font=('arial',10,'bold'),width=20)
AddFrameNameLabel.grid(row=10,column=4,columnspan=3,padx=5,pady=2,rowspan=2)

AddFrameNameTextEntry=Entry(AddFrame,bd=5,font=('arial',10,'bold'),width=20)
AddFrameNameTextEntry.grid(row=10,column=7,columnspan=3,padx=5,pady=2,rowspan=2)

def addSaveData():
    try:
        if(AddFrameRnoTextEntry.get()!='' and AddFrameNameTextEntry.get()!=''):
            try:
                rno=AddFrameRnoTextEntry.get()
                name=AddFrameNameTextEntry.get().capitalize()
                if(name.isalpha() and rno.isdigit()): 
                    addStudent(int(rno),name)
                else:
                    messagebox.showerror("Value Error","Name should be alphabetic")
                    
            except:
                er="Rno.should be integer"
                messagebox.showerror("Value error",str(er))
        else:
            messagebox.showerror("error","Field can not be empty")

    except Exception as e:
        messagebox.showerror("error",str(er))
        
    finally:
        AddFrameRnoTextEntry.delete(0,END)
        AddFrameNameTextEntry.delete(0,END)
        AddFrameRnoTextEntry.focus()
    
    


AddFrameSaveButton=Button(AddFrame,text="Save Record",font=('arial',10,'bold'),width=20,command=addSaveData)
AddFrameSaveButton.grid(row=12,column=4,columnspan=3,padx=2,pady=2,rowspan=2)

def addFrameBack():
    AddFrame.withdraw()
    root.deiconify()

AddFrame.protocol("WM_DELETE_WINDOW",addFrameBack)

AddFrameBackButton=Button(AddFrame,text="Back",font=('arial',10,'bold'),width=20,command=addFrameBack)
AddFrameBackButton.grid(row=12,column=7,columnspan=3,padx=2,pady=2,rowspan=2)



#Viewing student record Frame in system GUI code


ViewFrame = Toplevel(root)
ViewFrame.title("View Student Record into System")
ViewFrame.geometry("400x400+400+100")
ViewFrame.withdraw()



ViewFrameScrolledText=scrolledtext.ScrolledText(ViewFrame,width=30,height=10)
ViewFrameScrolledText.pack(pady=20)

def viewFrameClose():
    ViewFrame.withdraw()
    root.deiconify()

ViewFrame.protocol("WM_DELETE_WINDOW",viewFrameClose)

def viewFrameScrollTextClearAndBack():
    ViewFrame.withdraw()
    ViewFrameScrolledText.delete('1.0',END)
    root.deiconify()

ViewFrameBackButton=Button(ViewFrame,text="Back",font=('arial',10,'bold'),width=20,command=viewFrameScrollTextClearAndBack)
ViewFrameBackButton.pack(pady=20)



#Updating student record Frame in system GUI code

UpdateFrame = Toplevel(root)
UpdateFrame.title("Update Student Record into System")
UpdateFrame.geometry("400x400+400+100")
UpdateFrame.withdraw()

UpdateFrameRnoLabel=Label(UpdateFrame,text="Roll Number : ",font=('arial',10,'bold'),width=20)
UpdateFrameRnoLabel.pack(pady=20)

UpdateFrameRnoTextEntry=Entry(UpdateFrame,bd=5,font=('arial',10,'bold'),width=20)
UpdateFrameRnoTextEntry.pack(pady=20)

UpdateFrameNameLabel=Label(UpdateFrame,text="Student Name : ",font=('arial',10,'bold'),width=20)
UpdateFrameNameLabel.pack(pady=20)

UpdateFrameNameTextEntry=Entry(UpdateFrame,bd=5,font=('arial',10,'bold'),width=20)
UpdateFrameNameTextEntry.pack(pady=20)

def updateSaveData():
    try:
        if(UpdateFrameRnoTextEntry.get()!='' and UpdateFrameNameTextEntry.get()!=''):
            
            try:
                rno=UpdateFrameRnoTextEntry.get()
                name=UpdateFrameNameTextEntry.get().capitalize()
                if(name.isalpha()):
                    updateStudent(int(rno),name)
                else:
                    messagebox.showerror("Value Error","Name should be aplhabetic")
                
            except ValueError as e:
                er="Rno. should be Integer Only"
                messagebox.showerror("Value Error",str(er))
        else:
            messagebox.showerror("error","Field can not be empty")
        
            

    except Exception as e:
        print("Issue: ",e)
        
    finally:
        UpdateFrameRnoTextEntry.delete(0,END)
        UpdateFrameNameTextEntry.delete(0,END)
        UpdateFrameRnoTextEntry.focus()
    
    
UpdateFrameSaveButton=Button(UpdateFrame,text="Update Record",font=('arial',10,'bold'),width=20,command=updateSaveData)
UpdateFrameSaveButton.pack(pady=20)

def updateFrameBack():
    UpdateFrame.withdraw()
    root.deiconify()

UpdateFrame.protocol("WM_DELETE_WINDOW",updateFrameBack)

UpdateFrameBackButton=Button(UpdateFrame,text="Back",font=('arial',10,'bold'),width=20,command=updateFrameBack)
UpdateFrameBackButton.pack(pady=20)




#Deleting student record Frame in system GUI code

DeleteFrame = Toplevel(root)
DeleteFrame.title("Delete Student Record into System")
DeleteFrame.geometry("400x400+400+100")
DeleteFrame.withdraw()

DeleteFrameRnoLabel=Label(DeleteFrame,text="Roll Number : ",font=('arial',10,'bold'),width=20)
DeleteFrameRnoLabel.pack(pady=20)

DeleteFrameRnoTextEntry=Entry(DeleteFrame,bd=5,font=('arial',10,'bold'),width=20)
DeleteFrameRnoTextEntry.pack(pady=20)

def deleteSaveData():
    try:
        if(DeleteFrameRnoTextEntry.get()!=''):
            try:
                rno=DeleteFrameRnoTextEntry.get()
                deleteStudent(int(rno))
            except ValueError as e:
                er="Rno. should be Integer Only"
                messagebox.showerror("Value Error",str(er))
        else:
            messagebox.showerror("error","Field can not be empty")
        
    except Exception as e:
        messagebox.showerror("Issue: ",str(e))
        
    finally:
        DeleteFrameRnoTextEntry.delete(0,END)
        DeleteFrameRnoTextEntry.focus()
    
    
DeleteFrameSaveButton=Button(DeleteFrame,text="Delete Record",font=('arial',10,'bold'),width=20,command=deleteSaveData)
DeleteFrameSaveButton.pack(pady=20)

def deleteFrameBack():
    DeleteFrame.withdraw()
    root.deiconify()

DeleteFrame.protocol("WM_DELETE_WINDOW",deleteFrameBack)

DeleteFrameBackButton=Button(DeleteFrame,text="Back",font=('arial',10,'bold'),width=20,command=deleteFrameBack)
DeleteFrameBackButton.pack(pady=20)


def rootBack():
   root.withdraw()
   root1.deiconify()

root.protocol("WM_DELETE_WINDOW",rootBack)

ButtonRootBack=Button(root,text="HOME",font=('arial',15,'bold'),width=20,command=rootBack)
ButtonRootBack.pack(pady=20)

#Closing root1 (Main GUI)

def root1Exit():
    ans=messagebox.askyesno("Exit","Do you want to Exit?")
    if ans:
        import sys
        root1.destroy()
        sys.exit()

root1.protocol("WM_DELETE_WINDOW",root1Exit)




#mail window

root1.mainloop()
