import mysql.connector

try:
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='db_maracujina'
    )
    if conexao.is_connected():
        print("Conexão bem-sucedida!")
    conexao.close()

except mysql.connector.Error as erro:
    print(f"Erro ao conectar: {erro}")
