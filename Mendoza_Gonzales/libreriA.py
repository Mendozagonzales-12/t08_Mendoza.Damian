#Ejercicio1
#Funcion: Convertir una cadena en Formato Título
#Parametros: strTitulo
#Retorna:bool
def cadena_titulo(strTitulo):
    if(strTitulo.title()==True):
        return True
    else:
        return False
    #fin_if
#fin_cadena_titulo

#Ejercicio2
#Funcion: Saber si una cadena es numérica
#Parametros: strTexto
#Retorna:bool
def cadena_texto(strTexto):
    if(strTexto.isdigit()==True):
        return True
    else:
        return False
    #fin_if
#fin_cadena_texto

#Ejercicio3
# Funcion   : Verifica si intNum es un entero
# Parametros: intNum => Numero entero
# Retorna   : bool
def validar_entr(intNum):
    if ( isinstance(intNum, int)):
        return True
    else:
        return False
#fin_validar_numero

#Ejercicio4
# Funcion   : Verifica si intNum esta dentro de un rango
# Parametros: intNmr => Numero entero
#             intRangi => Rango inicial
#             intRangf=> Rango final
# Retorna   : bool
def validar_rang(intNmr, intRangi, intRangf):
    # 1. intNum, intRi e intRf deben ser enteros
    if ( validar_entr(intNmr) == False):
        return -1
    if ( validar_entr(intRangi) == False):
        return -2
    if ( validar_entr(intRangf) == False):
        return -3

    # 2. Rango Inicial no puede ser mayor o igual que Rango Final
    if ( intRangi >= intRangf ):
        return -4

    # 3. Numero entero debe estar dentro del rango
    if ( intNmr >= intRangi and intNmr <= intRangf ):
        return True     # num estan dentro del rango
    else:
        return -5       # num esta fuera del rango
#fin_validar_rango

#Ejercicio5
#Funcion: Validar si la cadena contiene solamente mayúsculas
#Parametros: strMayuscula
#Retorna:bool
def cadena_mayuscula(strMayuscula):
    if(strMayuscula.isupper()==True):
        return True                   #Es valido la caracteristica
    else:
        return False                  #No es valido
    #fin_if
#fin_cadena_mayuscula

#Ejercicio6
#Funcion: Validar si la cadena contiene solamente minúsculas
#Parametros:strMinuscula
#Retorna:bool
def cadena_minuscula(strMinuscula):
    if(strMinuscula.islower()==True):
        return True                   #Es valido la caracterisica
    else:
        return False                  #No es valido
    #fin_if
#fin_cadena_minuscula

#Ejercicio7
#Funcion: Convertir mayúsculas a minúsculas y viceversa
#Parametros: strPalabs
#Retorna: bool
def cadena_palabs(strPalabs):
    palabra=""
    if(strPalabs.swapcase()==True):
        return palabra
    else:
        return False
    #fin_if
#fin_cadena_palabs

#Ejercicio8
#Funcion:Validar y pedir si la cadena es DNI
#Parametros: intDNI
#Retorna: bool
def validar_DNI(intDNI):
    #1. El tipo de dato de intDNI es str
    #2. La longitud del entero es de 8 digitos
    if(isinstance(intDNI,str)):
        if(len(intDNI)==8):
            return True    #Es valido la caracteristica
        else:
            return False   #Insuficiente caracteristica
    else:
        return False       #No es valido
#fin_validar_DNI

def pedir_Dni(msj):
    dni=""
    while (validar_DNI(dni)==False):
        dni=input(msj)
    #fin_while
    return dni
#fin_pedir_Dni

#Ejercicio9
#Funcion: Validar si la cadena contiene solamente espacios en blanco
#Parametros: strEspacios
#Retornar: bool
def cadena_espacio(strEspacios):
    if(strEspacios.isspace()==True):
        return True                   #Es valido la cadena
    else:
        return False                  #No es valido
    #fin_if
#fin_cadena_espacios

#Ejercicio10
#Funcion: Validar si es la cadena es alfanumerica
#Parametro: strCadenaAL
#Retorno: bool
def cadena_alfanumerica(strCadenaAL):
    if(strCadenaAL.isalnum()==True):
        return True                   #valida que si es cadena_alfanumerica
    else:
        return False                  #Rechaza la validacion
    #fin_if
#fin_cadena_alfanumerica

#Ejercicio11
#Funcion: Validar  si la cadena es alfabética
#Parametros: strCadena
#Retorna:bool
def cadena_alfabetica(strCadena):
    if(strCadena.isalpha()==True):
        return True                #valida que si es cadena_alfabetica
    else:
        return False              #Rechaza la validacion
    #fin_if
#fin_cadena_alfabetica

#Ejercicio12
# Funcion   : Valida y pedir si es un nombre de persona
# Parametros: strNombre => Nombre de persona
# Retorna   : bool
def validar_nomb(strNombre):
    #1. El tipo de dato de strNombre es str
    #2. La longitud de la cadena es al menos de 3
    if ( isinstance(strNombre, str) ):
        if ( len(strNombre) >= 3):
            return True     # Es un nombre valido
        else:
            return False    # Insuficients caracteres
    else:
        return False        # No es str

#fin_validar_nombre

def pedir_nombre(msg):
    nombre=""
    while (validar_nomb(nombre) == False ):
        nombre=input(msg)
    #fin_while
    return nombre
#fin_pedir_nombre

#Ejercicio13
#Función: Pide el ingresar nombre
#Parametros: strSaludo => que muestra el saludo ¡Hola nombre!
#Retorna   : str
def saludo (strNombre):
   if ( strNombre):
        return "Hola "+ strNombre
#fin_saludo

#Ejercicio14
# Funcion   : Verifica si fltNum es un real
# Parametros: fltNum => Numero real
# Retorna   : bool
def validar_real(fltNum):
    if ( isinstance(fltNum, float)):
        return True
    else:
        return False
#fin_validar_numero

#Ejercicio15
#Funcion: Devuelve el descuento dependiendo del precio
#Parametros:intNc
#Retornar:str
def numero_camisas (intNc):
    #Si se compran tres camisas o más se aplica un descuento del 20%
    if (intNc>=3 and intNc<12):
        return "El descuento es del 20%"
    #si son menos de tres camisas un descuento del 10%
    if (intNc<3):
        return "El descuento es del 10%"
    #si son mas de 12 camisas un descuento del 50%
    if (intNc>=12):
        return "El descuento es del 50%"
    else:
        return " "
#fin_precio_des

def costo(intNc,flotPrecio):
    return round(intNc*flotPrecio,1)
#fin_costo

def reporte_boleta(cliente,pt,intDNI):
    print("#" * 32)
    print("# REPORTE DE BOLETA #")
    print("# Cliente:" + cliente)
    print("# DNI:"+str(dni))
    print("# Monto: S/." + str(pt))
    print("#" * 32)
