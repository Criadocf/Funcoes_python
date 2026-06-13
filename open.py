salario = [1500, 3000, 700, 9000]
funcionario = ['hose', 'frrnando', 'genriqur', 'diego']

#aqui eu crio o arquivo 'txt' q automaticamente é adicionado na pasta.
arquivo = open('novo_salario.txt', 'w', encoding="utf-8")


#aqui eu escrevo no arquivo que criei acima
for sal, func in zip(salario, funcionario):
	arquivo.write(f"o salário de {func} é {sal}\n")
arquivo.close()


