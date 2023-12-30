from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from AI import openai_handler


from config import config

# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User

app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user == None:
            flash("User not found...")
            return render_template('auth/login.html')
        elif False == logged_user.password:
            flash("Invalid password...")
            return render_template('auth/login.html')
        else:
            login_user(logged_user)
            return redirect(url_for('home'))
    else:
        return render_template('auth/login.html')



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/chat_page', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        data = request.get_json()
        text = data['text']

        respuesta = openai_handler.generate_chatbot_response(text)

        return respuesta
    else:
        return render_template('chat_page.html')


def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>The page you search do not exist</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
