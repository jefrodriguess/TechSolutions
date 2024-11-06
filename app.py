from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Conexão com o banco de dados
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='techsolutions_db'
    )
#definição da pasta raiz INDEX
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        cidade = request.form['cidade']
        estado = request.form['estado']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO clientes (nome, email, telefone, cidade, estado) VALUES (%s,%s,%s,%s,%s)' , (nome, email, telefone, cidade, estado))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect('/clientes')
    
    return render_template('clientes.html')

@app.route('/funcionarios', methods=['GET', 'POST'])
def funcionarios():
    if request.method == 'POST':
        nome = request.form['nome']
        cargo = request.form['cargo']
        email = request.form['email']
        telefone = request.form['telefone']
        salario = request.form['salario']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO funcionarios (nome, cargo, email, telefone, salario ) VALUES (%s,%s,%s,%s,%s)' , (nome, cargo, email, telefone, salario))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect('/funcionarios')
    
    return render_template('funcionarios.html')

@app.route('/produtos', methods=['GET', 'POST'])
def produtos():
    if request.method == 'POST':
        nome = request.form['nome']
        categoria = request.form['categoria']
        preco = request.form['preco']
        quantidade_em_estoque = request.form['quantidade_em_estoque']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO produtos (nome, categoria, preco, quantidade_em_estoque) VALUES (%s,%s,%s,%s)' , (nome, categoria, preco, quantidade_em_estoque))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect('/produtos')
    
    return render_template('produtos.html')

@app.route('/vendas', methods=['GET', 'POST'])
def vendas():
    if request.method == 'POST':
        id_clientes = request.form['id_clientes']
        id_produtos = request.form['id_produtos']
        data_vendas = request.form['data_vendas']
        quantidade = request.form['quantidade']
        valor_total = request.form['valor_total']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO funcionarios (id_clientes, id_clientes, data_vendas, quantidade, valor_total ) VALUES (%s,%s,%s,%s,%s)' , (id_clientes, id_clientes, data_vendas, quantidade, valor_total ))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect('/vendas')
    
    return render_template('vendas.html')

if __name__ == '__main__':
    app.run(debug=True)



    
