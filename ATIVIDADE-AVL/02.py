class celula:
  def __init__(self,valor,FE=None,FD=None):
    self.valor = valor
    self.fe = FE
    self.fd = FD
    
  def __str__(self):
    return 'No('+str(self.valor)+')'


def criaExemplo():
  r = celula(55)
  f1 = celula(10)
  f2 = celula(50)
  r.fe = f1
  r.fe.fd = f2
  return r

def rotacaoDuplaDir(no):
  aux = no
  r = aux.fe.fd
  r.fd = aux
  r.fe = aux.fe

  return r

r = criaExemplo()
r = rotacaoDuplaDir(r)

# print(r)
# print(r.fe)
# print(r.fd)