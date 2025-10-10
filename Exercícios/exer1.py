segundos = int(input("Diga um numero para converter de segundos para horas,minutos e segundos: "))
horas = segundos // 3600
restante = segundos % 3600
minutos = restante // 60
segundo = restante % 60

print(f"O número fica em {horas} hora(s),{minutos} minutos e {segundo} segundos")



