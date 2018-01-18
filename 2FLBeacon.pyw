#!/usr/bin/env python
import os
import datetime
import time
import subprocess
#from configparser import ConfigParser
import six
if six.PY2:
    import ConfigParser as configparser
else:
    import configparser
from Tkinter import*
from subprocess import call
from sys import executable


window = Tk()
#Top = Tk ()
dt = str(datetime.datetime.now())


parser = configparser.ConfigParser()
parser.read('FLBeacon.conf')

print(parser.get('MessageConfig', 'Callsign1'))
print(parser.get('MessageConfig', 'Callsign2'))
print(parser.get('MessageConfig', 'Message'))
print(parser.getint('MessageConfig', 'timer'))

callsign1Get = (parser.get('MessageConfig', 'Callsign1'))
callsign2Get = (parser.get('MessageConfig', 'Callsign2'))
messageGet = (parser.get('MessageConfig', 'message'))
timerGet = (parser.getint('MessageConfig', 'timer'))
label1 = Label(window,text = "Beacon is not running")
label1.configure(bg='red')
label1.place(x= 350, y=10, width=150)
label = Label(window,text = "Current Beacon Settings :")
label.configure(bg='yellow')
label.place(x= 50, y=10)
label = Label(window, text="Your Callsign :"+callsign1Get)
label.configure(bg='Yellow')
label.place(x=50, y=27)
label = Label(window, text="To Callsign :"+callsign2Get)
label.configure(bg='Yellow')
label.place(x=50, y=42)
label = Label(window, text="Message :"+messageGet)
label.configure(bg='Yellow')
label.place(x=50, y=57)
label = Label(window, text="Beacon Timer :"+ str (timerGet))
label.configure(bg='Yellow')
label.place(x=50, y=72)

full_message=StringVar()
full_message=("current beacon :"+callsign2Get+" "+callsign2Get+" DE "+callsign1Get+" "+callsign1Get+" "+messageGet)





C1in = StringVar()
C2in = StringVar()
messageValue = StringVar()
beacontimerin = StringVar()
C1 = None
C2 = None
messageout = None 
beacontimer = None

window.title("FLBeacon")
window.geometry("600x600+200+50")
window.configure(bg="blue")
label = Label(window,text = "Update beacon settings in the boxes below")
label.configure(bg='yellow')
label.place(x= 50, y=125)

Beacon=[]
#From Callsign Entry
label = Label(window, text="Your Callsign")
label.configure(bg='Yellow')
label.place(x=50, y=170)
entry_box1=Entry(window,textvariable=C1in)
entry_box1.place(x=140,y=170, width=75)

# To Callsign Entry
label = Label(window, text="To Callsign")
label.configure(bg='Yellow')
label.place(x=50, y=210)
entry_box2=Entry(window,textvariable=C2in)
entry_box2.place(x=127,y=210, width=75)

# Beacon Timer Entry
label = Label(window, text="Beacon Timer in seconds")
label.configure(bg='Yellow')
label.place(x=210, y=210)
entry_box4=Entry(window,textvariable=beacontimerin)
entry_box4.place(x=380,y=210, width=75)


#Message  Entry
label = Label(window, text="25 char Message")
label.configure(bg='Yellow')
label.place(x=50, y=250)

def limitSizeMessage(*args):
    value = messageValue.get()
    if len(value) > 25: messageValue.set(value[:25])

messageValue = StringVar()
messageValue.trace('w', limitSizeMessage)

entry_box3=Entry(window,textvariable=messageValue)
entry_box3.place(x=168, y=250, width=210)

# Function

def enter():
    global C1in, C2in, messageValue,beacontimer, newbeaconVal  
    C1 = C1in.get()
    C2 = C2in.get()
    messageout = messageValue.get()
    beacontimer = beacontimerin.get()
    #print C1
    #print C2
    #print messageout
    #print beacontimer
    parser = configparser.ConfigParser()

    parser.add_section('MessageConfig') 
    parser.set('MessageConfig', 'Callsign1', C1)
    parser.set('MessageConfig', 'Callsign2', C2)
    parser.set('MessageConfig', 'Message', messageout)
    parser.set('MessageConfig', 'Timer', beacontimer)

    parser.write(sys.stdout)
    with open('FLBeacon.conf', 'w') as configfile:
       parser.write(configfile)
    parser.read('FLBeacon.conf')
    callsign1Get = (parser.get('MessageConfig', 'Callsign1'))
    callsign2Get = (parser.get('MessageConfig', 'Callsign2'))
    messageGet = (parser.get('MessageConfig', 'message'))
    timerGet = (parser.getint('MessageConfig', 'timer'))
    label1 = Label(window,text = "Beacon is not running")
    label1.configure(bg='red')
    label1.place(x= 350, y=10, width=150)
    label = Label(window,text = "Current Beacon Settings :")
    label.configure(bg='yellow')
    label.place(x= 50, y=10)
    label = Label(window, text="Your Callsign :"+callsign1Get)
    label.configure(bg='Yellow')
    label.place(x=50, y=27)
    label = Label(window, text="To Callsign :"+callsign2Get)
    label.configure(bg='Yellow')
    label.place(x=50, y=42)
    label = Label(window, text="Message :"+messageGet)
    label.configure(bg='Yellow')
    label.place(x=50, y=57)
    label = Label(window, text="Beacon Timer :"+ str (timerGet))
    label.configure(bg='Yellow')
    label.place(x=50, y=72)
    global full_message
    full_message=StringVar()
    full_message=("current beacon :"+callsign2Get+" "+callsign2Get+" DE "+callsign1Get+" "+callsign1Get+" "+messageGet)
    clear_msg()
   
proc = None
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func 
def turnOff():
    global proc
    if proc is not None:
        print('Beacon Stopped')
        proc.terminate()
        proc = None
        label1 = Label(window,text = "Beacon is not running")
        label1.configure(bg='red')
        label1.place(x= 350, y=10, width=150)
        label2.destroy()


def turnOn():
    global proc
    if proc is None:
        window.after(50000,file_chk)
        print('Starting Beacon')
        proc = subprocess.Popen(["python3", "/home/pi/FLBeacon/FLBeaconout.py"])
        label1 = Label(window,text ="Beacon is Running")
        label1.configure(bg='green')
        label1.place(x= 350, y=10, width=150)
        global  label2
        label2 = Label(window,text = full_message)
        label2.configure(bg='green')
        label2.place(x=50, y=90, width=550)
        file_chk()
        
def file_chk():
            PATH='./FLBeaconReceived.txt'
            if os.path.isfile(PATH):
               print("file has been found")
               file = open("FLBeaconReceived.txt")
               data = file.read()
               file.close()
               global T
               T = Text(window, height=6, width=70)
               T.insert(INSERT,data)
               T.place(x = 50, y = 365)
               Results = Label(window,text = "Incoming Message")
               Results.place(x = 50, y = 350)
               turnOff() 
               label1 = Label(window,text = "Beacon is not running")
               label1.configure(bg='red')
               label1.place(x= 350, y=10, width=150)
               label2.destroy()
               return
            else:
              print("there is no file")
              window.after(50000,file_chk)
              
              
          
            
            
            


       
on = Button(window, borderwidth=2, text = "Start Beacon", width=15, pady=5, command = turnOn)
off = Button(window, borderwidth=2, text = "Stop Beacon", width=15, pady=5, command = turnOff)
on.place(x=215,y=300)
off.place(x=380,y=300)
def clear_msg(): 
        newname = 'file_'+dt+'.txt'
        os.rename('FLBeaconReceived.txt',newname)
        T.destroy()
        window.update()
        print('window updated')



def stop():
        PATH='./FLBeaconReceived.txt'
        if os.path.isfile(PATH):
           newname = 'file_'+dt+'.txt'
           os.rename('FLBeaconReceived.txt',newname)
           window.destroy()
        else: 
           window.destroy()
 

b = Button(window, borderwidth=2, text="Update Beacon", width=15, pady=5, command=enter)
b.place(x=50,y=300)
b = Button(window, borderwidth=2, text="Exit", width=12, pady=5, command = combine_funcs(turnOff, stop))
b.place(x=250,y=550)
b = Button(window, borderwidth=2, text="Clear Message", width=16, pady=5, command = clear_msg)
b.place(x=50,y=550)

window.mainloop()

