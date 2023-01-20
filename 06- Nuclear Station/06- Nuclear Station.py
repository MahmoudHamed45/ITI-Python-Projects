from playsound import playsound
from tkinter import *
import tkinter as tk
import time
import os
import datetime as dt
import math
import random

window_1 = Tk() 
window_1.title("Nuclear Station")
window_1.geometry('400x350')
window_2=0
# declaring string variable
# for storing name and password
name_var=StringVar()
passw_var=StringVar()
reactorPhoto=0  #The variable photo is a local variable which gets garbage collected after the class is instantiated. Save a reference to the photo

weather=['Rainy', 'Mild', 'Cold', 'Dry', 'Hot', 'Windy']
frameCnt = 5
frames = [PhotoImage(file='explosion.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def submit():
    name=name_var.get()
    password=passw_var.get()
    name_var.set("")
    passw_var.set("")

    if name == "M" and password == "123":
        operationWindow()
    else:
        indicationLabel["text"]='Wrong Username or Password'

def operationWindow():
    global window_2
    window_2 = Toplevel(window_1)
    window_2.title("Nuclear Operation")
    window_2.geometry("600x600")
    explosionButton= Button(window_2, text= "Don't Press Me", command= explosion)
    explosionButton.place(x=0, y=0)
    tempButton= Button(window_2, text= "Temp", command= temp)
    tempButton.place(x=0, y=100)
    dayButton= Button(window_2, text= "Day", command=day)
    dayButton.place(x=0, y=200)
    humidButton= Button(window_2, text= "Humid", command=humid)
    humidButton.place(x=0, y=300)
    global reactorPhoto
    reactorPhoto = PhotoImage(file='reactor.png')
    reactorPhoto = reactorPhoto.subsample(8,8)
    photoLabel=Label(window_2, image= reactorPhoto)
    photoLabel.place(x=100, y=0)

        
def explosion():
    global window_2
    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label.configure(image=frame)
        window_2.after(100, update, ind)
    label = Label(window_2)
    label.grid(row=4, column=1)
    window_2.after(0, update, 0)
    playsound('explode.mp3')

def temp():
    arc_w= 80
    x1, y1 , x2, y2 = 40,40,560,560
    x , y , r = 300, 295, 220
    window_3 = Toplevel(window_2)
    window_3.title("Temperature")
    window_3.geometry("600x600")
    myCanvas = tk.Canvas(window_3, bg="white", height=300, width=600)
    myCanvas.grid(row=0, column=0)
    myCanvas.create_arc(x1, y1,x2,y2, start=0, extent=45,outline='red',
         width=arc_w,style=tk.ARC)
    myCanvas.create_arc(x1, y1,x2,y2, start=45, extent=45,outline='yellow', 
            width=arc_w,style=tk.ARC)
    myCanvas.create_arc(x1, y1,x2,y2, start=90, extent=30,outline='green', 
            width=arc_w,style=tk.ARC)
    myCanvas.create_arc(x1, y1,x2,y2, start=120, extent=60,outline='blue',
            width=arc_w,style=tk.ARC)
    myCanvas.create_oval(x-10,y-10,x+10,y+10,fill='blue')
    in_radian=math.radians(random.randint(0, 180))
    pointer=myCanvas.create_line(x,y, (x+r*math.cos(in_radian)), (y-r*math.sin(in_radian)), width=6 , arrow='last')
    label_temp= Label(window_3, text=("Temperature =" + str(int(3000*math.pi-in_radian*3000)) + " C"))
    label_temp.grid(row=1, column=0)

def day():
    global weather
    window_4 = Toplevel(window_2)
    window_4.title("day")
    window_4.geometry("600x600")
    date = dt.datetime.now()
    # Create Label to display the Date
    label_date = Label(window_4, text=f"{date:%A, %B %d, %Y}", font="Calibri, 10")  
    label_date.pack(pady=20)
    Label_weather= Label(window_4, text=("Weather is " + random.choice(weather)), font="Calibri, 10")  
    Label_weather.pack(pady=20)

def humid():
    window_5 = Toplevel(window_2)
    window_5.title("Humidity")
    window_5.geometry("600x600")
    Label_humid= Label(window_5, text=("Humidity is " + str(random.randint(0,30)) + '%'), font="Calibri, 10")  
    Label_humid.pack(pady=20)   


    
submitButton = Button(window_1, text= "Submit", command = submit)
submitButton.grid(row=2, column=0)
exitButton = Button(window_1, text= "Exit", command = window_1.destroy)
exitButton.grid(row=2, column=1)

usernameLabel = Label(window_1, text="User Name")
usernameLabel.grid(row=0, column=0)
E1 = Entry(window_1, bd =5, textvariable = name_var)
E1.grid(row=0, column=1)

passwordLabel = Label(window_1, text="User Name")
passwordLabel.grid(row=1, column=0)
E1 = Entry(window_1, bd =5,textvariable = passw_var, show= '*')
E1.grid(row=1, column=1)

indicationLabel= Label(window_1, text="")
indicationLabel.grid(row=4, column=1, rowspan=5)
passLabel= Label(window_1, text="username =M   pass =123")
passLabel.place(x=0, y=100)
reactorPhoto = PhotoImage(file='reactor.png')
reactorPhoto = reactorPhoto.subsample(8,8)
photoLabel=Label(window_1, image= reactorPhoto)
photoLabel.place(x=0, y=200)






window_1.mainloop() 