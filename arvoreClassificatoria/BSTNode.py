class BSTNode(object):

    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def get(self, key):
        """Retorna uma referência ao nó de chave key"""
        if self.key == key:
            return self
        node = self.left if key < self.key else self.right
        if node is not None:
            return node.get(key)

    def add(self, key):
        """Adiciona elemento à subárvore"""
        side = 'left' if key < self.key else 'right'
        node = getattr(self, side)
        if node is None:
            setattr(self, side, BSTNode(key))
        else:
            node.add(key)

    def remove(self, key):
        if key < self.key:
            self.left = self.left.remove(key)
        elif key > self.key:
            self.right = self.right.remove(key)
        else:
            # encontramos o elemento, então vamos removê-lo!
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            #ao invés de remover o nó, copiamos os valores do nó substituto
            tmp = self.right._min()
            self.key, self.value = tmp.key, tmp.value
            self.right._remove_min()
        return self

    def _min(self):
        """Retorna o menor elemento da subárvore que tem self como raiz.
        """
        if self.left is None:
            return self
        else:
            return self.left._min()

    def _remove_min(self):
        """Remove o menor elemento da subárvore que tem self como raiz.
        """
        if self.left is None:  # encontrou o min, daí pode rearranjar
            return self.right
        self.left = self.left._removeMin()
        return self


class BSTNodeObrigacao(object):

    def __init__(self, key, listOperators=None, value=None, left=None, right=None):
        self.key = key
        self.listOperators = listOperators
        self.value = value
        self.left = left
        self.right = right
        self.treeAccessed = False #no caso desta árvore já ter sido percorrida e ter atendido a pesquisa e setado com True

    def getByKey(self, key):
        """Retorna uma referência ao nó de chave key"""
        if key == self.key:
            return self
        node = self.left
        if node is not None:
            return node.getByKey(key)

    def getByOperators(self, operator):
        if operator in self.listOperators :
            if self.treeAccessed: # já foi usado, percorrido este nó da arvore, passa para o nó a esquerda
                node = self.left
                return node.getByOperators(operator)
            else:
                self.treeAccessed = True
                return self
        node = self.left
        if node is not None:
            return node.getByOperators(operator)
