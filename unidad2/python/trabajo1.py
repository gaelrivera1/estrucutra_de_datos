from queue import Queue

class UniqueNumbersManager:
    def __init__(self):
        self.unique_numbers_set = set()
        self.number_queue = Queue()

    def add_number(self, number):
        if number not in self.unique_numbers_set:
            self.unique_numbers_set.add(number)
            self.number_queue.put(number)
            print(f"Número {number} añadido con éxito.")

        else:
            print(f"El número {number} ya está en la lista.")

    def display_numbers(self):
        print("Números únicos en la lista:")
        while not self.number_queue.empty():
            number = self.number_queue.get()
            print(number, end=" ")
        print()


if __name__ == "__main__":
    manager = UniqueNumbersManager()

    manager.add_number(5)
    manager.add_number(8)
    manager.add_number(5)  
    manager.add_number(12)
    manager.add_number(8)  

    manager.display_numbers()
