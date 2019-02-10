import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
 
window = Tk()
window.geometry('450x300')
window.title("CompoundInterest Graphical Viewer")
 
lbl = Label(window, text="Enter current loan amount: ")
lbl.grid(column=0, row=0)

lbl2 = Label(window, text="Enter loan apr: ")
lbl2.grid(column=0, row=1)

lbl3 = Label(window, text="How many months graphed?: ")
lbl3.grid(column=0, row=2)

rlbl1 = Label(window, text=" # of months calculated ")
rlbl1.grid(column=1, row=4)

rlbl2 = Label(window, text=" delta: ")
rlbl2.grid(column=1, row=5)

rlbl3 = Label(window, text=" delta/months: ")
rlbl3.grid(column=1, row=6)


 
txt = Entry(window,width=10)
txt.grid(column=1, row=0)

txt2 = Entry(window,width=10)
txt2.grid(column=1, row=1)

txt3 = Entry(window,width=10)
txt3.grid(column=1, row=2)


def do_plotgraph(xaxis,compoundingint,justinterest):

    plt.plot(xaxis, compoundingint, 'ro')
    plt.xlabel('Time in Months')
    plt.ylabel('Cost in Dollars')
    plt.show()

    

def compound_interest(principle, rate, time): 


    array_xaxis = [0]
    array_just_interest = [0.00]
    array_compounding_int = [principle]
    


    for t in range(time):
            
        # Calculates compound interest  
        myNewAccruedInterest = (principle * (rate / 100))/12 
        mySubTotal = principle + myNewAccruedInterest
        print("mySub: ", myNewAccruedInterest)
        print("t is: ", [t+1])
        array_xaxis.append(int(t+1))
        principle = mySubTotal
        array_just_interest.append(float(myNewAccruedInterest))
        array_compounding_int.append(float(mySubTotal))




    print (array_xaxis)
    print (array_just_interest)
    print (array_compounding_int)
    doresults(array_xaxis,array_compounding_int,array_just_interest)
    do_plotgraph(array_xaxis,array_compounding_int,array_just_interest)
  
    
    

  


def clicked():
    principalLoan_f = float(txt.get())
    loanApr_f = float(txt2.get())
    monthsGraph_i = int(txt3.get())
    principalLoan = txt.get()
    loanApr = txt2.get()
    monthsGraph = txt3.get()
 
    lbl.configure(text = "Principal Loan is: " + principalLoan)
    lbl2.configure(text = "Loan APR is: " + loanApr)
    lbl3.configure(text = "Graph Month length is: " + monthsGraph)

    # Compute Code 
    compound_interest(principalLoan_f, loanApr_f, monthsGraph_i) 

def doresults(xaxis,compoundingint,justinterest):
    end= len(xaxis)-1
    x = str(xaxis[end])
    y = str('${:,.2f}'.format((compoundingint[end]-compoundingint[0])))
    z = str('${:,.2f}'.format((compoundingint[end]-compoundingint[0])/end))
    print("x: ", x)
    print("y: ", y)
    print("z: ", z)


    rlbl1.configure(text = "# of months: "+ x)
    rlbl2.configure(text = "loan Delta: "+ y)
    rlbl3.configure(text = "avg Delta/ #months: "+ z)




btn = Button(window, text="Click Me", bg="blue", fg="white", command=clicked)
btn.grid(column=4, row=1)

window.mainloop()




