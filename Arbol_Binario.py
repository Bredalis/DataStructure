
# Nodo del Árbol Binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# Árbol Binario
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar_nodo(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar_nodo_recursivo(valor, self.raiz)

    def _agregar_nodo_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._agregar_nodo_recursivo(valor, nodo_actual.izquierdo)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._agregar_nodo_recursivo(valor, nodo_actual.derecho)

    def recorrido_inorden(self, nodo_actual):
        if nodo_actual:
            self.recorrido_inorden(nodo_actual.izquierdo)
            print(nodo_actual.valor, end = ' ')
            self.recorrido_inorden(nodo_actual.derecho)

    def buscar(self, valor, nodo_actual):
        if nodo_actual is None:
            return False
        if valor == nodo_actual.valor:
            return True
        elif valor < nodo_actual.valor:
            return self.buscar(valor, nodo_actual.izquierdo)
        else:
            return self.buscar(valor, nodo_actual.derecho)

# --- Ejemplo ---
if __name__ == "__main__":
    arbol = ArbolBinario()

    # Insertar valores
    for valor in [50, 30, 20, 40, 70, 60, 80]:
        arbol.agregar_nodo(valor)

    # Recorrido inorden (valores en orden ascendente)
    print("Recorrido Inorden del Árbol Binario:")
    arbol.recorrido_inorden(arbol.raiz)
    print()  # Nueva línea

    # Búsqueda de valor
    valor_buscado = 60
    if arbol.buscar(valor_buscado, arbol.raiz):
        print(f"El valor {valor_buscado} está en el árbol.")
    else:
        print(f"El valor {valor_buscado} NO está en el árbol.")