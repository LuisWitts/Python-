frase = str(input('Digite uma frase :')).upper().strip()
print('A letras a aparece {} vezes'.format(frase.count('A')))
print('A primeira letars a apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra a apareceu na posição {} '.format(frase.rfind('A')+1))
