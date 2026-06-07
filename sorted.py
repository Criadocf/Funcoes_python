salario = [(1000, 750, 200),
					(5000, 250, 100),
					(1200, 2000, 170)]
					
salario_atualizado = sorted(salario, key= lambda x: x[2], reverse= True)

#dessa forma a ordenacao vai ser do 3° item das tuplas. no caso de forma decrescente. ja q o reverse esta True.

print(salario_atualizado)
