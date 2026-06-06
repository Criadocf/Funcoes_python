#funcao filter. filtra itens d uma lista, baseada em uma funcao.

salarios = [3500, 1200, 4000, 1900, 2100, 200, 8500, 700]

novos_salarios = list(filter(lambda x: x > 2000, salarios))

print(novos_salarios)