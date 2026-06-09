#salarios = [3000, 5000]

#funcionarios = ['Djavan', 'Osmar']

#for funcionario, salario in zip(salarios, funcionarios):
#	print (funcionario, salario)

salarios = [5000, 6000, 3400, 7000]

funcionarios = ['Osmar', 'Celso', 'Leandrinho', 'Deley'] 

dic_funcionarios = dict(zip(funcionarios, salarios))

print(dic_funcionarios['Osmar'])

