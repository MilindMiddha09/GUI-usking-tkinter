import tkinter
from tkinter.constants import SUNKEN
from typing import Collection, List

mainWindow= tkinter.Tk()
mainWindow.title("Grid Demo")
mainWindow.geometry("640x480")
mainWindow['padx']=8

label=tkinter.Label(mainWindow,text="Text Grid Demo")
label.grid(row=0, column=1, columnspan=3)

mainWindow.columnconfigure(0, weight=100)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1000)
mainWindow.columnconfigure(3, weight=600)
mainWindow.columnconfigure(4, weight=1000)

mainWindow.rowconfigure(0,weight=1)
mainWindow.rowconfigure(1,weight=10)
mainWindow.rowconfigure(2,weight=3)
mainWindow.rowconfigure(3,weight=3)
mainWindow.rowconfigure(4,weight=3)

#File List
fileList=tkinter.Listbox(mainWindow)
fileList.grid(row=1,column=0, sticky="nsew", rowspan=2)
fileList.config(border=2, relief='sunken')
for zone in range(0,26) :
    fileList.insert(tkinter.END,zone)

listScroll=tkinter.Scrollbar(mainWindow,command=fileList.yview)
listScroll.grid(row=1,column=1,sticky='nsw',rowspan=2)
fileList['yscrollcommand']=listScroll.set

#frame for radio buttons
optionFrame=tkinter.LabelFrame(mainWindow,text="File Details")
optionFrame.grid(row=1,column=2, sticky="ne")

# Radio Buttons
rbValue=tkinter.IntVar()
rbValue.set(3)

radio1=tkinter.Radiobutton(optionFrame,text="File Name",value=1,variable=rbValue)
radio2=tkinter.Radiobutton(optionFrame,text="Path",value=2,variable=rbValue)
radio3=tkinter.Radiobutton(optionFrame,text="Time Stamps",value=3,variable=rbValue)
radio1.grid(row=0,column=0,sticky='w')
radio2.grid(row=1,column=0,sticky='w')
radio3.grid(row=2,column=0,sticky='w')

#Result Field
resultLabel=tkinter.Label(mainWindow,text="Result")
resultLabel.grid(row=2,column=2,sticky='nw')
result=tkinter.Entry(mainWindow)
result.grid(row=2,column=2,sticky='w')

#Time Frame
timeFrame=tkinter.LabelFrame(mainWindow,text="time")
timeFrame.grid(row=0,column=0,sticky='nw')

#Time Spinner
hourSpinner=tkinter.Spinbox(timeFrame,width=2,values=tuple(range(0,24)))
minuteSpinner=tkinter.Spinbox(timeFrame,width=2,from_=0 ,to=59)
secondSpinner=tkinter.Spinbox(timeFrame,width=2,from_=0 , to=59)

hourSpinner.grid(row=0,column=0)
tkinter.Label(timeFrame,text=':').grid(row=0,column=1)
minuteSpinner.grid(row=0,column=2)
tkinter.Label(timeFrame,text=':').grid(row=0,column=3)
secondSpinner.grid(row=0,column=4)

timeFrame['padx']=36

# Date Frame
dateFrame=tkinter.LabelFrame(mainWindow,text='Date')
dateFrame.grid(row=4,column=0,sticky='nw')

#Date Spinner
daySpinner=tkinter.Spinbox(dateFrame,width=4,from_=1,to=31)
monthSpinner=tkinter.Spinbox(dateFrame,width=4,values=("Jan","Feb","March","April","May","June","July","Aug","Sept","Oct","Nov","Dec"))
yearSpinner=tkinter.Spinbox(dateFrame,width=4,from_=2000,to=2099)

yearSpinner.grid(row=0,column=4)
tkinter.Label(dateFrame,text=':').grid(row=0,column=1)
monthSpinner.grid(row=0,column=2)
tkinter.Label(dateFrame,text=':').grid(row=0,column=3)
daySpinner.grid(row=0,column=0)

# Buttons
okButton=tkinter.Button(mainWindow, text="OK", command=mainWindow.destroy)
cancelButton=tkinter.Button(mainWindow,text="Cancel",command=mainWindow.destroy)
okButton.grid(row=4,column=3,sticky='e')
cancelButton.grid(row=4,column=3)


mainWindow.mainloop()
