class Endereco:
    def __init__(self, rua: str, bairro: str, cidade: str):
        self.__rua = rua
        self.__bairro = bairro
        self.__cidade = cidade

    @property
    def rua(self):
        return self.__rua
    
    @property
    def bairro(self):
        return self.__bairro

    @property
    def cidade(self):
        return self.__cidade

    @rua.setter
    def rua(self, rua):
        self.__rua = rua

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade
