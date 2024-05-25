
from collections import deque

class Cola:
	def __init__(self):
		self.articulos = deque()

	def agregar_dato(self, articulo):
		self.articulos.append(articulo)

	def estado_vacio(self):
		return len(self.articulos) == 0

	def borrar_dato(self):

		if not self.estado_vacio():
			return self.articulos.popleft()

	def mostrar_datos(self):

		if not self.estado_vacio():
			return self.articulos[0]

	def tamaño(self):
		return len(self.articulos)

cola = Cola()
cola.agregar_dato(1)
cola.agregar_dato(2)
cola.agregar_dato(3)

cola.borrar_dato()
print(cola.mostrar_datos())