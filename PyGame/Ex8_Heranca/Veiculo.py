class Veiculo:
    def __init__(self, cor, marca):
        self._cor = cor
        self._marca = marca

    def get_cor(self):
        return self.__cor

    def set_cor(self, cor):
        self.__cor = cor

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def andar(self):
        print("Estou a andar!")

    def travar(self):
        print("Estou a travar!")

    def alterar_mudanca(self):
        print("Estou a mudar a mudança!")
