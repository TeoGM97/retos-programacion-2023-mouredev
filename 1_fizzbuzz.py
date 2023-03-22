#Enunciado:

# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

#Desarrollo:
for num in range(0,101):
    if num % 3 == 0 & num % 5 == 0:
        print('FizzFuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Fuzz')
    else:
        print(num)