from Veiculo import Veiculo

class Mota(Veiculo):
    def __init__(self, peso, cor, marca):
        super().__init__(cor, marca)
        self.__peso = peso

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    def receber_combustivel(self):
        print("Estou a receber combustível!")
