class celula:
  def __init__(self,valor,FE=None,FD=None):
    self.valor = valor
    self.fe = FE
    self.fd = FD
    
  def __str__(self):
    return 'No('+str(self.valor)+')'


def criaExemplo():
  r = celula(2)
  f1 = celula(4)
  f2 = celula(3)
  f3 = celula(6)
  r.fd = f1
  r.fd.fe = f2
  r.fd.fd = f3
  return r

def rotacaoEsq(no):
  aux = no
  r = aux.fd
  auxFdFe = r.fe
  r.fe = aux
  r.fe.fd = auxFdFe

  return r

r = criaExemplo()
r = rotacaoEsq(r)