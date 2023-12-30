# Chatme-AI
#### Video Demo:  <https://youtu.be/cagbn7caxYM?si=CgAige8e8rIhDAmh>
#### Description:


### Configuration before start using the app!
First create a data base with the name of your preference, a table that must have the name "user" and 4 columns as follows:
1. the first one must be called "id" and must be of type smallint(4)
2. the second one must be called "username" and must be of type varchar(20)
3. the third one must be called "password" and must be of type char(200)
4. the last one must be called "fullname" and must be of type varchar(50)

> [!IMPORTANT]
> Important: If you'r going to add a new user to the data base when you add the password must be hashed, to do this you can go to the config file and uncomment the print at the end, there you write your password, run the config file by executing `python .\src\test_project` and you should see in the terminal a lot of letters similar to this: `scrypt:32768:8:1$sR0hfAONwoKPFYii$89e4a4001c999f4870d789fcd4acfc7dfc1fed101cdb631d14a7b1b4c8d220b4ab8e6f943947979e17610938ad320375ded96190d70e5dfced396dcaf114a479` that must be the value for the column password.

### Configure the database
Go to the config file and replace the values of the following attributes in the DevelopmentConfig class:
1. MYSQL_HOST = 'localhost' 
2. MYSQL_USER = 'root' here goes the name of the user to acces to the data base
3. MYSQL_PASSWORD = '' The password should go here in case it is necessary, otherwise it can remain empty
4. MYSQL_DB = 'chat-users' Hero goes the name of the data base

Create a virtual environment by executing `virtualenv env` in the terminal. In case you don't have "virtualenv" installed, you can install it by executing `pip install virtualenv`.

Activate the virtual environment by executing `.\env\Scripts\activate`.

To finish the configuration, install all the libraries by executing `pip install -r requirements.txt` in the terminal.

### Now the app is ready to run!
Just execute `python .\src\project.py` and in the browser search 127.0.0.1, you should be able to see the login page

### To test the app just run the "test_app.py" file with pytest

