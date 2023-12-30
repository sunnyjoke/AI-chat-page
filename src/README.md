# Chatme-AI
#### Video Demo:  <https://youtu.be/cagbn7caxYM?si=CgAige8e8rIhDAmh>
#### Description:


### Before start using the app first create a data base with the name of your preference, a table that must have the name "user" and 4 columns as follows:
1. the first one must be called "id" and must be of type smallint(4)
#### 1. the second one must be called "username" and must be of type varchar(20)
#### 1. the third one must be called "password" and must be of type char(200)
#### 1. the last one must be called "fullname" and must be of type varchar(50)

#### Important: If you'r going to add an user the password must be hashed first, you can

### Go to the config file and replace the values of the following attributes in the DevelopmentConfig class:
#### 1. MYSQL_HOST = 'localhost' 
#### 1. MYSQL_USER = 'root' here goes the name of the user to acces to the data base
#### 1. MYSQL_PASSWORD = '' The password should go here in case it is necessary, otherwise it can remain empty
#### 1. MYSQL_DB = 'chat-users' Hero goes the name of the data base

### Create a virtual environment by executing `virtualenv env` in the terminal. In case you don't have "virtualenv" installed, you can install it by executing `pip install virtualenv`.
### Activate the virtual environment by executing `.\env\Scripts\activate`
### To finish the configuration, install all the libraries by executing `pip install -r requirements.txt` in the terminal.

### Now the app is ready to run! just execute `python .\src\project.py` and in the browser search 127.0.0.1, you should be able to see the login page

### To test the app just run the "test_app.py" file with pytest

