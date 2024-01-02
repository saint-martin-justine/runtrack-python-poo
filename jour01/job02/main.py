class Operation:
    def __init__(self, nombre1: int, nombre2: int):
        
        self.nombre1 = nombre1
        self.nombre2 = nombre2

        print("Le nombre1 est : " + str(nombre1))
        print("Le nombre2 est : " + str(nombre2))

print(Operation(12, 3))