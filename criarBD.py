import pymysql

_SQL = """
CREATE DATABASE IF NOT EXISTS db_maracujina
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

USE db_maracujina;

CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome       VARCHAR(100)  NOT NULL,
    email      VARCHAR(150)  NOT NULL UNIQUE,
    matricula  VARCHAR(30)   NOT NULL UNIQUE,
    curso      VARCHAR(100)  NOT NULL,
    celular    VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS autenticacoes (
    id_autenticacao INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario      INT          NOT NULL,
    senha           VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

CREATE TABLE IF NOT EXISTS tarefas (
    id_tarefa   INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario  INT          NOT NULL,
    nome_tarefa VARCHAR(255) NOT NULL,
    matriz      VARCHAR(4),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);
"""

def ensure_database(
    host="localhost",
    user="root",
    password="root",
    port=3306,
):

    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        port=port,
        autocommit=True   
    )
    try:
        with conn.cursor() as cur:
            for stmt in _SQL.strip().split(";"):
                sql = stmt.strip()
                if sql:
                    cur.execute(sql + ";")
    finally:
        conn.close()
    return True


if __name__ == "__main__":
    try:
        ensure_database()
        print(" Banco de dados garantido com sucesso.")
    except Exception as e:
        print(" Falha ao criar/garantir o banco:", e)
