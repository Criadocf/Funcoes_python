salario = [(1000, 750, 200),
					(5000, 250, 100),
					(1200, 2000, 170)]
					
salario_atualizado = sorted(salario, key= lambda x: x[2], reverse= True)

#o 'x' é a tupla.
#dessa forma a ordenacao vai ser do 3° item das tuplas. no caso de forma decrescente. ja q o reverse esta True.

print(salario_atualizado)
