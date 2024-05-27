
class Pila:
	def __init__(self):
		self.articulos = []

	def agregar_dato(self, articulo):
		self.articulos.append(articulo)

	def borrar_ultimo_dato(self):
		if not self.estado_vacio():
			return self.articulos.pop()

	def estado_vacio(self):
		return len(self.articulos) == 0

	def mostrar_datos(self):
		if not self.estado_vacio():
			return self.articulos[-1]

# Instancia

pila = Pila()

for i in range(1, 4):
	pila.agregar_dato(i)

pila.borrar_ultimo_dato()
print(pila.mostrar_datos())