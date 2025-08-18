# btree.py
from provider import Provider
from node import Node

class BTree:
    def __init__(self, t):
        self.t = t
        self.root = Node(t)

    def is_empty(self):
        return len(self.root.keys) == 0

    def exists_id(self, provider_id, node=None):
        if node is None:
            node = self.root
        for provider in node.keys:
            if provider.provider_id == provider_id:
                return True
        if not node.leaf:
            for child in node.children:
                if self.exists_id(provider_id, child):
                    return True
        return False

    def search_by_service(self, service, node=None, results=None):
        if results is None:
            results = []
        if node is None:
            node = self.root
        for provider in node.keys:
            if provider.service.lower() == service.lower():
                results.append(provider)
        if not node.leaf:
            for child in node.children:
                self.search_by_service(service, child, results)
        return results

    def insert(self, provider):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            new_root = Node(self.t, leaf=False)
            new_root.children.append(self.root)
            self.split_child(new_root, 0)
            self.insert_non_full(new_root, provider)
            self.root = new_root
        else:
            self.insert_non_full(root, provider)

    def split_child(self, parent, index):
        t = self.t
        node_to_split = parent.children[index]
        new_node = Node(t, leaf=node_to_split.leaf)
        parent.keys.insert(index, node_to_split.keys[t - 1])
        parent.children.insert(index + 1, new_node)
        new_node.keys = node_to_split.keys[t:(2 * t - 1)]
        node_to_split.keys = node_to_split.keys[0:t - 1]
        if not node_to_split.leaf:
            new_node.children = node_to_split.children[t:(2 * t)]
            node_to_split.children = node_to_split.children[0:t]

    def insert_non_full(self, node, provider):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(provider)
            node.keys.sort()
        else:
            while i >= 0 and provider < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self.split_child(node, i)
                if provider > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], provider)

    def traverse(self, node=None):
        if node is None:
            node = self.root
        providers = []
        self._collect(node, providers)
        providers.sort(key=lambda p: p.rating, reverse=True)
        for p in providers:
            print(p)

    def _collect(self, node, providers):
        for i in range(len(node.keys)):
            if not node.leaf:
                self._collect(node.children[i], providers)
            providers.append(node.keys[i])
        if not node.leaf:
            self._collect(node.children[len(node.keys)], providers)
