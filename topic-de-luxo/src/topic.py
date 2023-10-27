from passageiro import Passageiro


class Topic:
    def __init__(self, capacidade: int, qtdPrioritarios):
        self.capacidade = capacidade
        self.qtdPrioritarios = qtdPrioritarios
        self.qtdNormais = capacidade - qtdPrioritarios
        self.vagasDisponiveis = capacidade
        self.passageirosAssentoNormal = []
        self.passageirosAssentoPrioritario = []

    def getNumeroAssentosPrioritarios(self):
        if self.qtdPrioritarios > self.capacidade:
            return "IIlegalArgumentExpection"
        return "@", self.qtdPrioritarios

    def getNumeroAssentosNormais(self):
        return "=", self.qtdNormais

    def getPassageiroAssentoNormal(self, lugar):
        if 0 <= lugar <= len(self.qtdNormais):
            return self.passageirosAssentoNormal[lugar]
        else:
            return None

    def getPassageiroAssentoPrioritario(self, lugar):
        if 0 <= lugar <= len(self.qtdPrioritarios):
            return self.passageirosAssentoPrioritario[lugar]
        else:
            return None

    def getVagas(self):
        return self.vagasDisponiveis, "\n"

    def subir(self, passageiro: Passageiro):
        if self.vagasDisponiveis:
            if passageiro.idade >= 65:
                if len(self.passageirosAssentoPrioritario) < len(self.qtdPrioritarios):
                    self.passageirosAssentoPrioritario.append(Passageiro)
                    return True
                elif len(self.passageirosAssentoNormal) < len(self.qtdNormais):
                    self.passageirosAssentoNormal.append(Passageiro)
                    return True
            elif passageiro.idade < 65:
                if len(self.passageirosAssentoNormal) < len(self.qtdNormais):
                    self.passageirosAssentoNormal.append(Passageiro)
                    return True
                if len(self.passageirosAssentoPrioritario) < len(self.qtdPrioritarios):
                    self.passageirosAssentoPrioritario.append(Passageiro)
                    return True
            else:
                return False

    def descer(self, nome):
        if self.passageirosAssentoPrioritario.count(None) == 0:
            for i, passageiro in enumerate(self.passageirosAssentoPrioritario):
                if passageiro.nome == nome:
                    self.passageirosAssentoPrioritario.remove(passageiro)
                    self.vagasDisponiveis += 1
                    return True
            return False

    def toString(self):
        Topic = '['
        for a in range(self.qtdPrioritarios):
            if self.getPassageiroAssentoPrioritario(a):
                Topic += "@" + self.getPassageiroAssentoPrioritario(a).getNome() + ' '
            else:
                Topic += '@ '
        for a in range(self.qtdNormais):
            if self.getPassageiroAssentoNormal(a):
                Topic += '=' + self.getPassageiroAssentoNormal(a).getNome() + ' '
            else:
                Topic += '= '
                Topic += ']'
