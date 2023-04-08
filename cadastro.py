class Cadastro:
    def __init__(self,nome,cpf,sexo,idade):
        self.nome=nome
        self.__cpf=cpf
        self.sexo=sexo
        self.idade=idade

    def atendente(self):
        return "Responsável pelo atendimento ao público!"
    
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self,novo_cpf):
        self.__cpf= novo_cpf

