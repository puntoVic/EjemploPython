def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break
    # texto = input('Escribe un texto: ')
    # for letra in texto:
    #     if letra =='o':
    #         break
    #     print(letra)
    LIMITE = 1000
    contador = 0 
    potencia_2 = 2**contador
    while potencia_2 < LIMITE: 
        print("2 elevado a "+ str(contador)+ "= " + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador
        if potencia_2 > 100:
            break

if __name__ == '__main__':
    run()