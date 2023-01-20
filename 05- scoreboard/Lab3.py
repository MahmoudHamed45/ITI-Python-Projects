# from tkinter import *
# def func():
#     print("Hossam")
#     label2 = Label(window_1 , text = "Mahmoud")
#     label2.pack(side = TOP)
# window_1 = Tk() 
# window_1.title("Hello From Tkinter ")
# labelx  =Label(window_1 , text = "Mahmoud")
# labelx.pack(side = BOTTOM)
# b1 = Button(window_1, text= "ITI", command= func)
# b1.pack(side = TOP)
# b2 = Button(window_1, text= "RIGHT")
# b2.pack(side = RIGHT)
# b3 = Button(window_1, text= "LEFT")
# b3.pack(side = LEFT)
# b4 = Button(window_1, text= "BOTTOM")
# b4.pack(side = BOTTOM)
# b5 = Button(window_1, text= "HAHA")
# b5.pack(side = BOTTOM)
# window_1.geometry('600x500')
# window_1.mainloop()

#====================================================================================================
# x=0
# from tkinter import *
# def func():
#     print("Hossam")
#     global x
#     global label2
#     if x==0:
#         label2
#         label2= Label(window_1 , text = "Hossam")
#         label2.pack(side = TOP)
#         x=1
#     else:
#         label2= Label(window_1 , text = "Mahmoud")
#         label2.pack(side = TOP)
#         x=0
# window_1 = Tk() 
# window_1.title("Hello From Tkinter ")
# labelx  =Label(window_1 , text = "Mahmoud")
# labelx.pack(side = BOTTOM)
# label2 = Label(window_1 , text = "Mahmoud")
# label2.pack(side = TOP)
# b1 = Button(window_1, text= "ITI", command= func)
# b1.pack(side = TOP)
# b2 = Button(window_1, text= "RIGHT")
# b2.pack(side = RIGHT)
# b3 = Button(window_1, text= "LEFT")
# b3.pack(side = LEFT)
# b4 = Button(window_1, text= "BOTTOM", bd= '10', background='red', fg= 'green')
# b4.pack(side = BOTTOM)
# photo_1 = PhotoImage(file ='iti-logo.png')
# photo_1 = photo_1.subsample(2,2)
# b5 = Button(window_1, image=photo_1, text= "HAHA")
# b5.pack(side = BOTTOM)
# window_1.geometry('600x500')
# window_1.mainloop()

#=========================================================
# from tkinter import *
# window_1 = Tk() 
# window_1.title("Hello From Tkinter ")
# x=0
# y=0
# flag=0
# b7 = Button(window_1, text= "7", width=5, height=2)
# b7.place(x=50, y=150)
# b8 = Button(window_1, text= "8", width=5, height=2)
# b8.place(x=100, y=150)
# b9 = Button(window_1, text= "9", width=5, height=2)
# b9.place(x=150, y=150)
# b4 = Button(window_1, text= "4", width=5, height=2)
# b4.place(x=50, y=200)
# b5 = Button(window_1, text= "5", width=5, height=2)
# b5.place(x=100, y=200)
# b6 = Button(window_1, text= "6", width=5, height=2)
# b6.place(x=150, y=200)
# b1 = Button(window_1, text= "1", width=5, height=2)
# b1.place(x=50, y=250)
# b2 = Button(window_1, text= "2", width=5, height=2)
# b2.place(x=100, y=250)
# b3 = Button(window_1, text= "3", width=5, height=2)
# b3.place(x=150, y=250)
# be = Button(window_1, text= "=", width=5, height=2)
# be.place(x=50, y=300)
# bp = Button(window_1, text= "+", background='red', width=5, height=2)
# bp.place(x=100, y=300)
# bm = Button(window_1, text= "-", background='red', width=5, height=2)
# bm.place(x=150, y=300)
# bd = Button(window_1, text= "/",background='green', width=5, height=2)
# bd.place(x=100, y=350)
# bM = Button(window_1, text= "*",background='green', width=5, height=2)
# bM.place(x=150, y=350)
# window_1.geometry('600x500')
# window_1.mainloop()
#=================================================================================
#Problem in Time Display
from tkinter import *
import time
import os
import threading as th
import datetime as dt
# def sctn():  
#     label5["text"]=str(time.time())
# S = th.Timer(1/60, sctn)  
# S.start()  
# S.cancel()

x=0
y=0
t=0
def incrM():
    global x
    x+=1
    label3["text"]=str(x)
    return
def incrC():
    global y
    y+=1
    label4["text"]=str(y)
    return
def Reset():
    global y
    global x
    y=0
    x=0
    label4["text"]=str(0)
    label3["text"]=str(0)
    return
window_1 = Tk() 
window_1.title("Hello From Tkinter ")

b2 = Button(window_1, text= "increment", command=incrC)
b2.pack(side = RIGHT)
b3 = Button(window_1, text= "increment", command=incrM)
b3.pack(side = LEFT)
b3 = Button(window_1, text= "Reset", command=Reset)
b3.pack(side = BOTTOM)
photo_1 = PhotoImage(file ='Morocco.png')

photo_1 = photo_1.subsample(7,7)
photo_2 = PhotoImage(file ='640px-Flag_of_Croatia.png')
photo_2 = photo_2.subsample(5,5)
label1  =Label(window_1 , text = "Morroco", image=photo_1)
label1.pack(side = LEFT)
label2 = Label(window_1 , text = "Croatia", image=photo_2)
label2.pack(side = RIGHT)
label3  =Label(window_1 , text = "0")
label3.place(x=0 , y=400)
label4  =Label(window_1 , text = "0")
label4.place(x=450 , y=400)
label5  =Label(window_1 , text = str(t))

date = dt.datetime.now()
# Create Label to display the Date
label8 = Label(window_1, text=f"{date:%A, %B %d, %Y}", font="Calibri, 10")
label8.pack(pady=20)


from time import strftime
def my_time():
    time_string = strftime('%H:%M:%S %p') # time format 
    l1.config(text=time_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds 
l1=Label(window_1,bg='blue')
l1.pack(pady=20)
my_time()


startTime = time.time()
Mins= 0
Hr=0
Seconds=0
def stopwatch():
    global startTime, Mins, Hr, Seconds
    Seconds+=1
    if Seconds == 60:
        Seconds = 0
        Mins+=1
    if Mins == 60:
        Mins= 0
        Seconds=0
        Hr+=1 
    stopW= str(Hr) + ':'+ str(Mins)+ ':' + str(Seconds)
    l3.config(text=stopW)
    l1.after(1000,stopwatch)
l3=Label(window_1,bg='blue')
l3.pack(pady=20)    
stopwatch()



label5.pack(side= BOTTOM)
window_1.geometry('600x500')

window_1.mainloop()
