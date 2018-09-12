from flask import Flask, render_template, request, redirect, url_for
from modelos import *

app = Flask(__name__)

@app.before_request
def before_request():
	'''
	Crear la base de datos (si la necesita) y conectarse
	'''
	initialize_db() #Funtion creada en modelos.py
	
@app.teardown_request

def teardown_request():
	'''
	Cerrar la conexión con la db
	'''
	db.close()

@app.route('/home/')	
def home():
	return render_template(
	'index.html',
	posts = Post.select().order_by(Post.date.desc()))
	
@app.route('/new_post/')
def new_post():
	return render_template('new_semester.html')
	
@app.route('/create/', methods = ['SEMESTRE'])
def create_semester():
	Semestre.create(
	fecha_inicio = request.form['fecha inicio'], 
	fecha_final = request.form['fecha final'])
	
	return redirect(url_for('home'))
@app.route('/manage/', methods = ['SEMESTRE'])
def manage_semester():
	
	
if __name__ == '__main__':
	app.run(debug = True)
	