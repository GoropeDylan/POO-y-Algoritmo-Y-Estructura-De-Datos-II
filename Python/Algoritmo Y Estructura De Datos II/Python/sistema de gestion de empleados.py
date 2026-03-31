from abc import ABC, abstractmethod #->IMPORTAR LIBRERIA DE CLASES ABSTRACTAS
#--------------------------------------------CLASE ABSTRACTA EMPLEADO------------------------------------#
class Empleado(ABC):
    def __init__(self,nombre,DNI,salario_base): #->DEFINIMOS ATRIBUTOS
        self.nombre = nombre
        self.dni = DNI
        self.salario_base = salario_base
    def mostrar_datos(self): #->METODO NORMAL PARA MOSTRAR DATOS
        print(f'''Nombre: {self.nombre}
Documento: {self.dni}
salario: {self.salario_base}
------------------------------------------------------------------------------------------------''')
    @abstractmethod #->METODO ABSTRACTO PARA CREAR 
    def calcular_sueldo(self):
        pass
        
#---------------------------------------------CLASE EMPLEADO CONTRATADO-------------------------------------#    
class EmpleadoContratado(Empleado):
    def __init__(self, nombre, DNI, salario_base,horas_trabajadas,valor_hora):
        super().__init__(nombre, DNI, salario_base)#HEREDAR ATRIBUTOS
        self.valor_hora = valor_hora#ATRIBUTO ADICIONAL VALOR DE HORA
        self.horas_trabajadas = horas_trabajadas #ATRIBUTO ADICIONAL HORAS TRABAJADASr
        #CALCULAR SUELDO
    def calcular_sueldo(self):#METODO CALCULAR SUELDO
       self.salario_base = self.valor_hora*self.horas_trabajadas 
            
    def actualizar_datos(self):#METODO ACTUALIZAR DATOS ->CAMBIAR LAS HORAS TRABAJADAS
        self.horas_trabajadas = int(input("Cambie la cantidad de horas trabajadas: "))

#-----------------------------------------------CLASE EMPLEADO FIJO-----------------------------------------#
class EmpleadoFijo(Empleado):
    def __init__(self, nombre, DNI, salario_base,bono_antiguedad):
        super().__init__(nombre, DNI, salario_base)#HEREDAR ATRIBUTOS
        self.bono_antiguedad = bono_antiguedad #ATRIBUTO ADICIONAL BONO ANTIGUEDAD
        
    def calcular_sueldo(self):#METODO PARA CALCULAR SUELDO
        self.salario_base + self.bono_antiguedad
            
    def actualizar_datos(self):#METODO ACTUALIZAR DATOS -> CAMBIA LOS AÑOS DE ANTIGUEDAD
        self.bono_antiguedad = int(input("Ingrese años de antiguedad: "))
#--------------------------------------------FUNCIONES PARA EL SISTEMA-----------------------------------#       
def CrearEmpleado(): #CONTRATAMOS A UN EMPLEADO NUEVO
    Nombre = input("ingrese su nombre: ")
    dni = int(input("Ingrese su numero de DNI(sin puntos ni espacios): "))
    horas = int(input("ingrese la cantidad de horas trabajadas: "))
    valor = float(input("Ingrese el valor por hora: "))
    return EmpleadoContratado(Nombre,dni,0,horas,valor) #RETORNAMOS EL OBJETO

def CargarEmpleado():#CARGAMOS LOS DATOS DE UN EMPLEADO DE LA EMPRESA
    nombre = input("Ingrese su nombre: ")
    dni = int(input("Ingrese su numero de DNI: "))
    salario = float(input("Ingrese el salario base: "))
    return EmpleadoFijo(nombre,dni,salario,0)
#-----------------------------------------------PROBANDO SISTEMA--------------------------------------------#
#------>EMPLEADO 1:
E1 = CrearEmpleado()#CREAMOS EMPLEADO NUEVO
E1.calcular_sueldo()#CALCULAMOS SU SUELDO SEGUN LOS DATOS CARGADOS
E1.mostrar_datos()#MOSTRAMOS LOS DATOS DEL EMPLEADO NUEVO
E1.actualizar_datos()#ACTUALIZAMOS EN ESTE CASO LA CANTIDAD DE HORAS QUE TRABAJA
E1.calcular_sueldo()#CALCULAMOS SU SUELDO NUEVAMENTE
E1.mostrar_datos()#MOSTRAMOS DE NUEVO LOS DATOS DEL EMPLEADO NUEVO
#------>EMPLEADO 2:
E2 = CargarEmpleado()#CARGAMOS LOS DATOS DE UN EMPLEADO
E2.mostrar_datos()#MOSTRAMOS LOS DATOS DEL EMPLEADO
E2.actualizar_datos()#ACTUALIZAMOS EN ESTE CASO LA CANTIDAD DE AÑOS QUE LLEVA TRABAJANDO
E2.calcular_sueldo()#CALCULAMOS SU SUELDO SEGUN SU ANTIGUEDAD
E2.mostrar_datos()#MOSTRAMOS DE NUEVO LOS DATOS DEL EMPLEADO