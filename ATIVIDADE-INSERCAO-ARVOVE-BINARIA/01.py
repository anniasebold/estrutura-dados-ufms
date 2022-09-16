class celula:
    def __init__(self,valor,FE=None,FD=None):
        self.valor = valor
        self.fe = FE
        self.fd = FD
    def __str__(self):
        return 'No('+str(self.valor)+')'

n1 = celula(3)
n2 = celula(11)
r = celula(7, n1, n2)