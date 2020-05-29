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

    def find_node_by_key(self, key):
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

        return _recursive_walk(self.Root, key) if self.Root else BSTFind()

    def add_key_value(self, key, val):
        bst_find = self.find_node_by_key(key)

        if not bst_find.NodeHasKey:
            if bst_find.Node:
                if bst_find.ToLeft:
                    bst_find.Node.LeftChild = BSTNode(key, val, bst_find.Node)
                else:
                    bst_find.Node.RightChild = BSTNode(key, val, bst_find.Node)
            else:
                self.Root = BSTNode(key, val, None)
            return True

        return False

    def find_min_max(self, FromNode, FindMax):
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

        if self.Root:
            return _find_max(FromNode) if FindMax else _find_min(FromNode)
        else:
            return None

    def delete_node_by_key(self, key):
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
            node_to_delete.Parent = None

        def _recursive_walk(node_to_delete, node):
            if node.LeftChild is None and node.RightChild is None:
                node.LeftChild = node_to_delete.LeftChild
                node.LeftChild.Parent = node
                if node_to_delete.RightChild != node:
                    node.RightChild = node_to_delete.RightChild
                    node_to_delete.RightChild.Parent = node
                    node.Parent.LeftChild = None
                if node_to_delete == self.Root:
                    self.Root = node
                    node.Parent = None
                else:
                    if node_to_delete.NodeKey > node_to_delete.Parent.NodeKey:
                        node_to_delete.Parent.RightChild = node
                    else:
                        node_to_delete.Parent.LeftChild = node
                    node.Parent = node_to_delete.Parent

            elif node.LeftChild is None:
                node.LeftChild = node_to_delete.LeftChild
                node.LeftChild.Parent = node
                if node_to_delete.RightChild != node:
                    node.Parent.LeftChild = node.RightChild
                    node.RightChild.Parent = node.Parent
                    node.RightChild = node_to_delete.RightChild
                    node_to_delete.RightChild.Parent = node
                if node_to_delete == self.Root:
                    self.Root = node
                    node.Parent = None
                else:
                    if node_to_delete.NodeKey > node_to_delete.Parent.NodeKey:
                        node_to_delete.Parent.RightChild = node
                    else:
                        node_to_delete.Parent.LeftChild = node
                    node.Parent = node_to_delete.Parent

            else:
                return _recursive_walk(node_to_delete, node.LeftChild)

        node = self.find_node_by_key(key)

        if node.NodeHasKey:
            if node.Node.LeftChild is None and node.Node.RightChild is None:
                _simple_delete_node(node.Node, None)
            elif node.Node.LeftChild is None or node.Node.RightChild is None:
                child_node = node.Node.LeftChild if node.Node.LeftChild else node.Node.RightChild
                _simple_delete_node(node.Node, child_node)
            else:
                _recursive_walk(node.Node, node.Node.RightChild)

        return node.NodeHasKey

    def count(self):
        def _recursive_count(node):
            if node is None:
                return 0
            return 1 + _recursive_count(node.LeftChild) + _recursive_count(node.RightChild)

        return _recursive_count(self.Root)

    def get_level_node(self, node, level):
        res = []
        if node is None:
            return []

        if level == 1:
            res.append(node)
            return res

        left = self.get_level_node(node.LeftChild, level - 1)
        res += left if left else res
        right = self.get_level_node(node.RightChild, level - 1)
        res += right if right else res

        return res if left or right else False

    def wide_all_nodes(self):
        level = 1
        result = []

        while True:
            res = self.get_level_node(self.Root, level)
            if not res:
                break
            else:
                result += res
            level = level + 1
        return result

    def deep_all_nodes(self, traversal_param):
        def in_order_traversal(node):
            res = []
            if node:
                res = in_order_traversal(node.LeftChild)
                res.append(node)
                res += in_order_traversal(node.RightChild)
            return res

        def post_order_traversal(node):
            res = []
            if node:
                res = post_order_traversal(node.LeftChild)
                res += post_order_traversal(node.RightChild)
                res.append(node)
            return res

        def pre_order_traversal(node):
            res = []
            if node:
                res.append(node)
                res += pre_order_traversal(node.LeftChild)
                res += pre_order_traversal(node.RightChild)
            return res

        if traversal_param == 0:
            return tuple(in_order_traversal(self.Root))
        elif traversal_param == 1:
            return tuple(post_order_traversal(self.Root))
        elif traversal_param == 2:
            return tuple(pre_order_traversal(self.Root))

        else:
            raise ValueError('Wrong traversal parameter.')

    def print_nodes(self, node):
        nodes = []
        if node.LeftChild:
            print(f"LChild: {node.LeftChild.NodeValue}, parent: {node.LeftChild.Parent.NodeValue}")
            nodes.append(node.LeftChild)
        if node.RightChild:
            print(f"RChild: {node.RightChild.NodeValue}, parent: {node.RightChild.Parent.NodeValue}")
            nodes.append(node.RightChild)

        for el in nodes:
            self.print_nodes(el)
