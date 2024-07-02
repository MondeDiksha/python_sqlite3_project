#using GUI

from tkinter import*
from tkinter.messagebox import*
from sqlite3 import*

root=Tk()
root.title("whats Next App")
root.geometry("1000x500+300+140")
f=("cambria",30,"bold")

lab_name=Label(root,text="enter name ",font=f)
ent_name=Entry(root,font=f)
lab_name.place(x=30,y=30)
ent_name.place(x=300,y=30)

c=IntVar()
c.set(1)
lab_choice=Label(root,text="select one",font=f)
rb_job=Radiobutton(root,text="job",font=f,variable=c,value=1)
rb_ms=Radiobutton(root,text="Ms",font=f,variable=c,value=2)
rb_mba=Radiobutton(root,text="Mba",font=f,variable=c,value=3)

lab_choice.place(x=30,y=100)
rb_job.place(x=300,y=100)
rb_ms.place(x=300,y=170)
rb_mba.place(x=300,y=240)

def save():
	con=None
	try:
		con=connect("wn.db")
		cursor=con.cursor()
		sql="insert into student values('%s','%s')"
		name=ent_name.get()
		if c.get()==1:
			choice="job"
		elif c.get()==2:
			choice="ms"
		else:
			choice="mba"
		cursor.execute(sql%(name,choice))
		con.commit()
		showinfo("success","thankyou")
		ent_name.focus()
	except Exception as e:
		con.rollback()
		showerror("issue",e)
	finally:
		if con is None:
			con.close()

btn_submit=Button(root,text="submit",font=f,width=10,command=save)
btn_submit.place(x=300,y=330)


root.mainloop()