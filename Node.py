
class Node:
    def __init__(self, a0, a1, a2, a3):
        self.id = a0
        self.descripcion = a1
        self.duracion = int(a2)
        self.dependencias = a3.split(' ')

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return "node: "+str(self.id)

