salarios = [7000, 5000, 6000, 12000, 3000]
funcionarios = ['Kleber', 'André', 'Eduardo', 'Marta', 'Josue']

for salario, funcionario in zip(salarios, funcionarios):
	print('O salario de ', funcionario, 'é', salario)
	
#parecido com a funcao 'enumerate' so q mais simples, sem precisar 'percorrer' as listas.