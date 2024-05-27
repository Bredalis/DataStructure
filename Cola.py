
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

# Instanciamos
cola = Cola()

for i in range(1, 4):
	cola.agregar_dato(i)

cola.borrar_dato()
print(cola.mostrar_datos())