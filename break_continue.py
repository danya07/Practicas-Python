def run():
    # for contador in range(2999):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(29999):
    #     print(i)
    #     if i == 2345:
    #         break

    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'z':
            break
        print(letra)


if __name__ == '__main__':
    run()