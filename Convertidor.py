valor_prueba = int( input("ingrese el numero que desea convertir:"))

def Decimal2binario(numero):

    Binario = ""

    while numero //2 !=0 :

        Binario = str(numero%2) + Binario
        numero = numero // 2

    return str(numero) + Binario

valor_binario = Decimal2binario(valor_prueba)

def Decimal8octal(numero):

    Octal = ""

    while numero //8 !=0 :

        Octal = str(numero%8) + Octal
        numero = numero // 8

    return str(numero) + Octal

valor_octal = Decimal8octal(valor_prueba)

def Decimal16Hexadeximal(numero):

    Hexadecimal = ""

    while numero //16 !=0 :

        Hexadecimal = str(numero%16) + Hexadecimal
        numero = numero // 16

    return str(numero) + Hexadecimal

valor_hexadecimal = Decimal16Hexadeximal(valor_prueba)
print ("su numero {} en binario es {} en octal es {} en Hexadecimal es {}".format(valor_prueba, valor_binario, valor_octal, valor_hexadecimal))