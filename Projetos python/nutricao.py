def main():
    picaretas = {
        "madeira": "2x Gravetos, 3x Blocos de Madeiras",
        "pedra": "2x Gravetos, 3x Blocos de Pedra",
        "ferro": "2x Gravetos, 3x Barras de Ferro",
        "diamante": "2x Gravetos, 3x Diamantes",
        "netherite": "2x Gravetos, 3x Barras de Netherite"
    }

    pergunta = input("Qual o tipo da picareta? ").lower()

    if pergunta in picaretas:
        print(f"{picaretas[pergunta]}")
    else:
        print("Tipo NÃO ENCONTRADO, tente verificar a escrita")

main()