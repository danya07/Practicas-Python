menu = """
Bienvenido al conversor de monedas

1 - Pesos mexicanos
2 - Pesos chilenos
3 - Pesos Canadienses jaja

Elije una opción:  """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿Cuántos pesos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 20.22
    dolares = pesos / valor_dolar
    dolares = str(dolares)
    print("Tienes $" + dolares + "dólares")
elif opcion == 2:
    pesos = input("¿Cuántos pesos chilenos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 783.97
    dolares = pesos / valor_dolar
    dolares = str(dolares)
    print("Tienes $" + dolares + "dólares")
elif opcion == 3:
    pesos = input("¿Cuántos Pesos Candienses tienes?: ")
    pesos = float(pesos)
    valor_dolar = 1.26
    dolares = pesos / valor_dolar
    dolares = str(dolares)
    print("Tienes $" + dolares + "dólares")
else:
    print("ingresa una opción correcta por favor")



