#-------------------------------------------CLASES--------------------------------------------------#
class Animal():
    def __init__(self,nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    def __str__(self):
        return f'''
Nombre:{self.nombre}
Especie:{self.especie}
edad:{self.edad}'''
#-----------------------------------------------------------------------------------------
class Libro():
    def __init__(self,titulo,autor,anio,disponible):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = disponible
    def esta_disponible(self):
        return self.disponible
    def __str__(self):
        return f'''
titulo{self.titulo}
autor: {self.autor}
año: {self.anio}
Estado: {self.disponible}'''
#-------------------------------------------------------------------------------------------