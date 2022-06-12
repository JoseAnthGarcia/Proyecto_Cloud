class Node:
    def __init__(self, imagen, flavor, links):
        self.imagen = imagen
        self.flavor = flavor #flavor object
        self.links = links # list of link objets

    def add_node(self, node):
        self.links.append(node)