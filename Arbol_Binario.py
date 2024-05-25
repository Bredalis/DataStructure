
class ArbolNodo:
	def __init__(self, llave):
		self.llave = llave
		self.izquierda = None
		self.derecha = None

# Instanciamos la clase

arbol_nodo = ArbolNodo(1)
arbol_nodo.izquierda = ArbolNodo(2)
arbol_nodo.derecha = ArbolNodo(3)