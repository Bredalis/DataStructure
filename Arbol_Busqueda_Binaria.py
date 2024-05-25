
class ArbolNodo:
	def __init__(self, llave):
		self.llave = llave
		self.izquierda = None
		self.derecha = None

class ArbolBusquedaBinaria:
    def __init__(self, llave):
        self.llave = llave
        self.izquierda = None
        self.derecha = None

    def insertar(self, llave):
        self.arbol_nodo = self._insertar(self, llave)

    def _insertar(self, nodo, llave):

        if nodo is None:
            return ArbolBusquedaBinaria(llave)

        if llave < nodo.llave:
            nodo.izquierda = self._insertar(nodo.izquierda, llave)

        elif llave > nodo.llave:
            nodo.derecha = self._insertar(nodo.derecha, llave)

        return nodo

# Instanciamos la clase

arbol_busqueda_binaria = ArbolBusquedaBinaria(4)
arbol_busqueda_binaria.insertar(2)
arbol_busqueda_binaria.insertar(6)
arbol_busqueda_binaria.insertar(1)
arbol_busqueda_binaria.insertar(3)
arbol_busqueda_binaria.insertar(5)
arbol_busqueda_binaria.insertar(7)