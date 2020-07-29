from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk, Image
import os
from datetime import date
import tkinter.messagebox
import tkinter.filedialog


#icon file not added so far
root=Tk()
root.geometry("640x400")
root.configure(background="#2B2B2B")
root.title("My Daily Journal")
root.resizable(False, False)
root.iconbitmap('journal.ico')
#root.wm_attributes('-alpha', 0.5) #opacity of root

#image file of orange ribbon
img = ImageTk.PhotoImage(Image.open("bookmark.png"))
panel = Label(root, image = img,bg="#2B2B2B")
panel.place(x=550,y=0,width=70,height=120)

#color code
#F5A623 orange
#047AFB blue


softwarename="My Daily Journal"
fontStyle = tkFont.Font(family="Lucida Grande", size=24)
Labelsoftwarename=Label(root,text=softwarename,bg="#2B2B2B",fg="#FAFAFA",font=fontStyle)
Labelsoftwarename.place(x=200,y=20,width=240,height=50)
labelread=Label(root,text="Express your daily experience and feelings here",bg="#2B2B2B",fg="#FAFAFA",font=('Lucida Grande',16))
labelread.place(x=100,y=100,width=440,height=50)


#create  current day entry, if already created then open that.
def new():
	global savephoto
	global searchbox
	global f
	global datetoday
	text=""
	newWindow = Toplevel(root)
	newWindow.title("Tell me about your day")
	newWindow.geometry("640x800")				#
	newWindow.configure(background="#2B2B2B")
	newWindow.resizable(False, False)
	newWindow.iconbitmap('journal.ico')


	Diary="Dear Diary"
	fontStyle1 = tkFont.Font(family="Lucida Grande", size=34)
	Labeldiary=Label(newWindow,text=Diary,bg="#2B2B2B",fg="#FAFAFA",font=fontStyle1)
	Labeldiary.place(x=30,y=20,width=240,height=50)

	searchbox=Text(newWindow,font=("Helvetica", 18), highlightbackground="#F5A623",highlightcolor="#F5A623",highlightthickness="1",selectbackground="#013399",insertbackground="#FAFAFA", borderwidth=0,bg="#4A4A4A",fg="#FAFAFA")
	searchbox.place(x=20,y=90,width=600,height=690)

	savebutton=Button(newWindow)
	savephoto=PhotoImage(file="save.png")
	savebutton.config(image=savephoto,activebackground="#047AFB",bg="#047AFB", bd=0,command=save)
	savebutton.place(x=500,y=30,width=120,height=30)

	datetoday=date.today() #2020-06-17
	if os.path.isfile(str(datetoday)+'.txt'):
		searchbox.delete(1.0,END)
		f = open(str(datetoday)+".txt", "r")
		text13 = f.read()
		searchbox.insert(1.0,text13)

	else:
		file = open(str(datetoday)+".txt", "w")
		searchbox.delete(1.0,END)
		f = open(str(datetoday)+".txt", "w")
		text13 = f.read()

def save():
	f = open(str(datetoday)+".txt", "w")
	f.write(searchbox.get(1.0,END))
	tkinter.messagebox.showinfo('FYI', 'File Saved.')
	return


# open old entry, Read only
def openclick():
	openWindow = Toplevel(root)
	openWindow.title("Tell me about your day")
	openWindow.geometry("640x800")				#
	openWindow.configure(background="#2B2B2B")
	openWindow.resizable(False, False)
	openWindow.iconbitmap('journal.ico')

	readbox=Text(openWindow,font=("Helvetica", 18), highlightbackground="#F5A623",highlightcolor="#F5A623",highlightthickness="1",selectbackground="#013399",insertbackground="#FAFAFA", borderwidth=0,bg="#4A4A4A",fg="#FAFAFA")
	readbox.place(x=20,y=20,width=600,height=760)

	filetypes = [('Text', '*.txt'),]

	filename = tkinter.filedialog.askopenfilename(filetypes = filetypes)
	f = open(filename, 'r')
	f2 = f.read()
	readbox.insert(1.0,f2)

	return


#exit button functionality
def exit():
	iExit=tkinter.messagebox.askyesno("Gratitude Journal Application",'Do you want to exit?')
	if iExit>0:
		root.destroy()
	return



#buttons

newbutton=Button(root)
newphoto=PhotoImage(file="new.png")
newbutton.config(image=newphoto,activebackground="#047AFB",bg="#047AFB", bd=0,command=new)
newbutton.place(x=260,y=220,width=120,height=30)

openbutton=Button(root)
openphoto=PhotoImage(file="open.png")
openbutton.config(image=openphoto,activebackground="#047AFB",bg="#047AFB", bd=0,command=openclick)
openbutton.place(x=260,y=270,width=120,height=30)

exitbutton=Button(root)
exitphoto=PhotoImage(file="exit.png")
exitbutton.config(image=exitphoto,activebackground="#047AFB",bg="#047AFB", bd=0,command=exit)
exitbutton.place(x=260,y=320,width=120,height=30)


mainloop()

