def palindromo(texto):
    texto = texto.replace(' ', '')
    texto = texto.lower()
    texto_invertido = texto[::-1]
    return texto == texto_invertido


def run():
    texto = input('Escribe una palabra o enunciado: ')
    es_palindromo = palindromo(texto)
    if es_palindromo:
        print('Es palindromo FELICIDADES!!!')
    else:
        print('No es  palindromo, lo siento')


if __name__ == '__main__':
     run()