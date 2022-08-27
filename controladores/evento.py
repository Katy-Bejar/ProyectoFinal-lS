
from operator import pos
from flask import(
    render_template, Blueprint, flash, g, redirect, request, url_for
)

from werkzeug.exceptions import abort

from Dominio.Modelo.Evento import Evento
from Dominio.Modelo.Ponente import Usuario

from vistas import login_required

import db

blog = Blueprint('blog', __name__)

#Obtener un ususario
def get_user(id):
    user = Usuario.query.get_or_404(id)
    return user

@blog.route("/")
def index():
    posts = Evento.query.all()
    posts = list(reversed(posts))
    db.session.commit()
    return render_template('index.html', posts = posts, get_user=get_user)

#Eliminar un evento
@blog.route('/delete/<int:id>')
@login_required
def delete(id):
    post = get_post(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index'))

#Actualizar evento 
@blog.route('/actualizar/<int:id>', methods=('GET','POST'))
@login_required
def actualizar(id):
    post = get_post(id) 
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.body = request.form.get('body')        
    return render_template('actualizar.html', post=post)



#Registrar un evento
@blog.route('/crearEvento', methods=('GET','POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        post = Evento(g.user.id, title, body)
        error = None
        if not title:
            error = 'Se requiere un título' 
        if error is not None:
            flash(error)
        else:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('index')) 
        flash(error)
    return render_template('crearevento.html')

def get_post(id, check_author=True):
    post = Evento.query.get(id)
    if post is None:
        abort(404, f'Id {id} de la publicación no existe.')
    if check_author and post.author != g.user.id:
        abort(404)
    
    return post
