class Animal:
    # Atributo de clase
    especie = 'mamífer'
    posicio=0

    # El método __init__ es llamado al crear el objeto
    def __init__(self, nom, edat):
        print(f"Creant animal {nom}, {edat}")

        # Atributos de instancia
        self.nom = nom
        self.edat = edat
    
    def so(self):
        print("Som un animal")

    def menja(self,tipus):
        pass

    def camina(self):
        pass


class Ca(Animal):
    def so(self):
        print("guau guau")


a = Animal('pepe',12)
a.so()
b = Ca('paco',3)
b.so()
