from app.model.models import EmpresaModel

EMPRESA = EmpresaModel(indice=50, debitos = 0, notas= 0, nome = 'teste')

def test_addNotas():
    resultado = 5
    EMPRESA.addNotas(5)
    assert EMPRESA.notas == resultado

def test_addDebitos():
    result = 2
    EMPRESA.addDebitos(2)
    assert EMPRESA.debitos == result
    

def test_calculaIndice():
    resultado = 51
    assert EMPRESA.indice == resultado

def test_save():
    result = 