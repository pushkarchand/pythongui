import tkinter as tk
import tkinter as tk
from tkinter import Tk, Text, messagebox, StringVar, IntVar
from bson.objectid import ObjectId
import re
import os
import landingpage
import login
import dashboard

class Register(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # set header based on isUserRegistered  if loged in or Registration
        if master.isUserRegistered :
            self.master.title("Add new user"+ " ("+ master.user['name']+')')
        else:
            self.master.title("Register")
        self.master.geometry('1200x600')
        self.username=StringVar()
        self.email=StringVar()
        self.mobile=StringVar()
        self.gender=StringVar()
        self.age=StringVar()
        self.password=StringVar()
        self.confirmpassword=StringVar()
        self.gender.set('male')
        self.userType=StringVar()
        self.setDefaultScreen()
        
    # set default screen like input fields
    def setDefaultScreen(self):
        self.showWidgetsBasedOnRegistration()
        tk.Label(self, text="").grid(row=1,column=0)
        tk.Label(self, text="Username").grid(row=2,column=4,columnspan=2)
        tk.Entry(self, textvariable=self.username,width=50).grid(row=3,column=4,columnspan=2)
        tk.Label(self, text="").grid(row=4,column=0)
        tk.Label(self, text="Email").grid(row=5,column=4,columnspan=2)
        tk.Entry(self, textvariable=self.email,width=50).grid(row=6,column=4,columnspan=2)
        tk.Label(self, text="").grid(row=7,column=0)
        tk.Label(self, text="mobile").grid(row=8,column=4,columnspan=2)
        tk.Entry(self, textvariable=self.mobile, width=50).grid(row=9,column=4,columnspan=2)
        tk.Label(self, text="").grid(row=10,column=0)
        tk.Label(self, text="age").grid(row=11,column=4,columnspan=2)
        tk.Entry(self, textvariable=self.age,width=50).grid(row=12,column=4,columnspan=2)
        tk.Label(self, text="").grid(row=13,column=0)
        tk.Label(self, text="Gender").grid(row=14,column=4,columnspan=2)
        tk.Radiobutton(self, text="Male", padx=5, variable=self.gender,
            value="male").grid(row=15, column=4)
        tk.Radiobutton(self, text="Female", padx=20, variable=self.gender,
            value="female").grid(row=15, column=5)
        tk.Label(self, text="").grid(row=16,column=0)
        tk.Label(self, text="Password").grid(row=17,column=4,columnspan=2)
        tk.Entry(self, textvariable=self.password,width=50,show="*").grid(row=18,column=4,columnspan=2)
        tk.Label(self, text="").grid(row=19,column=0)
        tk.Label(self, text="confirm password").grid(row=20,column=4,columnspan=2)
        tk.Entry(self, textvariable=self.confirmpassword,
            width=50,show="*").grid(row=21,column=4,columnspan=2)
        tk.Label(self, text="").grid(row=22,column=0)
        tk.Button(self, text="Submit", width=45,
            command=lambda:self.registerUser()).grid(row=23,column=4,columnspan=2)
        tk.Label(self,text="").grid(row=24,column=0)

    # show header and set input field value based on the isUserRegistered  and selectedUserId
    # Check If the Registeration or update user
    def showWidgetsBasedOnRegistration(self):
        # If isUserRegistered is True and selectedUserId=='' that means add new user
        if self.master.isUserRegistered  and self.master.selectedUserId=='':
            tk.Button(self, text="Back", width=45,
                command=lambda: self.master.switch_frame(dashboard.Dashboard)).grid(row=25,column=4,columnspan=2)
            tk.Label(self, text="Add new user", bg="blue",
                width="155", font=("Calibri", 13)).grid(row=0,column=0,columnspan=10) 
        # If edit user then set user details to the GUI screen values like username,
        # email,mobile,gender,passowrd and confirm password
        elif self.master.isUserRegistered  and self.master.selectedUserId!='':
            try:
                tk.Button(self, text="Back", width=45,
                    command=lambda: self.master.switch_frame(dashboard.Dashboard)).grid(row=25,column=4,columnspan=2)
                tk.Label(self, text="Update user", bg="blue",
                    width="155", font=("Calibri", 13)).grid(row=0,column=0,columnspan=10) 
                user=self.master.db.users.find_one({"_id":ObjectId(self.master.selectedUserId)})
                if user:
                    self.username.set(user['name'])
                    self.email.set(user['email'])
                    self.mobile.set(user['mobile'])
                    self.gender.set(user['gender'])
                    self.age.set(user['age'])
                    self.password.set(user['password'])
                    self.confirmpassword.set(user['password'])
                    self.userType.set(user['userType'])
            except :
                self.master.switch_frame(dashboard.Dashboard)
        else :
            # If Register user then only set header text
            tk.Button(self, text="Back", width=45,
                command=lambda: self.master.switch_frame(landingpage.Landingpage)).grid(row=25,column=4,columnspan=2)
            tk.Label(self, text="Please enter your Registration details", bg="blue",
                width="155", font=("Calibri", 13)).grid(row=0,column=0,columnspan=10) 

    # Validate user inputs if any field fails then send the message
    # If all the fields pass the validations Check if the user is the first user
    # If user is first user then make the user admin
    # Else make the user normal user
    # Insert the user and send user to login(Register)/ Dashboard if (adduser/Update user)
    def registerUser(self):
        try:
            newage = int
            try:
                newage = int(self.age.get())
            except:
                newage=0
            if self.username.get() == "":
                messagebox.showinfo("Information", "Please Enter the full name")
            elif self.password.get() == "":
                messagebox.showinfo("Information", "Please Enter the password")
            elif self.confirmpassword.get() == "":
                messagebox.showinfo("Information", "Please Enter the confirm "
                                                "password to proceed")
            elif len(self.mobile.get()) != 10:
                messagebox.showinfo("Information", "Please Enter the 10 digit Mobile "
                                                "Number")
            elif self.email.get() == "":
                messagebox.showinfo("Information", "Please Enter the Email Id")
            elif self.gender.get() == "":
                messagebox.showinfo("Information", "Please select the gender")
            elif newage <= 0:
                messagebox.showinfo("Information", "Please Enter the Age")
            elif self.password.get() != self.confirmpassword.get():
                messagebox.showinfo("Information", "Password Mismatch")
            elif self.email.get() != "":
                status = self.master.isValidEmail(self.email.get())
                if status and self.master.selectedUserId=='':
                    # Register user / Add new user
                    userdata = {
                        "name": self.username.get(),
                        "password": self.password.get(),
                        "mobile": self.mobile.get(),
                        "email": self.email.get(),
                        "gender": self.gender.get(),
                        "age": self.age.get(),
                        "userType": "user"
                    }
                    userRoleCheck = self.isUserAdmin()
                    if not userRoleCheck:
                        dict1 = {"userType": "admin"}
                        userdata.update(dict1)
                    # if user is adding new user then add created userId
                    if self.master.user:
                         userdata.update({"createdby":self.master.user['_id']})
                    self.master.db.users.insert_one(userdata)
                    self.clearallfields()
                    if self.master.isUserRegistered :
                        messagebox.showinfo("Information", "Sucessfully added user")
                        self.master.switch_frame(dashboard.Dashboard)
                    else:
                        messagebox.showinfo("Information", " Add new user Sucessfully")
                        self.master.switch_frame(login.Login)
                elif status and self.master.selectedUserId!='':
                    # update existing user details
                    query={"_id":ObjectId(self.master.selectedUserId)} 
                    newvalues = {
                            "$set":{
                            "name": self.username.get(),
                            "password": self.password.get(),
                            "mobile": self.mobile.get(),
                            "email": self.email.get(),
                            "gender": self.gender.get(),
                            "age": self.age.get(),
                            "userType": self.userType.get()
                            }
                    }
                    if self.master.user._id:
                        newvalues.update({"createdby":self.master.user._id})
                    self.master.db.users.update_one(query,newvalues)
                    messagebox.showinfo("Information", "Updated user Successfully")
                    self.master.switch_frame(dashboard.Dashboard)

            # else:
            #     # messagebox.showinfo("Information", "User with same already exists")
        except Exception as error:
            print(error)


    # Check if admin already
    def isUserAdmin(self):
        results = self.master.db.users.find_one({'userType': "admin"})
        if results != None:
            return True
        else:
            return False

    # clear all input fields
    def clearallfields(self):
        self.username.set("")
        self.password.set("")
        self.confirmpassword.set("")
        self.mobile.set("")
        self.email.set("")
        self.gender.set("")
        self.age.set("")
