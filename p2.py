#GUI
from tkinter import*
from sqlite3 import*
from tkinter.messagebox import*

root=Tk()
root.title("success stiry App")
root.geometry("600x600+450+120")
f=("Arial",30,"bold")

lab_header=Label(root,text="Successs story App",font=f)
lab_header.pack()

lab_name=Label(root,text="enter name ",font=f)
ent_name=Entry(root,font=f)
lab_name.pack(pady=5)
ent_name.pack(pady=5)

lab_company=Label(root,text="enter company name ",font=f)
ent_company=Entry(root,font=f)
lab_company.pack(pady=5)
ent_company.pack(pady=5)

lab_pkg=Label(root,text="enter pkg ",font=f)
ent_pkg=Entry(root,font=f)
lab_pkg.pack(pady=5)
ent_pkg.pack(pady=5)

def save():
	con=None
	try:
		con=connect("ss.db")
		cursor=con.cursor()
		sql="insert into student values('%s','%s','%f')"
		name=ent_name.get()
		company=ent_company.get()
		pkg=float(ent_pkg.get())
		cursor.execute(sql% (name,company,pkg))
		con.commit()
		showinfo("save","congrats")
		ent_name.delete(0,END)
		ent_company.delete(0,END)
		ent_pkg.delete(0,END)
		ent_name.focus()
	except Exception as e:
		con.rollback()
		print("issue",e)
	finally:
		if con is not None:
			con.close()

btn_submit=Button(root,text="submit",font=f,command=save)
btn_submit.pack(pady=20)


root.mainloop()

