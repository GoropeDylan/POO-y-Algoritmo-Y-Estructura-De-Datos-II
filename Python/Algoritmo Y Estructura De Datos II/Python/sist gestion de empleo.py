class Empleado():#Clase Madre

    def __init__(self,Nombre, Cargo, Salario, Antiguedad):#Atributos

        
        self.nom = Nombre
        self.puesto = Cargo
        self.pago = Salario
        self.Anti = Antiguedad
    

class Trabajador(Empleado):#Clase Hija 
        pass
class Empleado_Contratado(Empleado):
   def __init__(self, valor_hora, horas_trabajadas ):
        
        self.valor_hora = valor_hora
        self.horas_trabajadas = horas_trabajadas
           
   def Calcular_Sueldo(self):
        self.sueldo_total= self.horas_trabajadas 
        
        print(f"El sueldo total es: {self.valor_hora*self.horas_trabajadas}")    


class Empleado_Fijo(Empleado):
     pass

        
    
trabajador1 =Empleado,Empleado_Contratado("Roberto", "Operario",  1200000 , "15 years",)   
trabajador2 = Trabajador("Aldana", "Gerente", 2500000 , "20 years")     
trabajador3 = Trabajador("Juan", "Seguridad", 1000000 , "5 years")


print(f"el nombre es: {trabajador1.nom} y su sueldo basico es {trabajador1.pago}")




