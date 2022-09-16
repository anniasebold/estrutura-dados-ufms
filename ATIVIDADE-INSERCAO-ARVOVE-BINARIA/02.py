class celula:
    def __init__(self,valor,FE=None,FD=None):
        self.valor = valor
        self.fe = FE
        self.fd = FD
    def __str__(self):
        return 'No('+str(self.valor)+')'

class arvoreBinaria:
  # Inicializar nossa variavel raiz com vazia (None)!
  def __init__(self):
    self.raiz = None
  
  def buscaPai(self, valor):
    aux2 = None
    aux1 = self.raiz
    while(aux1!=None):
      if (valor < aux1.valor):
        aux1=aux1.fe
      else:
        aux1=aux1.fd
    return aux2
  # INSERÇÃO:
  # Encontrar o nó PAI
  # Conectar o nó PAI com o NOVO nó
  def insercao(self, valor):
    novo = celula(valor)
    if (self.raiz == None):
      self.raiz = novo
    else:
      pai = self.buscaPai(valor)
      if (valor < pai.valor):
        pai.fe = novo
      else:
        pai.fd = novo

abb = arvoreBinaria()
abb.insercao(10)