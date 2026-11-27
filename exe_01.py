# TODO: Crie um programa que receba do usuário o valor da gasolina e do etanol, e informe para o usuário qual o melhor combustível para se abastecer.
# NOTE: compensa mais bastecer com etanol caso o valor do etanol corresponda a até 75% do valor da gasolina.
# NOTE: e não se esqueça do detalhe mais importante de todos:
# DIVIRTAM-SE!!! :)

# entrada de dados
gasolina = float(input("Informe o valor da gasolina: ").replace(",","."))
etanol = float(input("Informe o valor do etanol: ").replace(",","."))

# estrutura de decisão
if etanol <= 75%gasolina:
    print(f"etanol")
else etanol >= 75%gasolina:
    print(f"gasolina")
