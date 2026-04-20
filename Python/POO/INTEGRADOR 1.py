#------------------------------------------VIBE STREAM----------------------------------------#
#CREANDO CLASE BASE
class Contenido():
    def __init__(self,titulo,duracion,cant_repro):
        self.titulo = titulo
        self._duracion = duracion
        self._cant = cant_repro
        
    def reproducir(self): #AGREGAR VISUALIZACIONES
        self._cant += 1
        
    @property #-> TRAEMOS AL ATRIBUTO PRIVADO
    def modificar_duracion(self):
        return self._duracion
    
    @modificar_duracion.setter #->LO MODIFICAMOS CON EL SETTER
    def modificar_duracion(self, valor):
        if valor >= 0:
            self._duracion = valor
        else: print("❌Valor ingresado incorrecto")
    #REPRESENTACION
    def __str__(self):
        return f'{self.titulo}|{self._duracion}|{self._cant}'
    def duracion_total(self):
        pass
#---------------------------------------------------------------------------------------------------
#HERENCIA - 2 CLASES HIJAS
class Pelicula(Contenido):
    def __init__(self, titulo, duracion, cant_repro,director):
        super().__init__(titulo, duracion, cant_repro)
        self.director = director
    def __str__(self):
        return f'{self.titulo}|dir: {self.director}|{self._duracion} min|{self._cant} reproduciones'
    def duracion_total(self):
        return f'Duracion de la pelicula: {self._duracion}'

class Series(Contenido):
    def __init__(self, titulo, duracion, cant_repro,episodios):
        super().__init__(titulo, duracion, cant_repro)
        self.episodios = episodios
    def __str__(self):
        return f'serie {self.titulo}|{self.episodios} episodios|{self._duracion} min por episodio|{self._cant} reproduciones'
    def duracion_total(self):
        return self._duracion * self.episodios
#FUNCION MOSTRAR CATALOGO
def mostrar_catalogo(lista):
    for i in lista:
        print(i)
        i.duracion_total()
#POLIMORFISMO - CALCULO DE DURACION TOTAL------------------------------------------------------------
lista = [Pelicula('El señor de los anillos',178,0,"Juan"),Pelicula('Shrek',90,0,"Pedro"),Series("Game of thrones",39,0,100),Series("los simpson",25,0,300)]
mostrar_catalogo(lista)