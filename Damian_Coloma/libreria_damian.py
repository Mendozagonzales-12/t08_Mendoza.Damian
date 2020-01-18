#Ejercicio 1
#Funcion:Pide el ingresar nombre
#Parametros :strtFelicitacio => que muestre la felicitacion !feliz cumpleaños nombre!
#Retorna :str
def felicitacion (strNombre):
    if(strNombre):
        return "Feliz cumpleaños" + strNombre
#fin_felicitacion

#Ejercicio2
#Funcion:Pide la longiud de la palabra
#Parameros:strPalabra
#Retorna :bool
def palabra_longitud (strPalabra):
    if(isinstance(strPalabra,str)):
        if(len(strPalabra)== 5):
            return True
        else:
            return False
    else:
        return False
    #fin_if
#fin_palabra_longitud

#Ejercicio3
# Funcion   : Devuelve el producto de 4 numeros
# Parametros: n1, n2, n3, n4 => Numeros
# Retorna   : float
def producto(n1, n2, n3, n4):
    return round((n1*n2*n3*n4), 1)

#Ejercicio4
# Funcion   : Verifica si floatNumero es un real
# Parametros: floatNumero => Numero real
# Retorna   : bool
def validar_real(floatNumero):
    if ( isinstance(floatNumero,float)):
        return True
    else:
        return False
#fin_validar_numero

#Ejercicio5
#Funcion:Pide la longitud de la palabra
#Parametros:strNombre
#Retorna :bool
def nombre_longitud (strNombre):
    if(isinstance(strNombre,str)):
        if(len(strNombre)== 6):
            return True
        else:
            return False
    else:
        return False
    #fin_if
#fin_nombre_longitud

#Ejercicio6
# Funcion   : Verifica si strNombre es una palabra
# Parametros: strNombre => palabra
# Retorna   : bool
def validar_palabra(strNombre):
    if ( isinstance(strNombre,str)):
        return True
    else:
        return False
#fin_validar_palabra

#Ejercicio7
#Funcion:Pide la longitud de la frase
#Parametros:strFrase
#Retorna :bool
def frase_longitud(strFrase):
    if(isinstance(strFrase,str)):
        if(len(strFrase)== 9):
            return True
        else:
            return False
    else:
        return False
    #fin_if
#fin_validar_frase

#Ejercicio8
# Funcion   : Pide el ingreso de su codigo universitario
# Parametros: strMsg => Mensaje para input
# Retorna   : str
def pedir_codigo(msg):
    codigo=""
    while((codigo) == False):
        codigo=input(msg)
    #fin_while
    return codigo
#fin_pedir_codigo

#Ejercicio9
# Funcion   : Pide el ingreso de tu dni
# Parametros: strMsg => Mensaje para input
# Retorna   : str
def pedir_dni(msg):
    dni=""
    while((pedir_dni) == False):
        dni=input(msg)
    #fin_while
    return dni
#fin_pedir_dni

#Ejercicio10
#Funcion:Pide el ingresar nombre de trabajos realizados
#Parametros :strtMensaje => que muestre el mensaje ! excelente trabajo
#Retorna :str
def mensaje (strTrabajo):
    if(strTrabajo):
        return "excelente" + strTrabajo
#fin_mensaje

#Ejercicio11
# Funcion   : Devuelve la deuda promedio de 3 bancos diferentes
# Parametros: d1,d2,d3 => deudas
# Retorna   : float
def deuda_proemdio(d1, d2, d3):
    return round((d1+d2+d3)/3, 1)

#Ejercicio12
# Funcion   : Verifica si strpalabra es una cadena
# Parametros: strPalabra => Cadena
# Retorna   : bool
def validar_cadena(strPalabra):
    if ( isinstance(strPalabra, str)):
        return True
    else:
        return False
#fin_validar_cadena

#Ejercicio13
#Funcion:Pide la longitud del codigo
#Parametros:strcodigo
#Retorna :bool
def codigo_longitud (strcodigo):
    if(isinstance(strcodigo,str)):
        if(len(strcodigo)== 7):
            return True
        else:
            return False
    else:
        return False
    #fin_if
#fin_codigo_longitud

#Ejercicio14
# Funcion   : Devuelve la nota promedio de 5 alumnos
# Parametros: n1,n2,n3,n4,n5 => deudas
# Retorna   : float
def promedio(n1, n2, n3,n4,n5):
    return round((n1+n2+n3+n4+n5)/5, 1)

#Ejercicio15
# Funcion   : Devuelve la diferencia de edades
# Parametros: ed1,ed2,ed3 => deudas
# Retorna   : float
def diferencia(ed1, ed2, ed3):
    return round((ed1-ed2-ed3), 1)
