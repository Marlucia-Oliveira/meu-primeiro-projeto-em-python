class Ninja():
    def __init__(self, nome, sobrenome, time, nivel):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__time = time
        self.__nivel = nivel

    def missoes(self):
        print(f"O {self.__nome} apto para missões referente ao seu nível")
