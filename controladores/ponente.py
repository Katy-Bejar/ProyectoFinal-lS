import functools
from os import error
from flask import(render_template, Blueprint, flash, g, redirect, request, session, url_for)

from werkzeug.security import check_password_hash, generate_password_hash

from myblog.models.user import User

from myblog import db

ponente = Blueprint('', __name__, url_prefix='/')

#Registrar un usuario 
@ponente.route('/registro', methods=('GET','POST'))
def registro():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(username, generate_password_hash(password))   
    return render_template('registro.html')


#Iniciar Sesión
@ponente.route('/inicioSesion', methods=('GET','POST'))
def inicioSesion():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        error = None
        user = User.query.filter_by(username = username).first()

    return render_template('inicioSesion.html')


@ponente.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)


@ponente.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('inicioSesion'))
        return view(**kwargs)
    return wrapped_view