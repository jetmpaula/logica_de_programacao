# entrada de dados
nome = input("Informe o nome:")
idade = input("Informe sua idade: ")
altura = input("Informe sua altura: ").replace(',', '.')

# conversão de tipo
idade = int(idade)
altura = float(altura)

#saída de dados
print(f"Nome:{nome} Altura:{altura}")
print(f"Idade:{idade} Tipo:{(idade)}")
print(f"Altura:{altura} metros. Tipo:{(altura)}")

