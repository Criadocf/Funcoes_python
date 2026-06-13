
#aqui eu faço a leitura do arquivo que eu criei... usando "with" com essa estrutura nao corro o risco d ter algum erro e o arquivo continuar aberto e atrapalhar novas açoes
with open('novo_salario.txt', 'r', encoding='utf-8') as arquivo:
	conteudo = arquivo.read()

print(f"SALÁRIO DOS FUNCIONÁRIOS\n{conteudo}")
