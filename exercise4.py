#entrada de dados

#conversor de fahrenheit para celsius
tempFahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
tempCelsius = (tempFahrenheit - 32) * 5/9
print("A temperatura em Celsius é: ", tempCelsius, "°C")


#conversor de segundos para horas, minutos e segundos

totalSegundos = int(input("Digite o total de segundos: "))

dias = totalSegundos // 86400 #segundos totais em um dia
horas = (totalSegundos % 86400) // 3600 #segundos restantes após calcular os dias
minutos = (totalSegundos % 3600) // 60 #pegando os segundos restantes e dividindo por minutos dentro de uma hora
segundos = totalSegundos % 60 #pegando os segundos restantes


print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")

repetir = input("Deseja repetir o programa? (s/n): ")
if repetir == "s":
    totalSegundos = int(input("Digite o total de segundos: "))

    dias = totalSegundos // 86400 #segundos totais em um dia
    horas = totalSegundos // 3600 #segundos totais numa hora
    minutos = (totalSegundos % 3600) // 60 #pegando os segundos restantes e dividindo por minutos dentro de uma hora
    segundos = totalSegundos % 60 #pegando os segundos restantes


    print(horas, "horas,", minutos, "minutos e", segundos, "segundos.")
else:
    print("Programa encerrado.")
quit()