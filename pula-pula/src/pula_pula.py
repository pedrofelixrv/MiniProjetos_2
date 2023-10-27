from src.crianca import Crianca


class PulaPula:

    def __init__(self, limiteMax):
        self.limiteMax = limiteMax
        self.fila_de_espera = []
        self.criancas_no_pulapula = []
        self.conta = 0
        self.caixa = 0

    def getFilaDeEspera(self):
        return self.fila_de_espera

    def getCriancasPulando(self):
        return self.criancas_no_pulapula

    def getLimiteMax(self):
        return self.limiteMax

    def getCaixa(self):
        return self.caixa

    def getConta(self, nome):
        for crianca in self.criancas_no_pulapula:
            if crianca.nome == nome:
                return self.conta

    def entrarNaFila(self, crianca: Crianca):
        if self.fila_de_espera:
            if self.criancas_no_pulapula:
                for crianca in self.criancas_no_pulapula:
                    if crianca.nome != crianca.nome:
                        self.fila_de_espera.append(crianca)
                        return True
                    return False
            else:
                self.fila_de_espera.append(crianca)
                return True
        else:
            self.fila_de_espera.insert(0, crianca)
            return True

    def entrar(self):
        if len(self.criancas_no_pulapula) < self.limiteMax and len(self.fila_de_espera) > 0:
            crianca = self.fila_de_espera[0]
            self.fila_de_espera.pop(0)
            self.criancas_no_pulapula.insert(0, crianca)
            self.conta += 2.50
            return True
        else:
            return False

    def sair(self):
        if len(self.criancas_no_pulapula) > 0:
            crianca = self.criancas_no_pulapula[0]
            self.criancas_no_pulapula.pop(0)
            self.fila_de_espera.append(crianca)
            return True
        return False

    def papaiChegou(self, nome):
        if self.criancas_no_pulapula:
            for crianca in self.criancas_no_pulapula:
                if crianca.nome == nome:
                    self.caixa += self.conta
                    self.conta = 0
                    return True
        elif self.fila_de_espera:
            for crianca in self.fila_de_espera:
                if crianca.nome == nome:
                    self.caixa += self.contas
                    self.conta = 0
                    self.fila_de_espera.remove(crianca)
                    return True
        return False

    def fechar(self):
        if self.criancas_no_pulapula:
            self.criancas_no_pulapula.clear()
            self.conta = None
        if self.fila_de_espera:
            self.fila_de_espera.clear()
            self.conta = None