class Tamagotchi:

    def __init__(self, energiaMax: int, saciedadeMax: int, limpezaMax: int, idadeMax: int):
        self.energiaMax = energiaMax
        self.saciedadeMax = saciedadeMax
        self.limpezaMax = limpezaMax
        self.idadeMax = idadeMax
        self.energiaAtual = energiaMax
        self.saciedadeAtual = saciedadeMax
        self.limpezaAtual = limpezaMax
        self.estavivo = True
        self.diamantes = 0
        self.idade = 0

    def getEnergiaMax(self):
        return self.energiaMax

    def getSaciedadeMax(self):
        return self.saciedadeMax

    def getLimpezaMax(self):
        return self.limpezaMax

    def getIdadeMax(self):
        return self.idadeMax

    def getEnergiaAtual(self):
        return self.energiaAtual

    def getSaciedadeAtual(self):
        return self.saciedadeAtual

    def getLimpezaAtual(self):
        return self.limpezaAtual

    def getIdadeAtual(self):
        return self.idade

    def getDiamantes(self):
        return self.diamantes

    def getEstaVivo(self):
        if self.limpezaAtual > 0 and self.energiaAtual > 0 and self.saciedadeAtual > 0 and self.idade <= self.idadeMax:
            self.estavivo = True
            return True

    def brincar(self):
        self.energiaAtual -= 2
        self.saciedadeAtual -= 1
        self.limpezaAtual -= 3
        self.diamantes += 1
        self.idade += 1

    def comer(self):
        self.energiaAtual -= 1
        self.saciedadeAtual += 4
        self.limpezaAtual -= 2
        self.diamantes += 0
        self.idade += 1

    def dormir(self):
        if self.energiaAtual <= self.energiaMax - 5:
            self.energiaAtual = self.energiaMax
            self.saciedadeMax -= 2
            self.idade += 1

    def banhar(self):
        self.energiaAtual -= 3
        self.saciedadeAtual -= 1
        self.limpezaAtual = self.limpezaMax
        self.diamantes += 0
        self.idade += 2
