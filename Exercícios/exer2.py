num1 = int(input("Indique o primeiro número: "))
num2 = int(input("Indique o segundo número: "))
num3 = int(input("Indique o terceiro número: "))

if num1>num2>num3:
    print(f"Número {num1} é o maior, o do meio é o {num2} e o menor é o número {num3}")
elif num1>num3>num2:
    print(f"Número {num1} é maior, o do meio é o {num3} e o menor é o número {num2}")
elif num2>num1>num3:
    print(f"Número {num2} é maior, o do meio é o {num1} e o menor é o número {num3}")
elif num2>num3>num1:
    print(f"Número {num2} é o maior, o do meio é o {num3} e o menor é o número {num1}")
elif num3>num2>num1:
    print(f"Número {num3} é o maior, o do meio é o {num2} e o menor é o número {num1}")
elif num3>num1>num2:
    print(f"Número {num3} é o maior, o do meio é o {num1} e o menor é o número {num2}")
else:
    print("Não dá para deduzir qual o maior, do meio e o menor pois existem números iguais.")
