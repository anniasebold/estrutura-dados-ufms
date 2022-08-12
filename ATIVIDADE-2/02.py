class celula:
  def __init__(self, nome=None, idade=None, altura=None, prox=None):
    self.nome = nome
    self.idade = idade
    self.altura = altura
    self.prox = prox
  def __str__(self):
    return 'Celula('+str(self.nome)+','+str(self.idade)+','+str(self.altura)+')'


n1 = celula(input(),int(input()),float(input()))

n2 = celula(input(),int(input()),float(input()))

n1.prox = n2

n3 = celula(input(),int(input()),float(input()))

n2.prox = n3