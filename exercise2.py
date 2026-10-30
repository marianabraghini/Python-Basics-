#entendendo valores booleanos 
x = 5 > 3
print(x) #True

y = 5 < 3
print(y)   #False

#chamando a classe
print(False)
# <class 'bool'>

print(x > 0)
# <class 'bool'>

# AND : ambas as condições precisam ser verdadeiras para retornar True
x > 0 and x **2 > 10
#True

x <0 and x == 12310
#False

# OR : apenas uma das condições precisa ser verdadeira para retornar True
x > 0 or x **2 > 10
#True

#NOT : inverte o valor booleano
x > 0 #True
not x > 0 #False
not False #True
not True #False
not not True #True

#ex: quero decidir se vou para a praia segunda feira se for feriado e se fizer sol 
fozerSol = True
praiaFeriado = False
vouParaPraia = fozerSol and praiaFeriado
vouParaPraia
#False
praiaFeriado = True
vouParaPraia = fozerSol and praiaFeriado
vouParaPraia
#True

#ex: ir pro show com um amigo se meu pai me der dinheiro ou se eu ganhar o ingresso de graça
dinheiroDoPai = False
ganheiIngresso = False
vouShow = dinheiroDoPai or ganheiIngresso
vouShow
#False
ganheiIngresso = True
vouShow = dinheiroDoPai or ganheiIngresso
vouShow
#True

