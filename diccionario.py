def run():
    mi_diccionario = {
        'llave 1': 1,
        'llave 2': 2,
        'llave 3': 3,
    }

    # print(mi_diccionario['llave 1'])
    # print(mi_diccionario['llave 2'])
    # print(mi_diccionario['llave 3'])

    poblacion_paises = {
        'Mexico': 126014024,
        'Japon': 126050796,
        'USA': 332916000,
        'UK': 68207116,
    }

    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes ')


if __name__ == '__main__':
    run()