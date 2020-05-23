from flask import Flask, render_template, request
from flask_restful import Resource, Api
from models import Pessoas

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    data = Pessoas.query.all()
    return render_template('index.html', data=data)


@app.route('/adm')
def adm():
    return render_template('adm.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/record', methods=['POST'])
def record():
    error = None
    email = request.form['email']
    nome = request.form['nome']
    foto = request.form['foto']
    desc = request.form['desc']
    pcd = request.form['pcd']
    pessoa = Pessoas.query.filter_by(email=email).first()
    if nome and foto and desc:
        pessoa.nome = nome
        pessoa.foto = foto
        pessoa.desc = desc
        pessoa.pcd =pcd
        pessoa.save()
        error = 'Ação realizada  com sucesso'
    else:
        error = 'Cadastre todos os dados'

    return render_template('adm.html', error=error, person=pessoa)


@app.route('/sign_in', methods=['POST'])
def sign_in():
    error = None
    email = request.form['email']
    passw = request.form['password']

    if email:
        p = Pessoas.query.filter_by(email=email, password=passw).first()
        if p:
            return render_template('adm.html', person=p)
        else:
            error = 'Usuário não encontrado por favor faça seu registro'

    else:
        error = 'Dados inválidos'

    return render_template('register.html', error=error, email=email)


@app.route('/create', methods=['POST'])
def create():
    error = None
    email = request.form['email']
    passw = request.form['password']
    re_pass = request.form['password_rep']
    if email:
        if passw == re_pass:
            p = Pessoas.query.filter_by(email=email).first()
            if p:
                error = 'Email já cadastrado no sistema'
            else:
                nP = Pessoas(email=email, password=passw)
                nP.save()

        else:
            error = 'Senhas não conferem'
    else:
        error = 'Dados inválidos'

    if error:
        return render_template('register.html', error=error, email=email)
    else:
        return render_template('adm.html', person=nP)


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
