class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска
    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:
    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def FindNodeByKey(self, key):
        def _recursive_walk(node, key):
            if key == node.NodeKey:
                result = BSTFind()
                result.Node = node
                result.NodeHasKey = True
                return result

            if key > node.NodeKey:
                if node.RightChild is not None:
                    return _recursive_walk(node.RightChild, key)
                else:
                    result = BSTFind()
                    result.Node = node
                    result.NodeHasKey = False
                    return result
            else:
                if node.LeftChild is not None:
                    return _recursive_walk(node.LeftChild, key)
                else:
                    result = BSTFind()
                    result.Node = node
                    result.NodeHasKey = False
                    result.ToLeft = True
                    return result

        return _recursive_walk(self.Root, key)

    def AddKeyValue(self, key, val):
        bst_find = self.FindNodeByKey(key)

        if not bst_find.NodeHasKey:
            if bst_find.ToLeft:
                bst_find.Node.LeftChild = BSTNode(key, val, bst_find.Node)
            else:
                bst_find.Node.RightChild = BSTNode(key, val, bst_find.Node)

            return True

        return False

    def FinMinMax(self, FromNode, FindMax):
        def _find_min(node):
            if node.LeftChild is not None:
                return _find_min(node.LeftChild)
            else:
                return node

        def _find_max(node):
            if node.RightChild is not None:
                return _find_max(node.RightChild)
            else:
                return node

        return _find_max(FromNode) if FindMax else _find_min(FromNode)

    def DeleteNodeByKey(self, key):
        def _simple_delete_node(node_to_delete, child_node):
            if child_node:
                if node_to_delete == self.Root:
                    self.Root = child_node
                    child_node.Parent = None
                else:
                    child_node.Parent = node_to_delete.Parent
                    if node_to_delete.NodeKey > node_to_delete.Parent.NodeKey:
                        node_to_delete.Parent.RightChild = child_node
                    else:
                        node_to_delete.Parent.LeftChild = child_node
            else:
                if node_to_delete == self.Root:
                    self.Root = None
                else:
                    if node_to_delete.NodeKey > node_to_delete.Parent.NodeKey:
                        node_to_delete.Parent.RightChild = None
                    else:
                        node_to_delete.Parent.LeftChild = None

        def _recursive_walk(node_to_delete, node):
            if node.LeftChild is None and node.RightChild is None:
                if node_to_delete == self.Root:
                    self.Root = node
                    node.Parent = None
                    node.LeftChild = node_to_delete.LeftChild
                    node.RightChild = node_to_delete.RightChild
                else:
                    if node_to_delete.NodeKey > node_to_delete.Parent.NodeKey:
                        node_to_delete.Parent.RightChild = node
                    else:
                        node_to_delete.Parent.LeftChild = node
                node_to_delete.LeftChild.Parent = node
                node_to_delete.RightChild.Parent = node
            elif node.LeftChild is None:
                if node_to_delete == self.Root:
                    self.Root = node
                    node.Parent = None
                    node.LeftChild = node_to_delete.LeftChild
                    node.RightChild = node_to_delete.RightChild
                else:
                    node.RightChild.Parent = node.Parent
                    node.Parent.LeftChild = node.RightChild
                    node.Parent = node_to_delete.Parent
                    if node_to_delete.NodeKey > node_to_delete.Parent.NodeKey:
                        node_to_delete.Parent.RightChild = node
                    else:
                        node_to_delete.Parent.LeftChild = node
                    node_to_delete.LeftChild.Parent = node
                    node_to_delete.RightChild.Parent = node
            else:
                return _recursive_walk(node_to_delete, node.LeftChild)

        node = self.FindNodeByKey(key)

        if node.NodeHasKey:
            if node.Node.LeftChild is None and node.Node.RightChild is None:
                _simple_delete_node(node.Node, None)
            elif node.Node.LeftChild is None or node.Node.RightChild is None:
                child_node = node.Node.LeftChild if node.Node.LeftChild else node.Node.RightChild
                _simple_delete_node(node.Node, child_node)
            else:
                _recursive_walk(node.Node, node.Node.RightChild)

        return node.NodeHasKey

    def Count(self):
        def _recursive_count(node, counter):
            counter += 1
            if node:
                children_arr = []

                if node.LeftChild:
                    children_arr.append(node.LeftChild)
                if node.RightChild:
                    children_arr.append(node.RightChild)

                for el in children_arr:
                    counter = _recursive_count(el, counter)

            return counter

        return _recursive_count(self.Root, 0)
