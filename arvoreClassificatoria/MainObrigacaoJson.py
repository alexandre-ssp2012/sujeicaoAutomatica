from arvoreClassificatoria.BSTNode import BSTNode
from arvoreClassificatoria.BSTNode import BSTNodeObrigacao
from arvoreClassificatoria.ObrigacaoJson import ObrigacaoJson

class MainObrigacaoJson:

    def run(self):
        obrigacaoJson = ObrigacaoJson()
        # obrigacaoJson.printJson()

        # arvoreSP = BSTNode(42, "bla bla 42")
        # arvoreSP.left = BSTNode(10, "bla bla 10")
        # arvoreSP.right = BSTNode(92, "bla bla 92")
        # arvoreSP.left.left = BSTNode(2, "bla bla 2")

        arvoreSP = BSTNodeObrigacao(obrigacaoJson.listaCriterioKey_1, obrigacaoJson.dictCriterioValue_1)
        arvoreSP.right = BSTNodeObrigacao(obrigacaoJson.listaAplicabilidade_1, obrigacaoJson.dictAplicabilidade_1)

        arvoreSP.left = BSTNodeObrigacao(obrigacaoJson.listaCriterioKey_2, obrigacaoJson.dictCriterioValue_2)
        arvoreSP.right = BSTNodeObrigacao(obrigacaoJson.listaAplicabilidade_2_1, obrigacaoJson.dictAplicabilidade_2_1)
        arvoreSP.right.right = BSTNodeObrigacao(obrigacaoJson.dataSP["chave"])
        arvoreSP.right.left = BSTNodeObrigacao(obrigacaoJson.listaAplicabilidade_2_2, obrigacaoJson.dictAplicabilidade_2_2)

        arvoreSP.left.left = BSTNodeObrigacao(obrigacaoJson.listaCriterioKey_3, obrigacaoJson.dictCriterioValue_3)

        found = arvoreSP.get("importador")

        if found:
            print(found.value)
        else:
            print("Não achou na arvore")

        found = arvoreSP.get("equipamento ECF")

        if found:
            print(found.value)
        else:
            print("Não achou na arvore")

        foundNone = arvoreSP.get("Nada aqui")
        if foundNone:
            print(foundNone)
        else:
            print("None")


