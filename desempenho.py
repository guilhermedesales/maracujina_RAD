import pymysql
import matplotlib.pyplot as plt

def conectar_banco():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='db_maracujina'
    )

def obter_dados_tarefas():
    try:
        conn = conectar_banco()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 
                (SELECT COUNT(*) FROM tarefas WHERE status = 'SIM') AS completas,
                (SELECT COUNT(*) FROM tarefas WHERE status = 'NAO') AS incompletas
        """)
        completas, incompletas = cursor.fetchone()

        cursor.close()
        conn.close()

        return completas, incompletas
    except Exception as e:
        print("Erro ao acessar o banco:", e)
        return 0, 0

def gerar_grafico(completas, incompletas):
    labels = ['Completas', 'Incompletas']
    valores = [completas, incompletas]
    cores = ['#4CAF50', '#F44336']

    plt.figure(figsize=(6, 6))
    plt.pie(valores, labels=labels, colors=cores, autopct='%1.1f%%', startangle=90)
    plt.title('Tarefas Completas vs Incompletas')
    plt.axis('equal')  # Deixa o gráfico circular
    plt.show()

if __name__ == '__main__':
    completas, incompletas = obter_dados_tarefas()
    gerar_grafico(completas, incompletas)
