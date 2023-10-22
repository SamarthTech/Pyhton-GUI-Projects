from tkinter import *
root=Tk()
root.title("BMI CALCULATOR")
root.configure(bg="White")

def bmi(): 
	BMI = float(txt_1.get())/(float (txt_2.get())*float(txt_2.get()))
	txt_3.insert(0,BMI)
	if(BMI<18.5):
		txt_4.insert(0,"UNDERWEIGHT")
	elif(BMI<24.9):
		txt_4.insert(0,"NORMAL WEIGHT")
	else:
		txt_4.insert(0,"OVER WEIGHT")

def del1():
	txt_1.delete(0,END)
	txt_2.delete(0,END)
	txt_3.delete(0,END)
	txt_4.delete(0,END)

    

Label_1=Label(root, text="WEIGHT(in KGs): ")
Label_1.grid(row=0,column=0)
txt_1=Entry(root,width=10,borderwidth=6)
txt_1.grid(row=0,column=1)

Label_2=Label(root, text="HEIGHT(in Metres): ")
Label_2.grid(row=1,column=0)
txt_2=Entry(root,width=10,borderwidth=6)
txt_2.grid(row=1,column=1)

butt=Button(root, text="CALCULATE",bg="Silver",command=bmi)
butt.grid(row=2,column=0)

dele=Button(root, text="CLEAR",bg="Silver",command=del1)
dele.grid(row=2,column=1)

Label_3=Label(root, text="RESULT:")
Label_3.grid(row=4,column=0)
txt_3=Entry(root,width=20,borderwidth=6)
txt_3.grid(row=4,column=1)

Label_4=Label(root, text="CATEGORY:")
Label_4.grid(row=5,column=0)
txt_4=Entry(root,width=20,borderwidth=6)
txt_4.grid(row=5,column=1)
root.mainloop()