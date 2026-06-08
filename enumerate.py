salarios = [7000, 5000, 6000, 12000]
funcionarios = ['Kleber', 'André', 'Eduardo', 'Marta']

for c in salarios:
	print(c)
	
for c, salario in enumerate(salarios):
	funcionario = funcionarios[c]
	print('o salario do', funcionario, 'é de ', salario * 1.1)