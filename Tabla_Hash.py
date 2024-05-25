
class TablaHash:
	def __init__(self):
		self.tabla = {}

	def insertar(self, clave, valor):
		self.tabla[clave] = valor

	def eliminar(self, clave):
		if clave in self.tabla:
			del self.tabla[clave]

	def mostrar(self, clave):
		return self.tabla.get(clave, None)

tabla = TablaHash()
tabla.insertar("a", 1)
tabla.insertar("b", 2)
tabla.insertar("c", 3)

tabla.eliminar("a")
print(tabla.mostrar("a"))