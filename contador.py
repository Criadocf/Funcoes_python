#cria um contador, ou ao menos o efeito de um contador

from time import sleep

print('Começou')

for c in range(5):
	print(5-c, end="\r")
	sleep(1)
print('Terminou!')
	