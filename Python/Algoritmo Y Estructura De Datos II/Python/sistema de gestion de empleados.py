from abc import ABC, abstractmethod #->IMPORTAR LIBRERIA DE CLASES ABSTRACTAS
#CLASE ABSTRACTA EMPLEADO
class Empleado(ABC):
    def __init__(self,nombre,DNI,salario_base): #->DEFINIMOS ATRIBUTOS
        self.nombre = nombre
        self.dni = DNI
        self.salario_base = salario_base
        def mostrar_datos(self): #->METODO NORMAL PARA CREAR DATOS
            print(f'''Nombre: {self.nombre}
                  nro Documento: {self.dni}
                  salario: {self.salario_base}''')
            
        @abstractmethod #->METODO ABSTRACTO PARA CREAR 
        def calcular_sueldo(self):
            pass
        
#CLASE EMPLEADO CONTRATADO       
class EmpleadoContratado(Empleado):
    def __init__(self, nombre, DNI, salario_base,horas_trabajadas,valor_hora):
        super().__init__(nombre, DNI, salario_base)#HEREDAR ATRIBUTOS
        self.valor_hora = valor_hora#ATRIBUTO ADICIONAL VALOR DE HORA
        self.horas_trabajadas = horas_trabajadas #ATRIBUTO ADICIONAL HORAS TRABAJADASr
        #CALCULAR SUELDO
        def calcular_sueldo(self):#METODO CALCULAR SUELDO
            valor_hora*horas_trabajadas 
            
        def actualizar_datos(self):#METODO ACTUALIZAR DATOS
            self.horas_trabajadas = int(input("Cambie la cantidad de horas trabajadas: "))
            pass
        
#CLASE EMPLEADO FIJO
class EmpleadoFijo(Empleado):
    def __init__(self, nombre, DNI, salario_base,bono_antiguedad):
        super().__init__(nombre, DNI, salario_base)#HEREDAR ATRIBUTOS
        self.bono_antiguedad = bono_antiguedad #ATRIBUTO ADICIONAL BONO ANTIGUEDAD
        
        def calcular_sueldo(self):#METODO PARA CALCULAR SUELDO
            salario_base + bono_antiguedad
            
        def actualizar_datos(self):#METODO ACTUALIZAR DATOS
            self.bono_antiguedad = int(input("Ingrese años de antiguedad: "))
            pass
            
#---------------------------------PROBANDO SISTEMA-----------------------------------

E1 = EmpleadoContratado("Alexis","35.333.123",3000,8,40)
E2 = EmpleadoFijo("Bruno","30.501.911",8000,3000)
print(f'''Datos empleado 1
nombre: {E1.nombre}
DNI: {E1.dni}
salario base: US${E1.salario_base}
horas trabajadas: {E1.horas_trabajadas}
valor hora: US${E1.valor_hora}
      ''')