#CONDICIONAIS
temperatura = 102
if temperatura > 100:
    aguaFerve = True
    evaporacao = "muito rápida"
else: 
    aguaFerve = False
    evaporacao = "lenta"
aguaFerve
#True
evaporacao
# "muito rápida"

tempoDeJogo = int(input("Quanto tempo já temos jogados?  "))
if tempoDeJogo <= 90:
    print("O jogo ainda não acabou")
else:
    print("O jogo acabou")

#desafio: calcular raiz quadrada de um número. 
# quando não sei como fazer isso em python, pesquiso no google "python documentation square root".
# encontrei o módulo math.sqrt().
# primeiro: importar o módulo math > import math

import math
math.sqrt(25)
#5.0

#para o exercício: receber como entrada 3 valores "a", "b" e "c", que são as 3 constantes da fórmula de Bhaskara. Usando a fórmula de bhaskara, você vai imprimir as raízes. Temos 3 casos finais: se delta é <0 não tem raízes rais, se delta = 0 tem 1 raiz real e se delta > 0 tem 2 raízes reais.
import math
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b**2) - (4*a*c)

if delta < 0:
    #não existem raízes para número negativo
    print("Não existem raízes reais")
    quit()
else: 
    raizUm = (-b + math.sqrt(delta)) / (2*a)
    raizDois = (-b - math.sqrt(delta)) / (2*a)

if delta == 0.0:
    print("Existe uma raiz real")
else:
    print("Existem duas raízes reais")
quit()

