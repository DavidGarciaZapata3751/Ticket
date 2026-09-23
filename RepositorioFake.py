class RepositorioFake:
    def __init__(self):
        self.compras = []

    def guardar(self, usuario, cantidad):
        self.compras.append({
            'usuario': usuario,
            'cantidad': cantidad
        })
        return True

#repo = RepositorioFake()
#repo.guardar("Ana", 2)
#repo.guardar("Luis", 3)
#print(repo.compras)    