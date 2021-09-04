def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    return palabra == palabra_invertida


def run():
    texto = input('Escribe una palabra o enunciado: ')
    es_palindromo = palindromo(texto)
    if es_palindromo:
        print('Es palindromo FELICIDADES!!!')
    else:
        print('No es  palindromo, lo siento')


if __name__ == '__main__':
     run()