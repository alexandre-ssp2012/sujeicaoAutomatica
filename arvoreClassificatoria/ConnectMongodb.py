from pymongo import MongoClient

class ConnectMongodb:

    def getDbObrigacoesProducao(self):
        uri = 'mongodb://localhost/obrigacoes-producao'
        client = MongoClient(uri)
        db = client.get_default_database()
        return db

    def getDbObrigacoesProducaoLiberadas(self):
        uri = 'mongodb://localhost/obrigacoes-liberadas-producao'
        client = MongoClient(uri)
        db = client.get_default_database()
        return db


