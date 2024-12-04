def main():
 número = int(input("Digite um número: "))
 par(número)
 
def par(número):
    if número % 2 == 0:
        print("é par")
    elif número % 2 >= 1:
       print("o número é impar")


main()
número = int(input("Digite um número: "))

if número % 2 == 0:
    print("o número é par")
else:
    print("o número é ímpar")