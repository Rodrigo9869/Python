print("este é o segundo script")

import os
opc=0
#saida=True

while True:#saida:
    os.system('cls')
    print("1 - Para receber um bom dia")
    print("2 - Para receber um boa tarde")
    print("3 - Para receber um boa noite")
    print("4 - Sair")

    opc=int(input("Introduza a opção: "))

    match opc:
        case 1:
            print("Bom dia")
        case 2:
            print("Boa tarde")
        case 3:
            print("Boa noite")
        case 4:
            #saida=False
            print("Adeus")
            break