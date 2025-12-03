num=int(input("Indique o número: "))

match True:
    case _ if num < 0:
        print("O número é Negativo")

    case _ if num == 0:
        print("O número é Zero")

    case _ if num > 0:
        
        if num % 2 != 0:
            print("O número é positivo e ímpar")

        elif num % 2 == 0:
            print("O número é positivo e par")
        
        elif num % 3 == 0 and num % 5 == 0:
            print("O número é divisível por 3 e 5")

        else:
            print("Outros números positivos que não se encaixam em nenhuma das anteriores")         
         