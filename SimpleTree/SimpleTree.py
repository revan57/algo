class SimpleTreeNode:
    def __init__(self, val, parent):
        self.node_value = val
        self.parent = parent
        self.children = []


class SimpleTree:
    def __init__(self, root):
        self.root = root  # корень, может быть None

    def add_child(self, parent_node, new_child):
        try:
            if new_child.parent is not None:
                del new_child.parent.children[new_child.parent.children.index(new_child)]
        except ValueError:
            pass

        parent_node.children.append(new_child)
        new_child.parent = parent_node

    def delete_node(self, node_to_delete):
        try:
            del node_to_delete.parent.children[node_to_delete.parent.children.index(node_to_delete)]
        except ValueError:
            pass

        node_to_delete.parent.children.extend(node_to_delete.children)
        node_to_delete.parent = None

    def get_all_nodes(self):
        def recursive_walk(node, node_list):
            node_list.append(node)
            for el in node.children:
                recursive_walk(el, node_list)

            return node_list

        return recursive_walk(self.root, [])

    def find_nodes_by_value(self, val):
        def recursive_search(node, node_list):
            if node.node_value == val:
                node_list.append(node)
            for el in node.children:
                recursive_search(el, node_list)

            return node_list

        return recursive_search(self.root, [])

    def move_node(self, original_node, new_parent):
        self.add_child(new_parent, original_node)

    def count(self):
        def recursive_count(node, counter):
            counter += 1
            for el in node.children:
                counter = recursive_count(el, counter)

            return counter

        return recursive_count(self.root, 0)

    def leaf_count(self):
        def recursive_walk(node, counter):
            if len(node.children) == 0:
                counter += 1
            for el in node.children:
                counter = recursive_walk(el, counter)

            return counter

        return recursive_walk(self.root, 0)

    # find node depth by value
    def check_node_depth(self, val):
        def recursive_walk(node, increment, depth):
            if node.node_value == val:
                depth = increment
                return depth
            for el in node.children:
                depth = recursive_walk(el, increment + 1, depth)
            return depth

        depth = recursive_walk(self.root, 1, 0)

        return depth

    # set node depth
    def set_node_depth(self):
        def recursive_walk(node, depth):
            # node.depth = depth
            for el in node.children:
                recursive_walk(el, depth + 1)

        recursive_walk(self.root, 1)

    def get_node_depth(self, node):
        def recursive_walk(node, depth):
            depth += 1
            if node.parent is not None:
                depth = recursive_walk(node.parent, depth)

            return depth

        return recursive_walk(node, 0)
