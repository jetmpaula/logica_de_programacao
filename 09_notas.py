# atividade 05

#entrada de dados
nome = input("Informe o nome").strip().title()
nota1 = int(input("Informe a 1ª nota:"))
nota2 = int(input("Informe a 2ª nota:"))

#processamento de dados
media = (nota1+nota2)/2

#exibir a média
print(f"Média: {media}")

# estrutura de decisão
if media >= 7:
    print(f"{nome} está aprovdo.")
elif media >= 5:
    print(f"{nome} está de recuperação.")
else: 
    print(f"{nome} está reprovado")