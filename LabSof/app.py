from flask import Flask, render_template, request, redirect, url_for, flash
from modelos import *

app = Flask(__name__,template_folder="templates")

pin=1234

@app.before_request
def before_request():
	'''
	Crear la base de datos (si la necesita) y conectarse
	'''
	initialize_db() #Funtion creada en modelos.py
	
@app.teardown_request
def teardown_request(exception=None):
	print("olis")
	db.close()

@app.route('/home/')	
def home():
	if request.method == 'POST':
		hpin= request.form['Pin']
		if (hpin==pin):
			print ('holis')
			flash('bien')
		else:
			flash('mal')
			
	return render_template(
	"inicio.html")
	
@app.route('/index/')
def index():
	return render_template('index.html')
	
@app.route('/check_semester/')
def new_post():
	lista_sem=[2018,20182,2019] #simulacion de acceso a bd
	cod_sem=request.form['semesters']
	consulta=Semestre.get(id_semestre==cod_sem)
	#https://www.w3schools.com/html/tryit.asp?filename=tryhtml_elem_select
	return render_template('check semester.html')
	
@app.route('/create_semester/')
def create_semester():
	if request.method == 'POST':
		Semestre.create(
		id_semestre = request.form['Codigo semestre'],
		fecha_inicio = request.form['fecha inicio'], 
		fecha_final = request.form['fecha final'])
	return render_template(
	"new_semester.html")
	
@app.route('/manage_semester/', methods = ['POST'])
def manage_semester():
	pass
	
	
if __name__ == '__main__':
	app.run(debug = True)
	