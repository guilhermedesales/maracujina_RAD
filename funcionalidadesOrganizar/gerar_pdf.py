import os
import pymysql
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

def conectar_banco():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='db_maracujina',
        connect_timeout=5
    )

def gerar_pdf(id_usuario):
    try:
        conn = conectar_banco()
        cursor = conn.cursor()

        # buscar dados do usuário
        cursor.execute("""
            SELECT nome, matricula, email
            FROM usuarios
            WHERE id_usuario = %s
        """, (id_usuario,))
        usuario = cursor.fetchone()

        if not usuario:
            raise Exception("Usuário não encontrado.")

        nome, matricula, email = usuario

        # buscar tarefas do aluno
        cursor.execute("""
            SELECT nome_tarefa
            FROM tarefas
            WHERE id_usuario = %s
        """, (id_usuario,))
        tarefas = cursor.fetchall()

        cursor.close()
        conn.close()

        pasta = "pdfs"
        os.makedirs(pasta, exist_ok=True)
        data_str = datetime.now().strftime("%Y-%m-%d_%H-%M")
        nome_arquivo = f"{nome.replace(' ', '_')}_{data_str}.pdf"
        caminho = os.path.join(pasta, nome_arquivo)

        doc = SimpleDocTemplate(caminho, pagesize=A4)
        styles = getSampleStyleSheet()
        elementos = []

        # cabeçalho
        data_formatada = datetime.now().strftime("%d/%m/%Y")
        elementos.append(Paragraph("Dados do Aluno", styles['Title']))
        elementos.append(Paragraph(f"<i>Gerado em: {data_formatada}</i>", styles['Normal']))
        elementos.append(Spacer(1, 12))

        elementos.append(Paragraph(f"<b>Nome:</b> {nome}", styles['Normal']))
        elementos.append(Paragraph(f"<b>Matrícula:</b> {matricula}", styles['Normal']))
        elementos.append(Paragraph(f"<b>Email:</b> {email}", styles['Normal']))
        elementos.append(Spacer(1, 20))

        # titulo da lista de tarefas
        elementos.append(Paragraph("LISTA DE TAREFAS", styles['Heading2']))
        elementos.append(Spacer(1, 10))

        if tarefas:
            # criar tabela de tarefas
            data = [["Nº", "Tarefa"]] + [[str(i+1), t[0]] for i, t in enumerate(tarefas)]
            tabela = Table(data, colWidths=[30, 450])
            tabela.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ]))
            elementos.append(tabela)
        else:
            elementos.append(Paragraph("Nenhuma tarefa encontrada.", styles['Normal']))

        doc.build(elementos)
        return caminho

    except Exception as e:
        print(f"Erro ao gerar PDF: {e}")
        return None
