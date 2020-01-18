import Mendoza_Gonzales.libreriA

#INPUT
cliente=Mendoza_Gonzales.libreriA.pedir_nombre("Ingrese Nombre del Cliente:")
dni=Mendoza_Gonzales.libreriA.pedir_Dni("Ingrese DNI:")
pt=Mendoza_Gonzales.libreriA.numero_camisas("Ingrese la cantidad de camisas:")

#PROCESSING
def proceso(intNc,costo):
    des=0.0
    pt=0.0
#Si se compran tres camisas o más se aplica un descuento del 20%
  if (intNc>=3 and intNc<12):
    des=costo*0.20
    pt=costo-des
    print("El costo total a pagar es ",pt)
#si son menos de tres camisas un descuento del 10%
  if (intNc<3):
    des = costo*0.10
    pt = costo-des
    print("El costo total a pagar es ",pt)
#si son mas de 12 camisas un descuento del 50%
  if (intNc>=12):
    des = costo*0.50
    pt = costo-des
    print("El costo total a pagar es ",pt)

#OUTPUT
Mendoza_Gonzales.libreriA.reporte_boleta(cliente,dni,pt)
