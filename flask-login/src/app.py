from contextlib import redirect_stderr
from functools import reduce
from django.shortcuts import redirect
from flask import Flask, render_template, request,redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_wtf import CSRFProtect

from config import config #importo la configuracion de config

#Models:
from models.ModelUser import ModelUser

#Entities:
from models.entities.User import User

app = Flask(__name__)

#token form
csrf=CSRFProtect(app)
db = MySQL(app) #ejecuto la base
login_manager_app = LoginManager(app)

#cargo los datos del user
@login_manager_app.user_loader
def load_user(id):
      return ModelUser.get_by_id(db, id)


##redirijo de la ruta raiz al login
@app.route('/')
def index():
      return redirect(url_for('login'))


#acepto GET y POST
@app.route('/login', methods=['GET','POST'])

def login():
      if request.method=='POST':
            #print(request.form['username'])
            #print(request.form['password'])
            user = User(0, request.form['username'], request.form['password'])
            logged_user=ModelUser.login(db, user)
            if logged_user != None:
                  if logged_user.password:
                        login_user(logged_user)
                        return redirect(url_for('home'))
                  else:
                        flash("invalid pasword...")
                        return render_template('auth/login.html')
            else:
                  flash("invalid user...")
                  return render_template('auth/login.html')
            return render_template('auth/login.html')
      else:
            return render_template('auth/login.html')

#vista home
@app.route('/home')
def home():
      return render_template('home.html')


#vista logout
@app.route('/logout')
def logout():
      logout_user()
      return redirect(url_for('login'))


#vista protegida
@app.route('/protected')
@login_required
def protected():
      return "<h1>Esta es una vista protegida</h1>"

def status_404(error):
      return "<h1>Pagina no encontrada</h1>", 404


def status_401(error):
      return redirect(url_for('login'))


if __name__ == '__main__':
      app.config.from_object(config['development'])#el diccionario config en su llave development
      csrf.init_app(app)
      app.register_error_handler(401, status_401)
      app.register_error_handler(404, status_404)
      app.run()





