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
    if self.tabela[pos] == self.codigo:
      self.tabela[pos] = chave
    else: 
      self.nColisoes += 1
  
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
print("Quantidade de Colisões:", t.nColisoes)