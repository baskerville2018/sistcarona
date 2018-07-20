-- Gênero
CREATE TABLE genero (
    id SERIAL,
    nome VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO genero (nome) VALUES ('Trash');
INSERT INTO genero (nome) VALUES ('Terror');
INSERT INTO genero (nome) VALUES ('Indie');
INSERT INTO genero (nome) VALUES ('Drama');
INSERT INTO genero (nome) VALUES ('Ação');

-- Filme
CREATE TABLE filme (
    id SERIAL,
    nome VARCHAR(255) NOT NULL,
    ano INTEGER NOT NULL,
    descricao TEXT NOT NULL,
    diretor VARCHAR(255) NOT NULL,
    genero INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY (genero) REFERENCES genero(id)
);
INSERT INTO filme (nome, ano, descricao, diretor, genero) VALUES ('Toy story', 1995, 'O aniversário de Andy está chegando e os brinquedos estão nervosos. Afinal de contas, eles temem que um novo brinquedo possa substituí-los. Liderados por Woody, um caubói que é também o brinquedo predileto de Andy, eles montam uma escuta que lhes permite saber dos presentes ganhos. Entre eles está Buzz Lightyear, o boneco de um patrulheiro espacial, que logo passa a receber mais atenção do garoto. Isto aos poucos gera ciúmes em Woody, que tenta fazer com que ele caia atrás da cama. Só que o plano dá errado e Buzz cai pela janela. É o início da aventura de Woody, que precisa resgatar Buzz também para limpar sua barra com os outros brinquedos.', 'John Lasseter', 6);
INSERT INTO filme (nome, ano, descricao, diretor, genero) VALUES ('Rubber, O Pneu Assassino', 2010, 'Em algum lugar do deserto californiano, um pneu telepático acorda subitamente para uma missão demoníaca, isto é, assassinar todos os seres que vir pela frente. Os habitantes da região assistem incrédulos aos crimes cometidos por esta espécie de serial killer das rodovias, que se sente misteriosamente atraído por uma bela jovem. Em paralelo, uma investigação é lançada.', 'Quentin Dupieux', 1);

-- Ator
CREATE TABLE ator (
    id SERIAL,
    nome VARCHAR(255) NOT NULL,
    data_nasc DATE,
    bio TEXT,
    PRIMARY KEY (id)
);

-- Usuário
CREATE TABLE usuario (
    id SERIAL,
    nome VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    senha VARCHAR(15) NOT NULL,
    PRIMARY KEY (id)
);

-- Personagem
CREATE TABLE personagem (
    id SERIAL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    ator INTEGER,
    filme INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY (ator) REFERENCES ator(id),
    FOREIGN KEY (filme) REFERENCES filme(id)
);

-- Curtir
CREATE TABLE curtir (
    usuario INTEGER,
    filme INTEGER,
    FOREIGN KEY (usuario) REFERENCES usuario(id),
    FOREIGN KEY (filme) REFERENCES filme(id)
);

-- Avaliacao
CREATE TABLE avaliacao (
    id SERIAL,
    rate INTEGER,
    comentario TEXT,
    data DATE,
    usuario INTEGER,
    filme INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY (usuario) REFERENCES usuario(id),
    FOREIGN KEY (filme) REFERENCES filme(id),
    CONSTRAINT rate_check CHECK (rate >= 0 and rate <=5)
);
