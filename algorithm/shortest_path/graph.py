import sys

class Link:
    def __init__(self, to, weight):
        self.to = to
        self.weight = int(weight)

def load_graph(path):
    graph = {}
    file = open(path, "r", encoding="utf-8")
    line = file.readline()
    while line != "":
        add_link(line, graph)
        line = file.readline()
    file.close()
    return graph

def add_link(string, graph):
    args = string.split(",")
    name = args[0]
    links = []

    for i in range(1, len(args)):
        arg = args[i]
        link_data = arg.split(":")
        link = Link(link_data[0], link_data[1])
        links.append(link)
    graph[name] = links
            
if __name__ == "__main__":
    path = sys.argv[1]
    graph = load_graph(path)
    for name in graph.keys():
        print("name: " + name)
        link_string = ""
        for link in graph[name]:
            link_string += "link_to: " + link.to + " weight: " + str(link.weight) + " "
        print(link_string)
