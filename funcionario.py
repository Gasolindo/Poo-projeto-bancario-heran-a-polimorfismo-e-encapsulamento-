from cadastro import Cadastro
from random import*


class Funcionario(Cadastro):
    
    def numero_do_funcionario(self,nome,cpf,sexo,idade):
        super().__init__(self,nome,cpf,sexo,idade)
        
    def codigo(self):
        return (random)

    def atendente(self):
        return "Responsável por gerenciar os processos!"