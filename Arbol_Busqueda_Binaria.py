
class ArbolNodo:
    def __init__(self, llave):
        self.llave = llave
        self.izquierda = None
        self.derecha = None

class ArbolBusquedaBinaria(ArbolNodo):
    def __init__(self, llave):
        super().__init__(llave)

    def insertar_nodo(self, llave):
        self.arbol_nodo = self._insertar_llave(self, llave)

    def _insertar_llave(self, nodo, llave):

        if nodo is None:
            return ArbolBusquedaBinaria(llave)

        if llave < nodo.llave:
            nodo.izquierda = self._insertar_llave(nodo.izquierda, llave)

        elif llave > nodo.llave:
            nodo.derecha = self._insertar_llave(nodo.derecha, llave)

        return nodo

# Instanciamos la clase
arbol_busqueda_binaria = ArbolBusquedaBinaria(4)

for i in range(0, 10, 2):
    arbol_busqueda_binaria.insertar_nodo(i)