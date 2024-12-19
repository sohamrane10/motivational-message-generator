from tkinter import *
from requests import *

root = Tk()
root.title("Motivational Msg wallah")
root.geometry("1200x400+300+50")
f = ("Ink Free", 30, "bold")

def gm():
	try:
		url = "https://zenquotes.io/api/random"
		res = get(url)
		data = res.json()
		q = data[0]['q']
		msg = str(q)
		lab.configure(text=msg)
	except Exception as e:
		msg = "issue" + str(e)
		lab.configure(text=msg)

btn = Button(root, text="Get Msg",font=f,command=gm)
btn.pack(pady=10)
lab = Label(root,font=f,wraplength=1000)
lab.pack()

root.mainloop()

