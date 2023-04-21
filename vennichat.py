import tkinter as tk
from tkinter import Button, Entry, StringVar
from tkinter import * 

root = tk.Tk()
root.title("vennichat")
root.geometry("312x260")
root.resizable(False, False)
message = tk.StringVar()

chat_start = Frame(root,bd=1,bg='grey',width=40,height=8)
chat_start.place(x=6,y=6,height=200,width=300)

txt=tk.Text(chat_start,bd=1,bg='alice blue',width=30,height=4)
txt.pack(fill='both',expand=True)

msg= Entry(root,width=30, xscrollcommand=True, textvariable=message)
msg.place(x=6, y=210,height=40,width=230)
msg.focus()

txt.config(fg='black')
txt.tag_config('usr',foreground='black')
txt.insert(END,"Bot:hai,welcome to this site\nlet us know your contact details\nour executive will contact you.\n\n")

def sending_mesz(event=None):
    usr_input = msg.get()
    msg.delete(0, tk.END)
    txt.insert(END, f'you:{usr_input}'+'\n','usr')

b = Button(root, text="send", bg="brown", activebackground='grey',
              fg="black", font=('Arial'),command=sending_mesz,width=6,height=1) 
b.place(x=230, y=210)

root.mainloop()

