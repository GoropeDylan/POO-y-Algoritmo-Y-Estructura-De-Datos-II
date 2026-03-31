import random #LIBRERIA PARA PODER CREAR NUMERO DE CUENTA BANCARIA (sacado por IA)
#----------------------------------------------------CLASES--------------------------------------------------------------#
#DEFINIMOS CLASE PERSONA
class Persona():
    def __init__(self,nombre,apellido):#ATRIBUTOS
        self.nombre = nombre
        self.apellido = apellido
#DEFINIMOS CLASE Cliente       
class Cliente(Persona):
    def __init__(self, nombre, apellido,num,balance):#ATRIBUTOS TOTALES
        super().__init__(nombre, apellido)#ATRIBUTOS HEREDADOS
        self.Num = num
        self.balance = balance
        
    def imprimir_Datos(self):#METODO PARA IMPRIMIR DATOS BANCARIOS (capitalize() -> para mostrar nombre y apellido en mayuscula)
        print(f'''----------------------------------------------------------------------------------
Datos Bancarios:
Nombre:{self.nombre.capitalize()} 
Apellido:{self.apellido.capitalize()}
Numero de cuenta: {self.Num}
balance:${self.balance}  
----------------------------------------------------------------------------------''')
        input("Enter para continuar...")
           
    def depositar(self):#METODO PARA PODER DEPOSITAR DINERO A LA CUENTA BANCARIA
        monto = float(input("ingrese el monto que desea agregar a su cuenta: "))
        if monto<=0: 
            print("Ocurrio un ERROR, Monto ingresado incorrecto❌")
            input("Enter para continuar...")
        else:
            self.balance += monto
            input("Deposito realizado con exito✅,enter para continuar") 
            
    def retirar(self):#METODO PARA PODER RETIRAR DINERO (SI TIENE SALDO SUFICIENTE)
        retiro = float(input("Ingrese el monto que desea retirar de su cuenta: "))
        if retiro>self.balance: 
            print("Saldo insuficiente❌")#VERIFICAMOS QUE TENGA SALDO DISPONIBLE EN SU CUENTA
            input("Enter para continuar...")
        else: 
            self.balance -= retiro#RETIRAMOS SALDO DE SU CUENTA
            input("Transaccion realizada con exito✅,presione Enter para continuar")
            
#------------------------------------------FUNCIONES PARA EL SISTEMA---------------------------------------------#
#FUNCION PARA CREAR UN CLIENTE NUEVO AL BANCO         
def Crear_Cliente(): 
    nombre = input("Ingrese su nombre y presione enter: ").lower() #PEDIMOS NOMBRE DE USUARIO
    apellido = input("Ingrese su apellido y presione enter: ").lower() #PEDIMOS APELLIDO DE USUARIO
    NumeroDeCuenta = random.randint(10**21, 10**22 - 1) #FUNCION PARA PODER CREAR NUMERO DE CUENTA (sacado por IA)
    return Cliente(nombre,apellido,NumeroDeCuenta,0) #Balance = 0, ya que es una cuneta nueva
#FUNCION PRINCIPAL DE EJECUCION
def Menu():
    while True:
        print('''Seleccione una opcion: 
(1):imprimir informacion de cuenta
(2):depositar
(3):retirar
(0)salir''')
        op = int(input('->'))
        if op == 0: break
        elif op == 1: C1.imprimir_Datos()
        elif op == 2: C1.depositar()
        elif op == 3: C1.retirar()
        else: input("por favor elija una de las opciones anteriores, enter para continuar...")
        
#--------------------------------------------------SISTEMA PRINCIPAL----------------------------------------------------#
print("----------------------------------BANCO-------------------------------------")
C1 = Crear_Cliente()#CREANDO CLIENTE
Menu() #EJECUCION
print("gracias por usar el programa✅")