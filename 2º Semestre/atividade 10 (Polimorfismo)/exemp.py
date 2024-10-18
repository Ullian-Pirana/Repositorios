class Animal:
    def mover(self):
        return "se move"
    
class Cachorro (Animal):
    def mover(self):
        return "anda de 4"
    
class Peixe (Animal):
    def mover(self):
        return "nada"
    
class Lesma (Animal):
    pass

animal = Animal()
cachorro = Cachorro()
peixe = Peixe()
lesmo = Lesma()

print(animal.mover())
print(cachorro.mover())
print(peixe.mover())
print(lesmo.mover())