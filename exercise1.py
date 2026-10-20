# observando precedência de operadores e associatividade
a = 2 + 3 * 4 - 5
print(a) #saída 9

b = 2 + 3 * (4 - 5)
print(b) #saída -1

#observando condições booleanas
# Exercício 1: Escreva um expressão em função de uma incógnita nota que resulte em True caso nota esteja no intervalo aberto (3.0, 5.0), e resulte em False caso contrário.Dica : A seguinte expressão em função de nota resulta em True para uma nota maior ou igual a 5. nota >= 5
c = 4 ; 3 < c < 5 # ou: x = 4 ; 3 < c and c < 5
print(c) #saída True

d = 2 ; 3 < d < 5 #ou: x = 2 ; 3 < d and d < 5
print(d) #saída False

# Exercício 2 : Um ano bissexto ocorre aproximadamente a cada 4 anos. Escreva uma expressão (em função de uma incógnita ano) que resulte em True caso ano seja bissexto e False caso contrário. Para ser bissexto, o valor de ano precisa ser múltiplo de 4, exceto múltiplos de 100 que não são múltiplos de 400. Assim o ano de 2020 é bissexto pois satisfaz todas essas condições.Dica: Use o operador % para verificar se ano é um múltiplo de algum número, como por exemplo: ano % 4 == 0
# Se ano=12, a expressão 12 % 4 == 0 resulta em True pois como 12 é múltiplo de 4 o resto da divisão (12%4) é zero.

ano = 2020 ; ano % 4 == 0
print(ano) #saída True

ano = 2023 ; ano % 4 == 0
print(ano) #saída False

