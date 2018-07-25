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
		data_de_partida  = request.form['data_de_partida']
		data_de_chegada = request.form['data_de_chegada']
		lugares = request.form['lugares']
		valor = request.form['valor']
		detalhes = request.form['descricao']
		cur.execute("INSERT INTO carona(ponto_de_saida, ponto_de_chegada, data_de_partida, data_de_chegada, lugares,valor , detalhes ) VALUES ('%s','%s','%s','%s',%s,%s,'%s')"%(ponto_de_saida, ponto_de_chegada, data_de_partida, data_de_chegada, lugares, valor, detalhes))
		conn.commit()
	return render_template('carona.html')

@app.route('/ofertadas', methods=['GET', 'POST'])
def ofertadas():
	if (request.method == 'POST'):
		cur.execute("SELECT * FROM carona;")
		caronas = cur.fetchall()
		ponto_de_saida = request.form['ponto_de_saida']
		ponto_de_chegada = request.form['ponto_de_chegada']
		data_de_partida  = request.form['data_de_partida']
		data_de_chegada = request.form['data_de_chegada']

		cur.execute("UPDATE carona SET lugares = lugares - 1 where ponto_de_saida = '%s' and ponto_de_chegada = '%s';" %(ponto_de_saida, ponto_de_chegada))
		cur.execute("SELECT ponto_de_saida, ponto_de_chegada, to_char(data_de_partida, 'DD/MM/YYYY') AS data_de_partida, to_char(data_de_chegada, 'DD/MM/YYYY') AS data_de_chegada, lugares, valor, detalhes, motorista FROM carona where ponto_de_saida = '%s' and ponto_de_chegada = '%s';" %(ponto_de_saida, ponto_de_chegada))
		
		lista_caronas = cur.fetchall()
		return render_template('ofertadas.html', caronas=lista_caronas)
	cur.execute("SELECT ponto_de_saida, ponto_de_chegada, to_char(data_de_partida, 'DD/MM/YYYY') AS data_de_partida, to_char(data_de_chegada, 'DD/MM/YYYY') AS data_de_chegada, lugares, valor, detalhes, motorista FROM carona")
	lista_caronas = cur.fetchall()
	return render_template('ofertadas.html', caronas=lista_caronas)



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
		cur.execute("SELECT * FROM usuario where email = '%s' and senha = '%s';"%(email, senha))
		if len(cur.fetchall())>0:
			session={}
			session['id'] = cur.execute("SELECT id_usuario FROM usuario where email = '%s' and senha = '%s';"%(email, senha))
			session['nome'] = cur.execute("SELECT nome FROM usuario where email = '%s' and senha = '%s';"%(email, senha))
			return render_template('homecarona.html')
		
	return render_template('login.html')
