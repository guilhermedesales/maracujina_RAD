-- Active: 1747516643046@@127.0.0.1@3306@db_maracujina

CREATE database db_maracujina;
USE db_maracujina;

CREATE Table usuarios (
    id_usuario int not null auto_increment,
    nome varchar(100) not null,
    email varchar(150) not null UNIQUE,
    matricula varchar(30) not null UNIQUE,
    curso VARCHAR(100) not null,
    celular varchar(20),
    primary key (id_usuario)
);

CREATE Table autenticacoes (
    id_autenticacao int not null auto_increment,
    id_usuario int not null,
    senha_hash varchar(255) not null,
    primary key (id_autenticacao),
    foreign key (id_usuario) references usuarios(id_usuario)
);

SELECT * from usuarios;
select * from autenticacoes;
desc usuarios;
desc autenticacoes;
show tables;