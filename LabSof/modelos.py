from peewee import *
import datetime

db = SqliteDatabase('semestres.db') #Base de datos

class Semestre(Model):
	'''
	Si no hay llave primaria, peewee lo hará automáticamente
	'''
	#Campos que voy a usar
	id_semestre = PrimaryKeyField()
	fecha_inicio = DateTimeField(default = datetime.datetime.now)
	fecha_final = DateTimeField(default = datetime.datetime.now)
	
	#Conectar la base de datos
	class Meta:
		database = db
		
class Materia(Model):
	id_materia = PrimaryKeyField()
	Nombre = CharField()
	Jornada = CharField()
	id_Sem = ForeignKeyField(Semestre,backref ="semestre")
	
	class Meta:
		database = db

class Grupo(Model):
	id_grupo = PrimaryKeyField()
	id_Mat = ForeignKeyField(Materia,backref ="materia")
	
	class Meta:
		database = db
		
class Estudiante (Model):
	id_estudiante= PrimaryKeyField()
	nombre = CharField()
	correo = CharField()
	
	class Meta:
		database = db
	
#Inicializar la base de datos
def initialize_db():
	db.connect()
	db.create_tables([Semestre,Materia,Estudiante,Grupo], safe = True)