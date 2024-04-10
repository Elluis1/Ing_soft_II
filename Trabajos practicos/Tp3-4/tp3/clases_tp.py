from builder import *

def llamadoFunciones():
    # punto 1
    print('Escriba el numero del que quiere saber el factorial: ')
    print(factorial(int(input())))

    # punto 2
    print('Ingrese el valor del que quiere recibir el calculo: ')
    print(calculoImpuestos(int(input())))

    # punto 3 (Lo hice por numeros para simplificar)
    print('De que manera quiere la entrega(1 = mostrador, 2 = retira el cliente, 3 = delivery): ')
    print(entregaFastFood(int(input())))

    # punto 4
    print('¿Que condicion impositiva tiene usted?(1 = IVA Responsable, 2 = IVA no inscripto, 3 = IVA Exento): ')
    print(condicionIVA(int(input())))
    
    # punto 5


# funcion punto 1 ( factorial )
def factorial (num):
    a = 1
    if num == 0 or num == 1:
        return 1
    elif num < 0:
        return 'Los numeros negativos no tienen factorial'
    else:
        while num > 1:
            a *= num
            num -= 1
        return a

# funcion punto 2 ( impuestos )
def calculoImpuestos(valor):
    if valor <= 0:
        return 'No hay nada que calcular'

    else:
        impuesto_1 = valor * 0.21
        impuesto_2 = valor * 0.05
        impuesto_3 = valor * 0.012

        total_impuestos = impuesto_1 + impuesto_2 + impuesto_3
        total_a_pagar = valor + total_impuestos

        return total_a_pagar

# funcion punto 3 ( "hamburguesa" )
def entregaFastFood(entrega):
    if entrega == 1:
        return 'La entrega se realizo por mostrador'
    elif entrega == 2:
        return 'La hamburguesa la retira el cliente'
    elif entrega == 3:
        return 'La hamburguesa es enviada por delivery'
    else:
        return 'No es una forma de entrega'

# funcion punto 4 ( "Factura" )
def condicionIVA(condicion):

    if condicion == 1: # Crea la factura si es IVA Responsable
        print('               Factura                     ')
        print('                                           ')
        print('Su condicion impositiva es: IVA Responsable')
        print('                                           ')
        print('                                           ')

    elif condicion == 2: # Crea la factura si es IVA no inscripto
        print('                Factura                     ')
        print('                                            ')
        print('Su condicion impositiva es: IVA no inscripto')
        print('                                            ')
        print('                                            ')

    elif condicion == 3: # Crea la factura si es IVA Exento
        print('               Factura                     ')
        print('                                           ')
        print('  Su condicion impositiva es: IVA Exento   ')
        print('                                           ')
        print('                                           ')

    else:
        return 'No es una condicion impositiva'

# funcion punto 5 ( "" )


llamadoFunciones()