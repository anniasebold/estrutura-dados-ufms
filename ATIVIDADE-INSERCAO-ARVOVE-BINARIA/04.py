class celula:
  def __init__(self,valor,FE=None,FD=None):
    self.valor = valor
    self.fe = FE
    self.fd = FD
  def __str__(self):
    return 'No('+str(self.valor)+')'
  
def busca(raiz, valor):
  aux = raiz
  while(aux!=None):
    if(valor<aux.valor and aux.fe!=None):
      aux=aux.fe
    elif(valor>aux.valor and aux.fd!=None): 
      aux=aux.fd
    else:
      break
  return aux

a = celula(1)
b = celula(4)
n1 = celula(3,a,b)
n2 = celula(11)
r = celula(7,n1,n2)

nova = celula(int(input()))

p = busca(r, nova.valor)

if(nova.valor<p.valor):
  p.fe = nova
else: 
  p.fd = nova

print(p)
print(p.fe)
print(p.fd)