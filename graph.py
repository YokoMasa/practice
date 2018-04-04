import sys

class Node:

    def __init__(self, name):
        self.name = name
        self.links = []
        self.cost = 0

    def add_link(self, link):
        self.links.append(link)

    def get_links(self):
        return self.links

    def get_name(self):
        return self.name

    def set_cost(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost

    def to_string(self):
        string = "name:" + self.name
        for link in self.links:
            string += " | to:" + link.to + " weight: " + link.weight
        return string

class Link:

    def __init__(self, to, weight):
        self.to = to
        self.weight = weight

def load_graph(path):
    graph = []
    file = open(path, "r", encoding="utf-8")
    line = file.readline()
    while line != "":
        node = inflate_node(line)
        graph.append(node)
        line = file.readline()
    file.close()
    return graph

def inflate_node(string):
    args = string.split(",")
    node = Node(args[0])

    for i in range(1, len(args)):
        arg = args[i]
        link_data = arg.split(":")
        link = Link(link_data[0], link_data[1])
        node.add_link(link)

    return node
            
if __name__ == "__main__":
    path = sys.argv[1]
    for node in load_graph(path):
        print(node.to_string())
