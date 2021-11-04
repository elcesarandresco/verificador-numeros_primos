def es_primo(numero):
    contador = 0
    for i in range(1, numero + 1):
        resultado = numero % i
        if resultado == 0:
            contador += 1
    
    if numero == 1:
        return False
    elif contador == 2:
        return True
    else:
        return False


def run():
    numero = input("Escriba el número que quiere verificar: ")
    numero = int(numero)
    if es_primo(numero) == True:
        print("El número " + str(numero) + " es primo.")
    else:
        print("El número " + str(numero) + " no es primo.")


if __name__ == '__main__':
    run()