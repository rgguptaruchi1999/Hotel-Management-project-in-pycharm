from tkinter import *
import time
import random
from datetime import date
#price1,price2,price3,price4,price5,price6,price7,price8,

FRAME_ONE_BG_COLOR = "#33A9CE"
FRAME_TWO_BG_COLOR = "#8F2D56"

def price():
	roo = Tk()
	roo.geometry("600x280+0+0")
	roo.title("Price List")
	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM",
	fg="black", bd=5)
	lblinfo.grid(row=0, column=0)
	lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________",
	fg="white", anchor=W)
	lblinfo.grid(row=0, column=2)
	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE",
	fg="black", anchor=W)
	lblinfo.grid(row=0, column=3)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drink",
	fg="#ED420B", anchor=W)
	lblinfo.grid(row=1, column=0)
	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10",
	fg="#ED420B", anchor=W)
	lblinfo.grid(row=1, column=3)
	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger King",
	fg="#ED420B", anchor=W)
	lblinfo.grid(row=2, column=0)
	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30",
	fg="#ED420B", anchor=W)
	lblinfo.grid(row=2, column=3)
	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cherry",
	fg="#ED420B", anchor=W)
	lblinfo.grid(row=3, column=0)
	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="15",
	fg="#ED420B", anchor=W)
	lblinfo.grid(row=3, column=3)
	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Nacho Fries",
	fg="#ED420B", anchor=W)
	lblinfo.grid(row=4, column=0)
	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="20",
	fg="#ED420B", anchor=W)
	lblinfo.grid(row=4, column=3)
	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza",
	fg="#ED420B", anchor=W)
	lblinfo.grid(row=5, column=0)
	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30",
	fg="#ED420B", anchor=W)
	lblinfo.grid(row=5, column=3)
	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Biscuits",
	fg="#ED420B", anchor=W)
	lblinfo.grid(row=6, column=0)
	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10",
	fg="#ED420B", anchor=W)
	lblinfo.grid(row=6, column=3)
	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10",
	fg="#ED420B", anchor=W)
	lblinfo.grid(row=7, column=3)
	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Roll",
	fg="#ED420B", anchor=W)
	lblinfo.grid(row=7, column=0)
	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10",
	fg="#ED420B", anchor=W)
	lblinfo.grid(row=8, column=3)
	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Tea",
	fg="#ED420B", anchor=W)
	lblinfo.grid(row=8, column=0)
	roo.mainloop()

def clear():
	text.delete(1.0,END)

def quit_fun():
	root.destroy()

def total():
	price1=dringE.get()
	price2=burger_kingE.get()
	price3=cherry.get()
	price4=nacho_fries.get()
	price5=pizza.get()
	price6=biscuits.get()
	price7=roll.get()
	price8=tea.get()

	if price1 != "":
		price1 = int(price1)
	else:
		price1 = 0

	if price2 != "":
		price2 = int(price2)
	else:
		price2 = 0

	if price3 != "":
		price3 = int(price3)
	else:
		price3 = 0

	if price4 != "":
		price4 = int(price4)
	else:
		price4 = 0
	
	if price5 != "":
		price5 = int(price5)
	else:
		price5 = 0

	if price6 != "":
		price6 = int(price6)
	else:
		price6 = 0

	if price7 != "":
		price7 = int(price7)
	else:
		price7 = 0

	if price8 != "":
		price8 = int(price8)
	else:
		price8 = 0

	if price4 != "":
		price4 = int(price4)
	else:
		price4 = 0

	#p1,p2,p3 etc means Price Per Person
	p1=price1*10
	p2=price2*30
	p3=price3*25
	p4=price4*20
	p5=price5*30
	p6=price6*10
	p7=price7*10
	p8=price8*5
	# print("%d %d %d %d %d %d %d %d" %(p1,p2,p3,p4,p5,p6,p7,p8))
	#Cost
	cost=p1+p2+p3+p4+p5+p6+p7+p8
	display=cost
	p1_label["text"]=display
	#Service Tax
	service_charge=cost/20
	service_display=service_charge
	p2_label["text"]=service_display
	#Tax
	tax_charge=int(cost/3)
	tax_display=tax_charge
	p3_label["text"]=tax_charge
	#Sub Total
	sub_total=p1+p2+p3+p4+p5+p6+p7+p8
	sub_display=sub_total
	p4_label["text"]=sub_display
	#Total
	total=display+service_charge+tax_charge
	total_display=total
	p5_label["text"]=total_display
	#Order Number
	num=random.randint(1,10000)
	order_label["text"]=num

def reset():
        global total
        dringE.delete(0,END)
        burger_kingE.delete(0,END)
        cherry.delete(0,END)
        nacho_fries.delete(0,END)
        pizza.delete(0,END)
        biscuits.delete(0,END)
        roll.delete(0,END)
        tea.delete(0,END)
        p1_label["text"]=""
        p2_label["text"]=""
        p3_label["text"]=""
        p4_label["text"]=""
        p5_label["text"]=""
        order_label["text"]=""
def clock():
        current=time.strftime("%H:%M:%S")
        label1 ["text"]=current
        root.after(1000,clock)

root=Tk()
root.geometry("1000x700")
root.minsize(1000,700)
root.maxsize(1000,700)
heading1=Label(root,text="Hotel Net-Tech",font="arial 30 bold",fg="#fc5a03")
heading2=Label(root,text="Management",font="arial 18 bold",fg="#fc5a03")
frame1=Frame(root,height="420",width="330",bd=10,bg=FRAME_ONE_BG_COLOR,highlightthickness=1,relief=SUNKEN)  #ED420B
frame1.place(x=40,y=140)
frame2=Frame(root,height="420",width="330",bd=10,bg=FRAME_TWO_BG_COLOR,highlightthickness=1,relief=SUNKEN)
frame2.place(x=380,y=140)
#Button Frame
frame3=Frame(root,height="100",width="670",bd=10,bg="#ED420B",highlightthickness=1,relief=SUNKEN)
frame3.place(x=40,y=565)
cal_frame=Frame(root,height="500",width="450",bd=10,highlightthickness=1,relief=SUNKEN)
cal_frame.place(x=750,y=150)
text_frame=Frame(root,height="100",width="100")
text_frame.place(x=1000,y=50)

frame_time=Frame(root,height="200",width="200",bd=10,highlightthickness=1,relief=SUNKEN)
frame_time.place(x=750,y=35)
#Price Frame
p1_label=Label(frame2,font="arial 14 bold ",bg=FRAME_TWO_BG_COLOR)
p1_label.place(x=200,y=80)
p2_label=Label(frame2,font="arial 14 bold ",bg=FRAME_TWO_BG_COLOR)
p2_label.place(x=200,y=120)
p3_label=Label(frame2,font="arial 14 bold ",bg=FRAME_TWO_BG_COLOR)
p3_label.place(x=200,y=160)
p4_label=Label(frame2,font="arial 14 bold ",bg=FRAME_TWO_BG_COLOR)
p4_label.place(x=200,y=200)
p5_label=Label(frame2,font="arial 14 bold ",bg=FRAME_TWO_BG_COLOR)
p5_label.place(x=200,y=240)
order_label=Label(frame2,font="arial 14 bold ",bg=FRAME_TWO_BG_COLOR)
order_label.place(x=200,y=40)
text=Text(root,height=10,width=25,bd=10,font="arial 10")
text.insert(END, "Enter Text Here")
text.place(x=750,y=500)
#Time
label1=Label(frame_time,font="article 30",bg="black",fg="#ED420B")
label1.grid(row=0,column=0)
clock()
#Buttons
#Frame 3
new_window=Button(frame3,text="Price",command=price,font="arial 15 bold",bd=10)
new_window.place(x=80,y=10)
total_btn=Button(frame3,text="Total",command=total,font="arial 15 bold",bd=10)
total_btn.place(x=210,y=10)
reset_btn=Button(frame3,text="Reset",command=reset,font="arial 15 bold",bd=10)
reset_btn.place(x=350,y=10)
quit_btn=Button(frame3,text="Quit",command=quit_fun,font="arial 15 bold",bd=10)
quit_btn.place(x=500,y=10)
clear=Button(root,text="Clear",command=clear,font="arial 10 bold",bd=10)
clear.place(x=760,y=450)
#Payment_Entry_Created
#Frame_2

order_number=Label(frame2,text="Order Number",font="arial 12 bold",bg=FRAME_TWO_BG_COLOR)
cost_label=Label(frame2,text="Cost",font="arial 12 bold ",bg=FRAME_TWO_BG_COLOR)
service_tax=Label(frame2,text="Service Cost",font="arial 12 bold",bg=FRAME_TWO_BG_COLOR)
tax=Label(frame2,text="Tax",font="arial 12 bold ",bg=FRAME_TWO_BG_COLOR)
sub_total=Label(frame2,text="Sub Total",font="arial 12 bold",bg=FRAME_TWO_BG_COLOR)
total=Label(frame2,text="Total",font="arial 12 bold ",bg=FRAME_TWO_BG_COLOR)
#Payment_Entry_Close
#Frame_2
order_number.place(x=10,y=40)
cost_label.place(x=10,y=80)
service_tax.place(x=10,y=120)
tax.place(x=10,y=160)
sub_total.place(x=10,y=200)
total.place(x=10,y=240)

#Food_item_Entry_Created
#Frame1_objects
dringE=Entry(frame1,bd="3")
burger_kingE=Entry(frame1,bd="5")
cherry=Entry(frame1,bd="5")
nacho_fries=Entry(frame1,bd="5")
pizza=Entry(frame1,bd="5")
biscuits=Entry(frame1,bd="5")
roll=Entry(frame1,bd="5")
tea=Entry(frame1,bd="5")
#Food_item_Entry_Close
#Frame_1_objects
dringE.place(x=130,y=35)
burger_kingE.place(x=130,y=80)
cherry.place(x=130,y=125)
nacho_fries.place(x=130,y=170)
pizza.place(x=130,y=215)
biscuits.place(x=130,y=260)
roll.place(x=130,y=305)
tea.place(x=130,y=350)
#Food_item_Label_Created
#Frame1_objects
drink_label=Label(frame1,text="Drink",font="arial 12 bold ",bg=FRAME_ONE_BG_COLOR)
burger_king_label=Label(frame1,text="Burger King",font="arial 12 bold",bg=FRAME_ONE_BG_COLOR)
cherry_label=Label(frame1,text="Cherry",font="arial 12 bold",bg=FRAME_ONE_BG_COLOR)
nacho_fries_label=Label(frame1,text="Nacho Fries",font="arial 12 bold",bg=FRAME_ONE_BG_COLOR)
pizza_label=Label(frame1,text="Pizza",font="arial 12 bold ",bg=FRAME_ONE_BG_COLOR)
biscuits_label=Label(frame1,text="Biscuits",font="arial 12 bold",bg=FRAME_ONE_BG_COLOR)
roll_label=Label(frame1,text="Roll",font="arial 12 bold ",bg=FRAME_ONE_BG_COLOR)
tea_label=Label(frame1,text="Tea",font="arial 12 bold ",bg=FRAME_ONE_BG_COLOR)
#Food_item_Label_Close
drink_label.place(x=10,y=35)
burger_king_label.place(x=10,y=80)
cherry_label.place(x=10,y=125)
nacho_fries_label.place(x=10,y=175)
pizza_label.place(x=10,y=215)
biscuits_label.place(x=10,y=260)
roll_label.place(x=10,y=305)
tea_label.place(x=10,y=350)
#-------------------------------------------------------------------------

from tkinter import messagebox
val = ""
A = 0
operator = ""
def btn_1_isclicked():
        global val
        val = val + "1"
        data.set(val)
def btn_2_isclicked():
        global val
        val = val + "2"
        data.set(val)
def btn_3_isclicked():
        global val
        val = val + "3"
        data.set(val)
def btn_4_isclicked():
        global val
        val = val + "4"
        data.set(val)
def btn_5_isclicked():
        global val
        val = val + "5"
        data.set(val)
def btn_6_isclicked():
        global val
        val = val + "6"
        data.set(val)
def btn_7_isclicked():
        global val
        val = val + "7"
        data.set(val)
def btn_8_isclicked():
        global val
        val = val + "8"
        data.set(val)
def btn_9_isclicked():
        global val
        val = val + "9"
        data.set(val)
def btn_0_isclicked():
        global val
        val = val + "0"
        data.set(val)
def btn_plus_isclicked():
        global A
        global operator
        global val
        A = int(val)
        operator = "+"
        val = val + "+"
        data.set(val)
def btn_min_isclicked():
        global A
        global operator
        global val
        A = int(val)
        operator = "-"
        val = val + "-"
        data.set(val)
def btn_mult_isclicked():
        global A
        global operator
        global val
        A = int(val)
        operator = "*"
        val = val + "*"
        data.set(val)

def btn_div_isclicked():
        global A
        global operator
        global val
        A = int(val)
        operator = "/"
        val = val + "/"
        data.set(val)
def btn_c_isclicked():
        global A
        global operator
        global val
        A = 0
        operator = ""
        val = ""
        data.set(val)
def result():
        global A
        global operator
        global val
        val2 = val
        if operator == "+":
                B = int((val2.split("+")[1]))
                C = A + B
                data.set(C)
                val = str(C)
        elif operator == "-":
                B = int((val2.split("-")[1]))
                C = A - B
                data.set(C)
                val = str(C)
        elif operator == "*":
                B = int((val2.split("*")[1]))
                C = A * B
                data.set(C)
                val = str(C)
        elif operator == "/":
                B = int((val2.split("/")[1]))
                if B == 0 :
                        messagebox.showerror("Error","Divisible by 0 not allowed.")
                        A = ""
                        val = ""
                        data.set(val)
                else:
                        C = int(A / B)
                        data.set(C)
                        val = str(C)

data = StringVar()
lbl = Label(cal_frame,text="LABEL",anchor=SE,
font=("Verdana", 20),
textvariable=data,
background="#ffffff",
fg="#000000"
)
lbl.pack(expand=True, fill="both")
btnrow1 = Frame(cal_frame, bg="#000000")
btnrow1.pack(expand=True, fill="both")
btnrow2 = Frame(cal_frame)
btnrow2.pack(expand=True, fill="both")
btnrow3 = Frame(cal_frame)
btnrow3.pack(expand=True, fill="both")
btnrow4 = Frame(cal_frame)
btnrow4.pack(expand=True, fill="both")
btn1 = Button(btnrow1,text="1",font=("Verdana", 22),relief=GROOVE,border=0,command=btn_1_isclicked)
btn1.pack(side=LEFT, expand=True, fill="both")
btn2 = Button(btnrow1,text="2",font=("Verdana", 22),relief=GROOVE,border=0,command=btn_2_isclicked)
btn2.pack(side=LEFT, expand=True, fill="both")
btn3 = Button(btnrow1,text="3",font=("Verdana", 22),relief=GROOVE,border=0,command=btn_3_isclicked)
btn3.pack(side=LEFT, expand=True, fill="both")
btnplus = Button(btnrow1,text="+",font=("Verdana", 22),relief=GROOVE,border=0,command=btn_plus_isclicked)
btnplus.pack(side=LEFT, expand=True, fill="both")
btn4 = Button(btnrow2,text="4",font=("Verdana", 22),relief=GROOVE,border=0,command=btn_4_isclicked)
btn4.pack(side=LEFT, expand=True, fill="both")
btn5 = Button(btnrow2,text="5",font=("Verdana", 22),relief=GROOVE,border=0,command=btn_5_isclicked)
btn5.pack(side=LEFT, expand=True, fill="both")
btn6 = Button(btnrow2,text="6",font=("Verdana", 22),relief=GROOVE,border=0,command=btn_6_isclicked)
btn6.pack(side=LEFT, expand=True, fill="both")
btnminus = Button(btnrow2,text="-",font=("Verdana", 22),relief=GROOVE,border=0,command=btn_min_isclicked)
btnminus.pack(side=LEFT, expand=True, fill="both")
btn7 = Button(btnrow3,text="7",font=("Verdana", 22),relief=GROOVE,border=0,command=btn_7_isclicked)
btn7.pack(side=LEFT, expand=True, fill="both")
btn8 = Button(btnrow3,text="8",font=("Verdana", 22),relief=GROOVE,border=0,command=btn_8_isclicked)
btn8.pack(side=LEFT, expand=True, fill="both")
btn9 = Button(btnrow3,text="9",font=("Verdana", 22),relief=GROOVE,border=0,command=btn_9_isclicked)
btn9.pack(side=LEFT, expand=True, fill="both")
btnmult = Button(btnrow3,text="*",font=("Verdana", 22),relief=GROOVE,border=0,command=btn_mult_isclicked)
btnmult.pack(side=LEFT, expand=True, fill="both")
btnc = Button(btnrow4,text="C",font=("Verdana", 22),relief=GROOVE,border=0,command=btn_c_isclicked)
btnc.pack(side=LEFT, expand=True, fill="both")
btn0 = Button(btnrow4,text="0",font=("Verdana", 22),relief=GROOVE,border=0,command=btn_0_isclicked)
btn0.pack(side=LEFT, expand=True, fill="both")
btnequal = Button(btnrow4,text="=",font=("Verdana", 22),relief=GROOVE,border=0,command=result)
btnequal.pack(side=LEFT, expand=True, fill="both")
btndiv = Button(btnrow4,text="/",font=("Verdana", 22),relief=GROOVE,border=0,command=btn_div_isclicked)
btndiv.pack(side=LEFT, expand=True, fill="both")
heading1.place(x=250,y=10)
heading2.place(x=300,y=80)
root.mainloop()