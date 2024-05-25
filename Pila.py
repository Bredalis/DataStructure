
class Pila:
	def __init__(self):
		self.articulos = []

	def agregar_dato(self, articulo):
		self.articulos.append(articulo)

	def borrar_dato(self):

		# Borrar ultimo dato
		if not self.estado_vacio():
			return self.articulos.pop()

	def estado_vacio(self):
		return len(self.articulos) == 0

	def mostrar_datos(self):
		if not self.estado_vacio():
			return self.articulos[-1]

	def tamaño(self):
		return len(self.articulos)

# Instancia

pila = Pila()
pila.agregar_dato(1)
pila.agregar_dato(2)
pila.agregar_dato(3)
pila.borrar_dato()

print(pila.mostrar_datos())