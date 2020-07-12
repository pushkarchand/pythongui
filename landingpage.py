import tkinter as tk
from login import Login
from register import Register


class Landingpage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.geometry('1200x600')
        tk.Label(self, text="Please Select your option", bg="blue", width="155", height="2", font=("Calibri", 13)).grid(row=0,column=0,columnspan=10) 
        tk.Label(self,text="").grid(row=1,column=0)
        tk.Label(self,text="").grid(row=2,column=0)
        tk.Label(self,text="").grid(row=3,column=0)
        tk.Label(self,text="").grid(row=4,column=0)
        tk.Label(self,text="").grid(row=5,column=0)
        tk.Label(self,text="").grid(row=6,column=0)
        tk.Label(self,text="").grid(row=7,column=0)
        tk.Button(self,text="Login", height="2", width="30", font=(16),
            command = lambda: master.switch_frame(Login)).grid(row=8,column=4,columnspan=2)
        tk.Label(self,text="").grid(row=9,column=0)
        tk.Button(self, text="Register", height="2", width="30",font=(16),
                  command=lambda: master.switch_frame(Register)).grid(row=10,column=4,columnspan=2)