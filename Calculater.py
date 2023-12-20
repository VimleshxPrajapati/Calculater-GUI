# Calculater
from tkinter import *
from math import *
v=0
def btnClick(number):
    global val
    if v%2==1:
      val = val + str(number)
      data.set(val)
def btnon():
    global v
    v=v+1
    if v%2==1:
        data.set("")
        btn_re["text"]="ON"
    else:
        btn_re["text"]="OFF"
        data.set("")

def name():
    data.set("____Coded By Vi____")

def btnClear():
    global val
    val = ""
    data.set("")

def trigOP(st):
    global val
    if v%2==1:
      val=val+st
      data.set(val)

def btnEqual():
    global val
    if v%2==1:
      result = str(eval(val))
      data.set(result)

def btnBack():
     global val
     val=data.get()
     val=val[:-1]
     data.set(val)



root = Tk()
root.title("Vi Calculater")
root.geometry("451x551+500+200")
val = ""
data = StringVar()
display = Entry(root, textvariable=data, bd=29, bg="Powderblue", justify="right", font=("ariel", 20))

# Border
display.grid(row=0, columnspan=5,sticky=NSEW)
# first row__________________________________________________
btn7 = Button(root, text="7", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(7))
btn7.grid(row=1, column=0)
btn8 = Button(root, text="8", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(8))
btn8.grid(row=1, column=1)
btn9 = Button(root, text="9", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(9))
btn9.grid(row=1, column=2)
btn_add = Button(root, text="+", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick("+"))
btn_add.grid(row=1, column=3)
btnsin = Button(root, text="sin", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda:trigOP("sin"))
btnsin.grid(row=1, column=4)
# second row_________________________________________________
btn4 = Button(root, text="4", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(4))
btn4.grid(row=2, column=0)
btn5 = Button(root, text="5", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(5))
btn5.grid(row=2, column=1)
btn6 = Button(root, text="6", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(6))
btn6.grid(row=2, column=2)
btn_sub = Button(root, text="-", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick("-"))
btn_sub.grid(row=2, column=3)
btncos = Button(root, text="cos", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda:trigOP("cos"))
btncos.grid(row=2, column=4)
# three row___________________________________________________
btn1 = Button(root, text="1", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(1))
btn1.grid(row=3, column=0)
btn2 = Button(root, text="2", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(2))
btn2.grid(row=3, column=1)
btn3 = Button(root, text="3", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(3))
btn3.grid(row=3, column=2)
btn_mul = Button(root, text="*", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick("*"))
btn_mul.grid(row=3, column=3)
btntan = Button(root, text="tan", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: trigOP("tan"))
btntan.grid(row=3, column=4)
# Forth row___________________________________________________
btn0 = Button(root, text="0", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(0))
btn0.grid(row=4, column=0)
btn_C = Button(root, text="C", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClear())
btn_C.grid(row=4, column=1)
btn_E = Button(root, text="=", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnEqual())
btn_E.grid(row=4, column=2)
btn_div = Button(root, text="/", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick("/"))
btn_div.grid(row=4, column=3)
btn_lp = Button(root, text="(", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick("("))
btn_lp.grid(row=4, column=4)
# Fifth row___________________________________________________
btn_exp = Button(root, text="Exp", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick("**"))
btn_exp.grid(row=5, column=0)
btn_fdiv = Button(root, text="//", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick("//"))
btn_fdiv.grid(row=5, column=1)
btndt = Button(root, text=".", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick("."))
btndt.grid(row=5, column=2)
btn_back = Button(root, text="Del", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda:btnBack())
btn_back.grid(row=5, column=3)
btn_rp = Button(root, text=")", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(")"))
btn_rp.grid(row=5, column=4)
# Sixth row___________________________________________________
btn_rem = Button(root, text="%", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick("%"))
btn_rem.grid(row=6, column=0)
btn_re = Button(root, text="SWITCH", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnon())
btn_re.grid(row=6, column=1)
btn_re1 = Button(root, text="Coded By Vi", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: name())
btn_re1.grid(row=6, column=2,columnspan=3,sticky=NSEW)
root.mainloop()

