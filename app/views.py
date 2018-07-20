# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras
conn = psycopg2.connect('dbname=sistcarona user=postgres password=ifpb host=127.0.0.1')
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

from flask import render_template, request

from app import app
class  Actor(object):
	def __init__(self,name):
		self.name = name

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
	if (request.method == 'POST'):
		nome = request.form['nome']
		email = request.form['email']
		nascimento = request.form['bday']
		senha = request.form['password']
		genero = request.form['sexo']
		telefone = request.form['telefone']
		cur.execute("INSERT INTO usuario (nome, nascimento, genero, email, telefone, senha ) VALUES ('%s','%s','%s','%s','%s','%s')"%(nome, nascimento, genero, email, telefone,senha))
		conn.commit()
	return render_template('cadastro.html')
