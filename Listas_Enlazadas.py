
class Nodo:
	def __init__(self, dato):
		self.dato = dato
		self.siguiente = None

class ListaEnlazada:
	def __init__(self):
		self.cabeza = None

	def insertar_al_principio(self, dato):
		nuevo_nodo =  Nodo(dato)
		nuevo_nodo.siguiente = self.cabeza
		self.cabeza = nuevo_nodo

	def imprimir(self):
		nodo_actual = self.cabeza

		while nodo_actual:
			print(nodo_actual.dato, end = "->")
			nodo_actual = nodo_actual.siguiente

		print("Null")

# Instanciamos la clase

lista = ListaEnlazada()
lista.insertar_al_principio(2)
lista.insertar_al_principio(3)
lista.insertar_al_principio(4)
lista.insertar_al_principio(5)

lista.imprimir()