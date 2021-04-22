from app import app
from app import db
'''
Este arquivo contem o classe contrutora do banco de dados
'''

class EmpresaModel(db.Model):
    '''Tabela no banco de dados com os dados da empresa

    Esta classe constrói a tabela EmpresaModel no banco de dados

    Atributes
    ---------
    nome : str
        nome da empresa
    indice : integer
        indice de crédito da empresa
    notas : integer
        quantidade de notas da empresa
    debitos : integer
        quantidade de débitos da empresa
    '''
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(100))
    indice = db.Column(db.Integer, default=50)
    notas = db.Column(db.Integer, default=0)
    debitos = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"EmpresaModel('{self.id}', '{self.nome}', '{self.indice}', '{self.notas}', '{self.debitos}')"

    def addNotas(self, nota):
        self.notas += nota
        self.calculaIndice()

    def addDebitos(self, debito):
        self.debitos += debito
        self.calculaIndice()

    def calculaIndice(self):
        self.indice = 50
        if self.notas != 0:
            self.indice = self.indice * ((1 + 0.02)**self.notas)
        if self.debitos != 0:
            self.indice = self.indice * ((0.96)**self.debitos)
        self.indice = round(self.indice)
        if self.indice > 100:
            self.indice = 100
        elif self.indice < 1:
            self.indice = 1

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def create(self, empresa):
        db.session.add(empresa)
        db.session.commit()



