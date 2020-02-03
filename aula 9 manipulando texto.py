
#fatiamento
#[9:13] = 9-12
frase = 'Curso em Video Pyhton'
frase[9:13:2]#do 9 até o 12 #2: pulando de 2 em dois

# analisar
len(frase) #comprimento da frase em caracteres
frase.count('o')#conta quantos 'o' tem na frase
frase.find('deo')#quantas vezes ele encontra 'deo' no video *aonde começa
frase.find('Andróid')# vai dar -1 se n existir essa str
'curso' in frase #dentro da frase existe a palavra curso ? , ele responde True or False

#transformação
frase.replace('Python', 'Android')#substitui  de uma forma secundaria
frase.upper()#ele deixa td maiusculas
frase.lower()#minusculas todas
frase.capitalize()#joga todos pra minuscula e a primeira letra fica maiuscula
frase.title()#quantas palavras tem essa string, , separadas e as primeiras letras de cada palavra fica maiuscula
frase.strip()# remove espaços inuteis nos começos e fim de strings
frase.rstrip()#remove somente do lado direito os espaços , o fim só
frase.lstrip()#só os da esquerda , começo só

#Divisão
frase.split()#divisão dentro da string considerando os espaços , lista com todas as palavras de uma string
'-'.join(frase)#juntar todos os elemntos de uma lista ,no caso por '-' mas da pra por espaço

