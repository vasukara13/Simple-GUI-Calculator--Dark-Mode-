from tkinter import *
import math
counter=0 # variable to check for clear button
equation=[] # where the input is stored
root=Tk()
root.title('Calculator')
root.resizable(0, 1)

def factorial(): # function to calculate the factorial
    global counter
    global equation
    e=''.join(equation)
    l = len(e)
    prd=1
    num = int(e[:l - 1])
    for i in range(1,num+1):
        prd=prd*i
    counter=1
    return prd

def result():   # function to display the result
    global counter
    global equation
    try:
        equation=''.join(equation)
        b = eval(equation)
        root.display.delete(0,END)
        if math.ceil(b)==b:
            b=int(b)
            root.display.insert(0,b)
            counter=1
        else:
            counter=1
            root.display.insert(0, b)

    except:
        counter=1
        root.display.delete(0,END)
        root.display.insert(0,"Invalid")


def entryDisplay(txt):#im getting bored commenting here,anyway to display the input on screen
    global equation
    global counter
    if counter==1:
        clearText()
        counter=0
    if txt == "=":
        eq=root.display.get()
        if eq.endswith("!"):
            f=factorial()
            root.display.delete(0,END)
            root.display.insert(0,f)

        else:
            result()
    else:
        if txt=="ˆ":
            equation.append("**")
        else:
            equation.append(txt)
        rn=str(root.display.get())
        root.display.delete(0, END)
        root.display.insert(0,rn+txt)


def backspace():# delete last entered character
    txt = root.display.get()[:-1]
    print(txt)
    # clear the widget of text
    root.display.delete(0,END)
    # insert the new string, sans the last character
    root.display.insert(0, txt)


def clearText(): # to clear the entry display
    global counter
    global equation
    equation=[]
    counter=0
    root.display.delete(0,END)


def createWidgets(self):# display buttons
    self.display = Entry(self,font=("Times", 17), borderwidth=0, relief=RAISED, justify=RIGHT,bg='black',fg='white',width=25)
    self.display.grid(row=0, column=0, columnspan=5)
    self.sevenButton = Button(self, font=("Times", 13,"bold"), text="7", borderwidth=0,command=lambda: entryDisplay("7"),bg="black",fg="white")
    self.sevenButton.grid(row=1, column=0, sticky="NWNESWSE")
    self.eightButton = Button(self, font=("Times", 13,"bold"), text="8", borderwidth=0,command=lambda: entryDisplay("8"),bg="black",fg="white")
    self.eightButton.grid(row=1, column=1, sticky="NWNESWSE")
    self.nineButton = Button(self, font=("Times", 13,"bold"), text="9", borderwidth=0, command=lambda: entryDisplay("9"),bg="black",fg="white")
    self.nineButton.grid(row=1, column=2, sticky="NWNESWSE")
    self.timesButton = Button(self, font=("Times", 13,"bold"), text="*", borderwidth=0, command=lambda: entryDisplay("*"),bg="black",fg="white")
    self.timesButton.grid(row=1, column=3, sticky="NWNESWSE")
    self.clearButton = Button(self, font=("Times", 13,"bold"), text="C", borderwidth=0, command=lambda: clearText(),bg="black",fg="white")
    self.clearButton.grid(row=2, column=4, sticky="NWNESWSE")
    #Second Row
    self.fourButton = Button(self, font=("Times", 13,"bold"), text="4", borderwidth=0,command=lambda: entryDisplay("4"),bg="black",fg="white")
    self.fourButton.grid(row=2, column=0, sticky="NWNESWSE")
    self.fiveButton = Button(self, font=("Times", 13,"bold"), text="5", borderwidth=0, command=lambda: entryDisplay("5"),bg="black",fg="white")
    self.fiveButton.grid(row=2, column=1, sticky="NWNESWSE")
    self.sixButton = Button(self, font=("Times", 13,"bold"), text="6", borderwidth=0, command=lambda: entryDisplay("6"),bg="black",fg="white")
    self.sixButton.grid(row=2, column=2, sticky="NWNESWSE")
    self.divideButton = Button(self, font=("Times", 13,"bold"), text="/", borderwidth=0, command=lambda: entryDisplay("/"),bg="black",fg="white")
    self.divideButton.grid(row=2, column=3, sticky="NWNESWSE")
    self.percentageButton = Button(self, font=("Times", 15), text="%", borderwidth=0, command=lambda:entryDisplay("%"),fg="white",bg="black")
    self.percentageButton.grid(row=5, column=2, sticky="NWNESWSE")
    self.backspaceButtom = Button(self,font=("Times",15),text="<",borderwidth=0,fg="white",bg="black",command=lambda :backspace())
    self.backspaceButtom.grid(row=1,column=4,sticky="NWNESWSE")
    self.powerButton=Button(self,text="ˆ",borderwidth=0,font=("Times",16,"bold"),command=lambda:entryDisplay("ˆ"),fg="white",bg="black",)
    self.powerButton.grid(row=5,column=0,sticky="NWNESWSE",columnspan=2)
    self.factorialButton=Button(self,text="!",font=("Times",14),command=lambda : entryDisplay("!"),borderwidth=0,fg="white",bg="black")
    self.factorialButton.grid(row=5,column=3,sticky="NWNESWSE")
    self.oneButton = Button(self, font=("Times", 13,"bold"), text="1", borderwidth=0, command=lambda: entryDisplay("1"),bg="black",fg="white")
    self.oneButton.grid(row=3, column=0, sticky="NWNESWSE")
    self.twoButton = Button(self, font=("Times", 13,"bold"), text="2", borderwidth=0, command=lambda: entryDisplay("2"),bg="black",fg="white")
    self.twoButton.grid(row=3, column=1, sticky="NWNESWSE")
    self.threeButton = Button(self, font=("Times", 13,"bold"), text="3", borderwidth=0, command=lambda: entryDisplay("3"),bg="black",fg="white")
    self.threeButton.grid(row=3, column=2, sticky="NWNESWSE")
    self.minusButton = Button(self, font=("Times", 13,"bold"), text="-", borderwidth=0, command=lambda: entryDisplay("-"),bg="black",fg="white")
    self.minusButton.grid(row=3, column=3, sticky="NWNESWSE")
    self.equalsButton = Button(self, font=("Times", 16,"bold"), text="=", borderwidth=0, command=lambda: entryDisplay("="),bg="black",fg="white")
    self.equalsButton.grid(row=3, column=4,sticky="NWNESWSE", rowspan=4)
    self. zeroButton = Button(self, font=("Times", 13,"bold"), text="0", borderwidth=0, command=lambda: entryDisplay("0"),bg="black",fg="white")
    self.zeroButton.grid(row=4, column=0, columnspan=2, sticky="NWNESWSE")
    self.dotButton = Button(self, font=("Times", 13,"bold"), text=".", borderwidth=0, command=lambda: entryDisplay("."),bg="black",fg="white")
    self.dotButton.grid(row=4, column=2, sticky="NWNESWSE")
    self.plusButton = Button(self, font=("Times", 13,"bold"), text="+", borderwidth=0, command=lambda: entryDisplay("+"),bg="black",fg="white")
    self.plusButton.grid(row=4, column=3, sticky="NWNESWSE")
createWidgets(root)
root.mainloop()# run the program
