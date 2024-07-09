def area(altura, largura):
    return altura*largura

def main():
    alt = input("Digite altura: ")
    larg = input("Digite largura: ")

    print("Area = ", area(int(alt), int(larg)))

if __name__ == '__main__':
    main()
