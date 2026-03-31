class Padre():
    def reirse(self):
        print("Me rio como papa")
    
class Madre():
    def vocacion(self):
        print("Abogada")
    
class Hija(Padre,Madre):
    pass

#PRUEBA
juana = Hija()
juana.reirse()