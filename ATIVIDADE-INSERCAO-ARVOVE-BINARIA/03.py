class celula:
    def __init__(self,valor,FE=None,FD=None):
        self.valor = valor
        self.fe = FE
        self.fd = FD
    def __str__(self):
        return 'No('+str(self.valor)+')'

r = celula(int(input()))
n1 = celula(int(input()))
n2 = celula(int(input()))

if(n1.valor > r.valor):
  if(r.fd == None):
    r.fd = n1
else:
  if(r.fe == None):
    r.fe = n1

if(n2.valor > r.valor):
  if(r.fd == None):
    r.fd = n2
else:
  if(r.fe == None): 
    r.fe = n2

print(r)
print(r.fe)
print(r.fd)