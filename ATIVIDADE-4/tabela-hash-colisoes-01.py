class TabelaHash:
  def __init__(self,M,codigo=-1):
    self.codigo = codigo
    self.tabela = [self.codigo]*M
    self.tamanho = M
    self.nColisoes = 0
  
  def hashFun(self,chave):
    pos = chave % self.tamanho
    return pos
  
  def inserir(self, chave):
    pos = self.hashFun(chave)
    while (self.temColisao(pos) == True): 
      self.nColisoes += 1
      pos = (self.hashFun(chave) + self.nColisoes) % self.tamanho
      self.temColisao(pos)
    self.tabela[pos] = chave
  
  def temColisao(self, pos):
    if self.tabela[pos] == self.codigo:
      return False
    else:
      return True
  
  def buscar(self, chave):
    pos = self.hashFun(chave)
    if self.tabela[pos] == chave:
      print("Encontrado na posição:", pos)
    else:
      print("Não encontrado")

t = TabelaHash(7)
t.inserir(int(input()))
t.inserir(int(input()))
t.inserir(int(input()))
t.inserir(int(input()))
t.inserir(int(input()))
t.inserir(int(input()))
print(t.tabela)