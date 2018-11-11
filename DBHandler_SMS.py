import cx_Oracle
from tkinter import messagebox

def addStudent(rno,name):
    con=None
    cursor=None

    try :
        con=cx_Oracle.connect("system/abc123")
        cursor=con.cursor()
        sql="insert into stud values('%d','%s')"
        args=(rno,name)
        cursor.execute(sql%args)
        con.commit()
        print(cursor.rowcount," row inserted")
        msg=str(cursor.rowcount)+" rows inserted"
        messagebox.showinfo("Insert Success",msg)
    except cx_Oracle.DatabaseError as e:
        con.rollback()
        print("Issue : ",e)
        messagebox.showerror("Failure",str(e))

    finally:    
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()

def viewStudent():
    con=None
    cursor=None
    try:
        con=cx_Oracle.connect("system/abc123")
        cursor=con.cursor()
        sql="select * from stud"
        cursor.execute(sql)
        data=cursor.fetchall()
        info=""
        for i in data:
            rno=i[0]
            name=i[1]
            info=info+"Rno: "+str(rno)+" "+"Name: "+name+"\n"

    except cx_Oracle.DatabaseError as e1:
        print("Issue :",e1)
        messagebox.showerror("Failure",str(e1))

    finally:

        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()

    return info

def updateStudent(rno,name):
    con=None
    cursor=None
    try:
        con=cx_Oracle.connect("system/abc123")
        cursor=con.cursor()
        sql="update stud set name='%s' where rno='%d'"
        args=(name,rno)
        cursor.execute(sql%args)
        
        con.commit()
        print(cursor.rowcount," row updated")
        msg=str(cursor.rowcount)+" rows updated"
        messagebox.showinfo("Update Success",msg)
        
    except cx_Oracle.DatabaseError as e2:
        con.rollback()
        print("Issue : ",e2)
        messagebox.showerror("Failure",str(e2))

    finally:    
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()
    
    
def deleteStudent(rno):
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		sql="delete from stud where rno='%d'"
		args=(rno)
		cursor.execute(sql % args)
		
		con.commit()
		print(cursor.rowcount,"rows deleted")
		msg=str(cursor.rowcount)+" rows deleted"
		messagebox.showinfo("Delete Success",msg)
	except cx_Oracle.DatabaseError as e3:
		con.rollback()
		print('issue',e3)
		messagebox.showerror("Failure",str(e3))
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()    
