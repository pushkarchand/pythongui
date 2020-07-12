import tkinter as tk
from tkinter import messagebox,StringVar
import landingpage
import register
from bson.objectid import ObjectId

class Dashboard(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("Dashboard"+ " (" +master.user['name'] + ")")
        self.master.geometry('1200x600')
        self.searchparam=StringVar()
        self.searchfeildType=StringVar()
        self.searchfeildType.set('name')
        tk.Label(self, text="Dashboard", width="90",height=2,font='bold').grid(row=0,column=0,columnspan=5)
        tk.Button(self, text="Add New",
                  command=lambda: master.switch_frame(register.Register,True)).grid(row=0,column=5)
        tk.Button(self, text="Logout",
                  command=lambda: self.logoutUser()).grid(row=0,column=6)
        tk.Label(self, text="",pady=20).grid(row=1,column=0)
        tk.Label(self, text="Search").grid(row=2,column=0)
        tk.Entry(self, textvariable=self.searchparam,width=50).grid(row=3,column=0,columnspan=2)
        tk.Radiobutton(self, text="Name", padx=20, variable=self.searchfeildType,
            value="name").grid(row=3, column=2)
        tk.Radiobutton(self, text="Email", padx=20, variable=self.searchfeildType,
            value="email").grid(row=3, column=3)
        tk.Radiobutton(self, text="Mobile", padx=20, variable=self.searchfeildType,
            value="mobile").grid(row=3, column=4)
        tk.Button(self, text="Search",
                  command=lambda:self.searchUsers()).grid(row=3,column=5)
        tk.Button(self, text="Clear Search",
                  command=lambda:self.clearSearch()).grid(row=3,column=6)
        tk.Label(self, text="").grid(row=4,column=0)
        tk.Label(self, text="").grid(row=5,column=0)
        # enumerate users created by the logedIn user
        data=master.enumerateusers()
        self.renderList(data)
    

    # search users created the logedin user based on the search option selected
    def searchUsers(self):
        query = {}
        if self.searchfeildType.get()=='name':
            query['name']={"$regex":self.searchparam.get()}
        elif self.searchfeildType.get()=='email':
            query['email']={"$regex":self.searchparam.get()}
        elif self.searchfeildType.get()=='mobile':
            query['mobile']={"$regex":self.searchparam.get()}
        data=list(self.master.db.users.find(query, {'password':0}))
        self.renderList(data)
    
    # Logout user and clear the userdetails in the app.py
    def logoutUser(self):
        self.master.setUserDetails({})
        self.master.switch_frame(landingpage.Landingpage)

    # If user has searched for users then user can clear their search
    def clearSearch(self):
        data=self.master.enumerateusers()
        self.renderList(data)
        self.searchfeildType.set('name')
        self.searchparam.set('')

    # Delete the selected user from the DB and on the GUI as well
    # on successfully deleting user indicated successfully updated
    def delete(self,user,index):
        for label in self.grid_slaves():
            if int(label.grid_info()["row"]) == int(index)+3:
                label.grid_forget()
                selectedUserId=str(user['_id'])
                self.master.db.users.delete_one({"_id":ObjectId(selectedUserId)})
        messagebox.showinfo("Information", "Successfully deleted")

    # edit exting user will direct user to edit user frame
    def edit(self,user,index):
        self.master.switch_frame(register.Register,True,str(user['_id']))
    
    # clear the table before every render of table data
    def clearall(self):
        for label in self.grid_slaves():
            if int(label.grid_info()["row"]) > 5:
                label.grid_forget()

    #  based on the user list passed render users in the grid
    def renderList(self,listitems):
        self.clearall()
        tk.Label(self,text="Name",width=20,font='bold').grid(row=6,column=0)
        tk.Label(self,text="Email",width=20,font='bold').grid(row=6,column=1)
        tk.Label(self,text="Mobile",width=20,font='bold').grid(row=6,column=2)
        tk.Label(self,text="Gender",width=20,font='bold').grid(row=6,column=3)
        tk.Label(self,text="Age",width=20,font='bold').grid(row=6,column=4)
        tk.Label(self,text="Edit",font='bold',width=15).grid(row=6,column=5)
        tk.Label(self,text="Delete",font='bold',width=15).grid(row=6,column=6)
        for i in range(len(listitems)):
            tk.Label(self,text=listitems[i]['name'],bg="#fff",width=20).grid(row=i+7,column=0)
            tk.Label(self,text=listitems[i]['email'],bg="#fff",width=20).grid(row=i+7,column=1)
            tk.Label(self,text=listitems[i]['mobile'],bg="#fff",width=20).grid(row=i+7,column=2)
            tk.Label(self,text=listitems[i]['gender'],bg="#fff",width=20).grid(row=i+7,column=3)
            tk.Label(self,text=listitems[i]['age'],bg="#fff",width=20).grid(row=i+7,column=4)
            tk.Button(self,text="edit",width=15, command=lambda i=i:self.edit(listitems[i],i)).grid(row=i+7,column=5)
            if listitems[i]['userType']!='admin':
                tk.Button(self,text="delete",width=15,command=lambda i=i:self.delete(listitems[i],i)).grid(row=i+7,column=6)

