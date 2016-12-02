from arvoreClassificatoria.BSTNode import BSTNode
from arvoreClassificatoria.BSTNode import BSTNodeObrigacao
from arvoreClassificatoria.ObrigacaoJson import ObrigacaoJson
from arvoreClassificatoria.SujeicaoAutomaticaRepository import ObrigacoesAcessoriasRepository

class MainObrigacaoJson:

    def run(self):
        obrigacaoAcessoriaRepository = ObrigacoesAcessoriasRepository()
        cursorAll = obrigacaoAcessoriaRepository.findObrigacoesAcessorias(False)
        cursor = obrigacaoAcessoriaRepository.findByChaveObrigacoesAcessorias("obrigacaoAcessoria_1399301985605", False)

        print("total de obrigações acessórias: ", cursorAll.count())
        print("obrigação acessória obrigacaoAcessoria_1399301985605: ", cursor)

        cursorLiberadasAll = obrigacaoAcessoriaRepository.findObrigacoesAcessorias(True)
        cursorLiberadas = obrigacaoAcessoriaRepository.findByChaveObrigacoesAcessorias("obrigacaoAcessoria_1393460088663", True)

        print("total de obrigações acessórias liberadas: ", cursorLiberadasAll.count())
        print("obrigação acessória obrigacaoAcessoria_1393460088663: ", cursorLiberadas)

        # obrigacaoJson = ObrigacaoJson()
        #
        # jsonDataSP = obrigacaoJson.jsonDataSP()
        # chaveObrigacao = jsonDataSP["chave"]
        #
        # arvoreSP = BSTNodeObrigacao(obrigacaoJson.dictCriterioValue_1["chaveCriterio"], obrigacaoJson.listaCriterioKey_1, obrigacaoJson.dictCriterioValue_1)
        # arvoreSP.right = BSTNodeObrigacao(obrigacaoJson.dictAplicabilidade_1["chaveAplicabilidade"], obrigacaoJson.listaAplicabilidade_1, obrigacaoJson.dictAplicabilidade_1)
        #
        # arvoreSP.left = BSTNodeObrigacao(obrigacaoJson.dictCriterioValue_2["chaveCriterio"], obrigacaoJson.listaCriterioKey_2, obrigacaoJson.dictCriterioValue_2)
        # arvoreSP.left.right = BSTNodeObrigacao(obrigacaoJson.dictAplicabilidade_2_1["chaveAplicabilidade"], obrigacaoJson.listaAplicabilidade_2_1, obrigacaoJson.dictAplicabilidade_2_1)
        # arvoreSP.left.right.right = BSTNodeObrigacao(chaveObrigacao)
        # arvoreSP.left.right.left = BSTNodeObrigacao(obrigacaoJson.dictAplicabilidade_2_2["chaveAplicabilidade"], obrigacaoJson.listaAplicabilidade_2_2, obrigacaoJson.dictAplicabilidade_2_2)
        # arvoreSP.left.right.left.right = BSTNodeObrigacao(chaveObrigacao)
        # arvoreSP.left.right.left.left = BSTNodeObrigacao(obrigacaoJson.dictAplicabilidade_2_3["chaveAplicabilidade"], obrigacaoJson.listaAplicabilidade_2_3, obrigacaoJson.dictAplicabilidade_2_3)
        # arvoreSP.left.right.left.left.right = BSTNodeObrigacao(chaveObrigacao)
        #
        # arvoreSP.left.left = BSTNodeObrigacao(obrigacaoJson.dictCriterioValue_3["chaveCriterio"], obrigacaoJson.listaCriterioKey_3, obrigacaoJson.dictCriterioValue_3)
        # arvoreSP.left.left.right = BSTNodeObrigacao(obrigacaoJson.dictAplicabilidade_3_1["chaveAplicabilidade"], obrigacaoJson.listaAplicabilidade_3_1, obrigacaoJson.dictAplicabilidade_3_1)
        # arvoreSP.left.left.right.right = BSTNodeObrigacao(chaveObrigacao)
        # arvoreSP.left.left.right.left = BSTNodeObrigacao(obrigacaoJson.dictAplicabilidade_3_2["chaveAplicabilidade"], obrigacaoJson.listaAplicabilidade_3_2, obrigacaoJson.dictAplicabilidade_3_2)
        # arvoreSP.left.left.right.left.right = BSTNodeObrigacao(chaveObrigacao)
        # arvoreSP.left.left.right.left.left = BSTNodeObrigacao(obrigacaoJson.dictAplicabilidade_3_3["chaveAplicabilidade"], obrigacaoJson.listaAplicabilidade_3_3, obrigacaoJson.dictAplicabilidade_3_3)
        # arvoreSP.left.left.right.left.left.right = BSTNodeObrigacao(chaveObrigacao)
        #
        # found = arvoreSP.getByOperators("usuário de equipamentos ECF")
        #
        # if found:
        #     print(found.key," - ", found.value)
        #     print(found.right.key," - ", found.right.value)
        # else:
        #     print("Não achou na arvore")
        #
        # found = arvoreSP.getByOperators("usuário de equipamentos ECF conteúdo da leitura da Memória Fiscal")
        #
        # if found:
        #     print(found.key, " - ", found.value)
        #     print(found.right.key, " - ", found.right.value)
        # else:
        #     print("Não achou na arvore")
        #
        # foundNone = arvoreSP.getByOperators("Nada aqui")
        # if foundNone:
        #     print(foundNone)
        # else:
        #     print("None")


