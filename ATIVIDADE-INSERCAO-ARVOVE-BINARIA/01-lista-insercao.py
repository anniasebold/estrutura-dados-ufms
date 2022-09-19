# A partir da implementação da nossa classe célula, implemente também a classe ABB.

# Essa classe deve ter como variável (componente) a raiz da árvore.

# Em seguida crie uma função dentro da classe ABB denominada teste.

# Dentro dessa função crie 3 células com os valores 4,3,5 e defina a componente raiz apontando para a célula 4.

class celula:
    def __init__(self,valor,FE=None,FD=None):
        self.valor = valor
        self.fe = FE
        self.fd = FD
    def __str__(self):
        return 'No('+str(self.valor)+')'

class arvoreBinaria:
  def __init__(self):
    self.raiz = None
  
  def buscaPai(self, valor):
    aux2 = None
    aux1 = self.raiz
    while(aux1!=None):
      aux2 = aux1
      if (valor < aux1.valor):
        aux1=aux1.fe
      else:
        aux1=aux1.fd
    return aux2

abb = arvoreBinaria()
r = celula(4)
a = celula(3)
b = celula(5)

r.fe = a
r.fd = b

print(r, r.fe, r.fd)