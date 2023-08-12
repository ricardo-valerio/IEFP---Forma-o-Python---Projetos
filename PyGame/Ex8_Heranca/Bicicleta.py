from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, tipo, material, cor, marca):
        super().__init__(cor, marca)
        self.__tipo = tipo
        self.__material = material

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def get_material(self):
        return self.__material

    def set_material(self, material):
        self.__material = material
