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

    while True:
        num_caract = int(input('Escribe el número de caracteres que tendrá la contraseña (de 5 a 16 caracteres): '))
        if num_caract >= 5 and num_caract <= 16:
            break
        else:
            print('El número de caracteres debe ser de 5 a 16. Por favor, intenta de nuevo.')



    wmay = str(input('Quieres que tenga mayuscula? (Si, No): ')).upper()
    wmin = str(input('Quieres que tenga minuscula? (Si, No): ')).upper()
    wnum = str(input('Quieres que tenga numeros? (Si, No): ')).upper()
    wsim = str(input('Quieres que tenga simbolos? (Si, No): ')).upper()

#Conditions
    caracteres = []
    if wmay == 'SI':
        caracteres += mayusculas
    if wmin == 'SI':
        caracteres += minusculas
    if wnum == 'SI':
        caracteres += numeros
    if wsim == 'SI':
        caracteres += simbolos
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