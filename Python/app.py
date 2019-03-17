import tkinter as tk
from tkinter import *
import webbrowser
import urllib.request
import os
import socket		# to get address of server     

def all_children (window) :
	_list = window.winfo_children()
	for item in _list :
		if item.winfo_children() :
			_list.extend(item.winfo_children())
	return _list


def clear_window(window):
	widget_list = all_children(window)
	print(widget_list)
	for item in widget_list:
	    item.pack_forget()


def change_frame(obj,which_frame,from_which_frame):
	from_which_frame.destroy()
	which_frame()


def frame_home(obj):
	frame = Frame(obj, width=500, height=500)
	frame.pack(pady=80)

	b2=Button(frame,text="Start Collabration",state="normal", width=25,command=lambda:change_frame(obj,lambda:frame_server(obj),frame))
	b2.pack(pady=20)

	b2=Button(frame,text="Join Collabration",state="normal", width=25,command=lambda:change_frame(obj,lambda:frame_join(obj),frame))
	b2.pack(pady=20)

	b3=Button(frame,text="Exit", width=25,command=obj.destroy)
	b3.pack(pady=20)


def go(url):
	print(url)
	webbrowser.open(url)

def go_server(url):	
	go(url)
	cmd = os.system("cd ../Socket && npm start")
	
	

def frame_join(obj):
	frame = Frame(obj, width=500, height=500)
	frame.pack(pady=40)

	l=Label(frame,text="Join Collaboration",font = "Helvetica 16 bold italic")
	l.pack(pady=40)

	l=Label(frame,text="IP address : ")
	l.pack()

	e1 = Entry(frame)
	e1.insert(END, '10.0.1.193')
	e1.pack(pady=10)

	l=Label(frame,text="Port no :")
	l.pack()

	e2 = Entry(frame)
	e2.insert(END, '80')
	e2.pack(pady=10)
	
	
	b1=Button(frame,text="Proceed",state="normal", width=25,command= lambda : go('http://'+e1.get()+'/VAPPP' ))
	b1.pack(pady=10)

	b2=Button(frame,text="Back",state="normal", width=25,command=lambda:change_frame(obj,lambda:frame_home(obj),frame))
	b2.pack(pady=10)


def frame_server(obj):

	frame = Frame(obj, width=500, height=500)
	frame.pack(pady=40)

	l=Label(frame,text="Start Collaboration",font = "Helvetica 16 bold italic")
	l.pack(pady=40)

	# =================================================
	hostname = socket.gethostname() 
	IPAddr = socket.gethostbyname(hostname)
	# ==================================================

	# l=Label(frame,text="Share Id : 10.0.1.193:8000")
	l=Label(frame,text="Share Id : 10.0.1.193:80")
	l.pack(pady=10)

	l=Label(frame,text="Click On button to start Editing..")
	l.pack(pady=10)

	b1=Button(frame,text="Proceed",state="normal", width=25,command= lambda : go_server('http://10.0.1.193:80/VAPPP' ))
	b1.pack(pady=10)

	b2=Button(frame,text="Quit",state="normal", width=25,command=obj.destroy)
	b2.pack(pady=10)


if __name__ == "__main__":
    obj = tk.Tk()
    obj.title('VAPPP')
    obj.geometry("500x500")
    
    frame_home(obj)    
    obj.mainloop() 
