import ninja

class n3(ninja.Ninja):
    def __init__(self, nome, sobrenome, time, nivel):
        super().__init__(nome, sobrenome, time, nivel)