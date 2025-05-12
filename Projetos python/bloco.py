while True:
    tamanho = int(input("Informe o tamanho:"))

    if tamanho <= 0:
        continue
    else:
        break

for _ in range(tamanho):
    print("#" * tamanho)