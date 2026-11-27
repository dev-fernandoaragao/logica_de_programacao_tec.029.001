# entrada de dados
nome = input("Informe o seu nome: ").strip().title()
idade = int(input("Informe sua idade: "))

# estrutura de decisão
if idade >=18:
    print(f"{nome} é maior de idade.")
else:
    print(f"{nome} é menor de idade.")