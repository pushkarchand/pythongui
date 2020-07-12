import tkinter as tk
from tkinter import Tk, messagebox, StringVar
import re
import os
import landingpage
import dashboard


class Login(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("Login")
        self.master.geometry('1200x600')
        self.email=StringVar()
        self.password=StringVar()
        self.initializeView()

    # set default view of the login screen
    def initializeView(self):
        tk.Label(self, text="Please enter login details", bg="blue", width="155", height="2", font=("Calibri", 13)).grid(row=0,column=0,columnspan=10) 
        tk.Label(self, text="").grid(row=1,column=0)
        tk.Label(self, text="").grid(row=2,column=0)
        tk.Label(self, text="").grid(row=3,column=0)
        tk.Label(self, text="").grid(row=4,column=0)
        tk.Label(self, text="Email",font=(14)).grid(row=5,column=4,columnspan=2)
        tk.Entry(self, textvariable=self.email,width=40,font=(12)).grid(row=6,column=4,columnspan=2,pady = 4)
        tk.Label(self, text="").grid(row=7,column=0)
        tk.Label(self, text="Password",font=(14)).grid(row=8,column=4,columnspan=2)
        tk.Entry(self, textvariable=self.password, show= '*',width=40,font=(12)).grid(row=9,column=4,columnspan=2,pady = 4)
        tk.Label(self, text="").grid(row=10,column=0)
        tk.Button(self, text="Login",font=(16), width=40,command=lambda: self.login()).grid(row=11,column=4,columnspan=2)
        tk.Label(self,text="").grid(row=12,column=0)
        tk.Button(self, text="Back",font=(16), width=40,
             command=lambda: self.master.switch_frame(landingpage.Landingpage)).grid(row=13,column=4,columnspan=2)

    # Validate 
    def login(self):
        if self.email.get() == "":
            messagebox.showinfo("Information", "Please Enter the Email")
        elif self.password.get() == "":
            messagebox.showinfo("Information", "Please Enter the password")
        else:
            status = self.validateUser(self.email.get(), self.password.get())
            if status:
                messagebox.showinfo("Information", "Logined Successfully")
                self.master.switch_frame(dashboard.Dashboard)
            else:
                messagebox.showinfo("Information", "Invalid Credentials")


    # fuction for validation credential
    def validateUser(self,email, pwd):
        data = self.getUserDetails(email)
        if data['data']:
            if email == data["data"]["email"] and pwd == data["data"]["password"]:
                return True
            else:
                return False
        else:
            return False


    def getUserDetails(self,email):
        results = self.master.db.users.find_one({'email': email})
        if results != None:
            self.master.setUserDetails(results)
            return {"data": results, "status": True}
        else:
            return {"data": results, "status": False}


    def clearFieleds(self):
        self.email.set("")
        self.password.set("")