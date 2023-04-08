from cadastro import Cadastro
from funcionario import Funcionario
from random import randint

nome=input("Digite seu nome:\n")
cpf=int(input("Digite seu cpf:\n"))
sexo=input("Digite seu sexo:\n")
idade=int(input("Digite sua idade:\n"))

codigo = randint (1000,9999)
funcioario=Funcionario(nome,cpf,sexo,idade)
print(f"Código do funcionário: {codigo}")

print(funcioario.atendente())

