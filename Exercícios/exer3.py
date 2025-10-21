import os

player1=0
player2=0
again=True

while again:

    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    player1 = int(input("Player 1 indique que número deseja para jogar ao pedra, papel ou tesoura: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    player2 = int(input("Player 2 indique que número deseja para jogar ao pedra, papel ou tesoura: "))
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Player 1 escolheu: ", end="")
    match player1:
        case 1:
            print("Pedra")
        case 2:
            print("Papel")
        case 3:
            print("Tesoura")
        case _:
            print("Escolha Errada")

    print("Player 2 escolheu: ", end="")
    match player2:
        case 1:
            print("Pedra")
        case 2:
            print("Papel")
        case 3:
            print("Tesoura")
        case _:
            print("Escolha Errada")

    if player1 == player2:
        print("Empate!")
    elif (player1 == 1 and player2 == 3) or (player1 == 2 and player2 == 1) or (player1 == 3 and player2 == 2):
        print("Player 1 venceu!")
    else:
        print("Player 2 venceu!")

    resp = input("Queres jogar outra vez? (s/n): ")
    if resp != 's':
        again = False