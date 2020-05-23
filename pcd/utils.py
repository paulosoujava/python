from models import Pessoas


# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Malu', email="malu@soujava.com",
                     foto="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRwrWOat-RjwfiLmAZygxundwcIKlVez5ROCbefxXznkTqyailL&usqp=CAU",
                     desc="By utilizing elements and principles of Material Design, we were able to create a  framework that incorporates components and animations that provide more feedback to users. Additionally, a single underlying responsive system across all platforms allow for a moreunified user experience.")
    print(pessoa)
    pessoa.save()


# Realiza consulta na tabela pessoa
def     consulta_pessoas():
    return Pessoas.query.all()
    # pessoa = Pessoas.query.filter_by(nome='Rafael').first()


# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(email='Galleani').first()
    pessoa.nome = 'Felipe'
    pessoa.save()


# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(email='paulosoujava@gmail.com').first()
    pessoa.delete()


if __name__ == '__main__':
    # insere_pessoas()
    # altera_pessoa()
    exclui_pessoa()
    print(consulta_pessoas())
