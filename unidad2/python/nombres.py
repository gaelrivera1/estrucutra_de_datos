from queue import Queue

class NumeroHandler:
    def __init__(self):
        self.pila = []
        self.cola = Queue()
        self.numeros_registrados = set()

    def agregar_numero(self, numero):
        if numero not in self.numeros_registrados:
            self.pila.append(numero)
            self.cola.put(numero)
            self.numeros_registrados.add(numero)
            print(f"Numero {numero} agregado con exito.")

    def mostrar_pila(self):
        print("Pila:", self.pila)

    def mostrar_cola(self):
        print("Cola:", list(self.cola.queue))

# Ejemplo de uso
if __name__ == "__main__":
    handler = NumeroHandler()

    handler.agregar_numero(10)
    handler.agregar_numero(20)
    handler.agregar_numero(10)  # Este número no se agregará debido a la repetición

    handler.mostrar_pila()
    handler.mostrar_cola()
