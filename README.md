# User managment Apllication

##### Technologies used
- python 3.7 +
- pymongo
- mongodb atlas **(DB)**

##### Folder structure and description
- app.py
    - A root file that handles all the switching of frames between landing, login, register & dashboard frames.
    - A single DB connection is maintained in the app.py which will be shared between all the frame class.
- landingpage.py
    - Landingpage frame offers the option to log in or register.
    - If the user opts for login then the login frame will be displayed.
    - If the user opts for registration then the registration frame will be displayed.
- login.py
    - login frame will handle the sign-in of the user.
    - Will validate the user credentials, if the user enters the wrong credentials a message will be displayed.
    - On successful login, the user will be directed to the dashboard screen.
- register.py
    - register screen works as both user registration, update, and add new user screen.
    - If the user opts for register from the landing page, then the user will land on the register screen where they will be asked to enter the following details. All the following fields has its validations. If the user is registering for the first time they will be made admin user.
        - username
        - emailId
        - age
        - gender
        - mobile
        - password
        - confirm password
    - After the user login successfully, the user can add a new user from the dashboard. Users can add new users by entering the above fields.
    - After the user login successfully, the user can edit the user from the dashboard by clicking on the edit option. Users can edit the above fields.
- dashboard.py
    - After the user login successfully, the user will land on the dashboard screen where they can view, edit, and add new users.
    - Search users by name, mobile, and email.
    - Users will be able to view users created by them.
- readme.md
    - project description

#### Steps to run the application in local environment
- ``install python``
- ``pip install pymongo``
- navigate to the project folder
- ``python app.py``

#### Reason's for opting Nosql(MongoDB)
    Ease of scale-out 
    Auto-Sharding
    Easily available for free as service
    Best suited for User Data Management
    Rich queries
    Replication and high availability

#### How to run the .exe file
- Navigate to dest and then app folder
- Double click on app.exe file to run the executable file.

#### References
- [Introduction to GUI programing](https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html) 
- [How to swicth between tkinter frames](https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter#:~:text=One%20way%20to%20switch%20frames,use%20any%20generic%20Frame%20class.)
- [pymongo](https://api.mongodb.com/python/current/tutorial.html)
    
    
