class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []


class SimpleTree:
    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        try:
            del NewChild.Parent.Children[NewChild.Parent.Children.index(NewChild)]
        except ValueError:
            pass

        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):
        try:
            del NodeToDelete.Parent.Children[NodeToDelete.Parent.Children.index(NodeToDelete)]
        except ValueError:
            pass

        NodeToDelete.Parent.Children.extend(NodeToDelete.Children)
        NodeToDelete.Parent = None

    def GetAllNodes(self):
        def recursive_walk(node, node_list):
            node_list.append(node)
            for el in node.Children:
                recursive_walk(el, node_list)

            return node_list

        return recursive_walk(self.Root, [])

    def FindNodesByValue(self, val):
        def recursive_search(node, node_list):
            if node.NodeValue == val:
                node_list.append(node)
            for el in node.Children:
                recursive_search(el, node_list)

            return node_list

        return recursive_search(self.Root, [])

    def MoveNode(self, OriginalNode, NewParent):
        self.AddChild(NewParent, OriginalNode)

    def Count(self):
        def recursive_count(node, counter):
            counter += 1
            for el in node.Children:
                counter = recursive_count(el, counter)

            return counter

        return recursive_count(self.Root, 0)

    def LeafCount(self):
        def recursive_walk(node, counter):
            if len(node.Children) == 0:
                counter += 1
            for el in node.Children:
                counter = recursive_walk(el, counter)

            return counter

        return recursive_walk(self.Root, 0)

    # find node depth by value
    def check_node_depth(self, val):
        def recursive_walk(node, increment, depth):
            if node.NodeValue == val:
                depth = increment
                return depth
            for el in node.Children:
                depth = recursive_walk(el, increment + 1, depth)
            return depth

        depth = recursive_walk(self.Root, 1, 0)

        return depth

    # set node depth
    def set_node_depth(self):
        def recursive_walk(node, depth):
            # node.depth = depth
            for el in node.Children:
                recursive_walk(el, depth + 1)

        recursive_walk(self.Root, 1)
