import tkinter as tk
from tkinter import  messagebox
import re
import os
import urllib 
from pymongo import MongoClient
from landingpage import Landingpage


class MathcoApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # create DB connection which is accessed across all pages
        uri='mongodb://test:test@cluster-2020-shard-00-01-krpg7.mongodb.net:27017/mathco?ssl=true&retryWrites=true&w=majority&authSource=admin'
        self.dbconnection=MongoClient(uri)
        self.db=self.dbconnection['mathco']
        self.user={}
        self._frame = None
        self.isUserRegistered =False
        self.selectedUserId=''
        # set landing page as default page
        self.switch_frame(Landingpage)

    # Swicth frames when user navigates between pages
    def switch_frame(self, frame_class,argIsRegistration=False,argUserId=''):
        self.isUserRegistered =argIsRegistration
        self.selectedUserId=argUserId
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(row=0,column=0)

    # DB query to find all users
    def enumerateusers(self):
        query={}
        if self.user:
            query.update({'createdby':self.user['_id']})
        return list(self.db.users.find(query, {"password": 0}))
    
    # set logedin user details
    def setUserDetails(self,arguser):
        self.user=arguser
    
    def isValidEmail(self,email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex, email)):
            return True
        else:
            messagebox.showinfo("Information", "this is not a valid email address")
            return False
    

if __name__ == "__main__":
    app = MathcoApp()
    app.mainloop()