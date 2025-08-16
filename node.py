class Node:
    def __init__(self, t, leaf = True):
        self.t = t
        self.keys = []
        self.children = []
        self.leaf = leaf

