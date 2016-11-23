from arvoreClassificatoria.BSTNode import BSTNode

class MainObrigacaoJson:

    def run(self):
        #obrigacaoJson = ObrigacaoJson()
        #obrigacaoJson.printJson()

        arvore = BSTNode(42, "bla bla 42")
        arvore.left = BSTNode(10, "bla bla 10")
        arvore.right = BSTNode(92, "bla bla 92")
        arvore.left.left = BSTNode(2, "bla bla 2")

        found = arvore.get(2)
        print(arvore.value)
        if found:
            print(found.value)

        foundNone = arvore.get(1001)
        if foundNone:
            print(foundNone)
        else:
            print("None")


