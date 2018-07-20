# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras
conn = psycopg2.connect('dbname=sistcarona user=postgres password=ifpb host=127.0.0.1')
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


from flask import render_template, request, redirect, url_for

from app import app
class  Actor(object):
	def __init__(self,name):
		self.name = name

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/carona', methods=['GET', 'POST'])
def carona():
	if (request.method == 'POST'):
		ponto_de_saida = request.form['ponto_de_saida']
		ponto_de_chegada = request.form['ponto_de_chegada']
		data_da_partida = request.form['data_da_partida']
		data_da_volta = request.form['data_da_volta']
		lugares = request.form['lugares']
		valor = request.form['valor']
		descricao = request.form['descricao']
		cur.execute("INSERT INTO carona(ponto_de_saida, ponto_de_chegada, data_da_partida, data_da_volta, lugares, valor, descricao) VALUES ('%s','%s',%s,%s,%s,%s,'%s')"%(ponto_de_saida, ponto_de_chegada, data_da_partida, data_da_volta, lugares,valor,descricao))
		conn.commit()
	return render_template('carona.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
	if (request.method == 'POST'):
		nome = request.form['nome']
		email = request.form['email']
		nascimento = request.form['bday']
		senha = request.form['password']
		genero = request.form['sexo']
		telefone = request.form['telefone']
		cur.execute("INSERT INTO usuario (nome, nascimento, genero, email, telefone, senha ) VALUES ('%s','%s','%s','%s','%s',%s)"%(nome, nascimento, genero, email, telefone,senha))
		conn.commit()
	return render_template('cadastro.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	if (request.method == 'POST'):
		cur.execute("SELECT * FROM usuario;")
		usuarios = cur.fetchall()
		email = request.form['email']
		senha = request.form['password']
		for i in usuarios:
			if i['email'] == email and i['senha'] == int(senha):
				return render_template('homecarona.html')
			else:
				pass
	return render_template('login.html')
