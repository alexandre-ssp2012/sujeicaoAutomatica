from arvoreClassificatoria.ConnectMongodb import ConnectMongodb

class ObrigacoesAcessoriasRepository:
    def __init__(self):
        self.connect = ConnectMongodb()

    def getDbObrigacaoAcessoria(self, isLiberadas):
        db = self.connect.getDbObrigacoesProducao() if isLiberadas else self.connect.getDbObrigacoesProducao()
        return db.obrigacaoAcessoria

    def findObrigacoesAcessorias(self, isLiberadas):
        obrigacaoAcessoria = self.getDbObrigacaoAcessoria(isLiberadas)
        return obrigacaoAcessoria.find()

    def findByChaveObrigacoesAcessorias(self, chave, isLiberadas):
        obrigacaoAcessoria = self.getDbObrigacaoAcessoria(isLiberadas)
        return obrigacaoAcessoria.find_one({"chave" : chave})



