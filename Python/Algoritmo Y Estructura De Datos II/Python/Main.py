class Auto():
    def __init__(self,marca,modelo,color):
        self.marca = marca #Atributo Público
        self._modelo = modelo #Atributo protegido
        self.__color = color #Atributo Privado
    def manejar(self): #METODO DE INSTANCIA AL OBJETO (SELF)
        print(f'''manejando:::
marca:{self.marca}
modelo:{self._modelo}
color:{self.__color}
            ''')
#CREANDO OBJETO
A1 = Auto('alfa romeo','146','rojo')
print(A1._modelo)
A1._modelo = '147'
A1.Auto__color = "Azul"
A1.manejar()