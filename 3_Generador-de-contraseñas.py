#Enunciado:

# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar generar contraseñas con los siguientes parámetros:
# - Longitud: Entre 8 y 16.
# - Con o sin letras mayúsculas.
# - Con o sin números.
# - Con o sin símbolos.
# (Pudiendo combinar todos estos parámetros entre ellos)

#Desarrollo:

import random

def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracteres = mayusculas + minusculas + numeros + simbolos

    contrasena = []

    num_caract = int(input('Escribe el numero de caracteres que tendra la contraseña: '))

    wmay = str(input('Quieres que tenga mayuscula? (Si, No): '))
    wmin = str(input('Quieres que tenga mayuscula? (Si, No): '))
    wnum = str(input('Quieres que tenga mayuscula? (Si, No): '))
    wsim = str(input('Quieres que tenga mayuscula? (Si, No): '))
#Conditions
##1
    if wmay == 'No' | 'no' | 'NO':
        for i in range(num_caract):
            caracter_random = random.choice(caracteres[minusculas, numeros, simbolos])
            contrasena.append(caracter_random)
    elif wmin == 'No' | 'no' | 'NO':
        for i in range(num_caract):
            caracter_random = random.choice(caracteres[mayusculas, numeros, simbolos])
            contrasena.append(caracter_random)
    elif wnum == 'No' | 'no' | 'NO':
        for i in range(num_caract):
            caracter_random = random.choice(caracteres[mayusculas, minusculas, simbolos])
            contrasena.append(caracter_random)
    elif wsim == 'No' | 'no' | 'NO':
        for i in range(num_caract):
            caracter_random = random.choice(caracteres[mayusculas, minusculas, numeros])
            contrasena.append(caracter_random)
##2
#wmay
    elif (wmay == 'No' | 'no' | 'NO') & (wmin == 'No' | 'no' | 'NO'):
        for i in range(num_caract):
            caracter_random = random.choice(caracteres[numeros, simbolos])
            contrasena.append(caracter_random)
    elif (wmay == 'No' | 'no' | 'NO') & (wnum == 'No' | 'no' | 'NO'):
        for i in range(num_caract):
            caracter_random = random.choice(caracteres[minusculas, simbolos])
            contrasena.append(caracter_random)
    elif (wmay == 'No' | 'no' | 'NO') & (wsim == 'No' | 'no' | 'NO'):
        for i in range(num_caract):
            caracter_random = random.choice(caracteres[minusculas, numeros])
            contrasena.append(caracter_random)
#wmin
    elif (wmin == 'No' | 'no' | 'NO') & (wnum == 'No' | 'no' | 'NO'):
        for i in range(num_caract):
            caracter_random = random.choice(caracteres[mayusculas, simbolos])
            contrasena.append(caracter_random)
    elif (wmin == 'No' | 'no' | 'NO') & (wsim == 'No' | 'no' | 'NO'):
        for i in range(num_caract):
            caracter_random = random.choice(caracteres[mayusculas, numeros])
            contrasena.append(caracter_random)
#wnum
    elif (wnum == 'No' | 'no' | 'NO') & (wsim == 'No' | 'no' | 'NO'):
        for i in range(num_caract):
            caracter_random = random.choice(caracteres[mayusculas, minusculas])
            contrasena.append(caracter_random)
##3
#only sim
    elif (wmay == 'No' | 'no' | 'NO') & (wmin == 'No' | 'no' | 'NO') & (wnum == 'No' | 'no' | 'NO'):
        for i in range(num_caract):
            caracter_random = random.choice(caracteres[simbolos])
            contrasena.append(caracter_random)
#only num
    elif (wmay == 'No' | 'no' | 'NO') & (wmin == 'No' | 'no' | 'NO') & (wsim == 'No' | 'no' | 'NO'):
        for i in range(num_caract):
            caracter_random = random.choice(caracteres[numeros])
            contrasena.append(caracter_random)
#only may
    elif (wsim == 'No' | 'no' | 'NO') & (wmin == 'No' | 'no' | 'NO') & (wnum == 'No' | 'no' | 'NO'):
        for i in range(num_caract):
            caracter_random = random.choice(caracteres[mayusculas])
            contrasena.append(caracter_random)
#only min
    elif (wmay == 'No' | 'no' | 'NO') & (wsim == 'No' | 'no' | 'NO') & (wnum == 'No' | 'no' | 'NO'):
        for i in range(num_caract):
            caracter_random = random.choice(caracteres[minusculas])
            contrasena.append(caracter_random)
##0
    else:
        for i in range(num_caract):
            caracter_random = random.choice(caracteres)
            contrasena.append(caracter_random)

    contrasena = ''.join(contrasena)
    return contrasena

def run():
    contrasena = generar_contrasena()
    print('Tu nueva contrasena es: ' + contrasena)


if __name__ == '__main__':
    run()