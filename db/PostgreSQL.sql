CREATE TABLE usuario (
	id serial,
	nome varchar(100),
	nascimento date,
	genero varchar(10),
	email varchar(100),
	telefone varchar(20),
	senha integer,
	PRIMARY KEY (id)
);



CREATE TABLE carona (
	id serial,
	ponto_de_saida varchar(100) NOT NULL,
	ponto_de_chegada varchar(100) NOT NULL,
	data_da_partida  date NOT NULL,
	data_da_volta date NOT NULL,
	lugares integer NOT NULL,
	detalhes text,
	motorista integer,
	 PRIMARY KEY (id),
	 FOREIGN KEY (motorista) REFERENCES usuario(id)
);



CREATE TABLE passageiro (
	id_user integer,
	id_carona integer,
	FOREIGN KEY (id_user) REFERENCES usuario(id),
	FOREIGN KEY (id_carona) REFERENCES carona(id)
);
