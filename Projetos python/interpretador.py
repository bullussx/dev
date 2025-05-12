def main():
 expressao = input("Digite a expressão (numero operador numero): ")

 numero1, operador, numero2 = expressao.split()

 numero1 = int(numero1)
 numero2 = int(numero2)

 calculo(numero1, operador, numero2)






def calculo(numero1, operador, numero2):
    if operador == "-":
        print(numero1 - numero2)
    elif operador == "+":
        print(numero1 + numero2)
    elif operador == "*":
        print(numero1 * numero2)
    elif operador == "/":
        print(numero1/numero2)
    elif operador == "**":
        print(numero1 ** numero2)
    else:
        print("Operador não identificado")
        

    return(numero1, operador, numero2)

main()