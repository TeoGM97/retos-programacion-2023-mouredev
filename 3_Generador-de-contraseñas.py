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

    contrasena = []

    num_caract = int(input('Escribe el numero de caracteres que tendra la contraseña: '))

    wmay = str(input('Quieres que tenga mayuscula? (Si, No): ')).upper()
    wmin = str(input('Quieres que tenga minuscula? (Si, No): ')).upper()
    wnum = str(input('Quieres que tenga numeros? (Si, No): ')).upper()
    wsim = str(input('Quieres que tenga simbolos? (Si, No): ')).upper()
#Conditions
##1
    if wmay == 'NO':
        caracteres = minusculas + numeros + simbolos
        for i in range(num_caract):
            caracter_random = random.choice(caracteres)
            contrasena.append(caracter_random)
    elif wmin == 'NO':
        caracteres = mayusculas + numeros + simbolos
        for i in range(num_caract):
            caracter_random = random.choice(caracteres)
            contrasena.append(caracter_random)
    elif wnum == 'NO':
        caracteres = mayusculas + minusculas + simbolos
        for i in range(num_caract):
            caracter_random = random.choice(caracteres)
            contrasena.append(caracter_random)
    elif wsim == 'NO':
        caracteres = mayusculas + minusculas + numeros
        for i in range(num_caract):
            caracter_random = random.choice(caracteres)
            contrasena.append(caracter_random)
##2
#wmay
    elif (wmay == 'NO') & (wmin == 'NO'):
        caracteres = numeros + simbolos
        for i in range(num_caract):
            caracter_random = random.choice(caracteres)
            contrasena.append(caracter_random)
    elif (wmay == 'NO') & (wnum == 'NO'):
        caracteres = minusculas + simbolos
        for i in range(num_caract):
            caracter_random = random.choice(caracteres)
            contrasena.append(caracter_random)
    elif (wmay == 'NO') & (wsim == 'NO'):
        caracteres = minusculas + numeros
        for i in range(num_caract):
            caracter_random = random.choice(caracteres)
            contrasena.append(caracter_random)
#wmin
    elif (wmin == 'NO') & (wnum == 'NO'):
        caracteres = mayusculas + simbolos
        for i in range(num_caract):
            caracter_random = random.choice(caracteres)
            contrasena.append(caracter_random)
    elif (wmin == 'NO') & (wsim == 'NO'):
        caracteres = mayusculas + numeros
        for i in range(num_caract):
            caracter_random = random.choice(caracteres)
            contrasena.append(caracter_random)
#wnum
    elif (wnum == 'NO') & (wsim == 'NO'):
        caracteres = mayusculas + minusculas
        for i in range(num_caract):
            caracter_random = random.choice(caracteres)
            contrasena.append(caracter_random)
##3
#only sim
    elif (wmay == 'NO') & (wmin == 'NO') & (wnum == 'NO'):
        caracteres = simbolos
        for i in range(num_caract):
            caracter_random = random.choice(caracteres)
            contrasena.append(caracter_random)
#only num
    elif (wmay == 'NO') & (wmin == 'NO') & (wsim == 'NO'):
        caracteres = numeros
        for i in range(num_caract):
            caracter_random = random.choice(caracteres)
            contrasena.append(caracter_random)
#only may
    elif (wsim == 'NO') & (wmin == 'NO') & (wnum == 'NO'):
        caracteres = mayusculas
        for i in range(num_caract):
            caracter_random = random.choice(caracteres)
            contrasena.append(caracter_random)
#only min
    elif (wmay == 'NO') & (wsim == 'NO') & (wnum == 'NO'):
        caracteres = minusculas
        for i in range(num_caract):
            caracter_random = random.choice(caracteres)
            contrasena.append(caracter_random)
##0
    else:
        caracteres = mayusculas + minusculas + numeros + simbolos
        for i in range(num_caract):
            caracter_random = random.choice(caracteres)
            contrasena.append(caracter_random)

    contrasena = ''.join(contrasena)
    return contrasena

def run():
    contrasena = generar_contrasena()
    print('Tu nueva contrasena es: ')
    print('**************')
    print(' ')
    print(contrasena)
    print(' ')
    print('**************')


if __name__ == '__main__':
    run()