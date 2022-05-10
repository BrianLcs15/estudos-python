from random import choice
import string

valores = string.ascii_letters+ string.digits + string.punctuation
tamanho = 8
senha = ''

for i in range(tamanho):
    senha += choice(valores)

print('Sua nova senha é: ' +senha)
