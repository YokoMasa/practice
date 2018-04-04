import sys

def load_graph(path):
    graph = []
    file = open(path, "r", encoding="utf-8")
    line = file.readline()
    while line != "":
        num_array = to_num_array(line)
        graph.append(num_array)
        line = file.readline()
    file.close()
    return graph

def to_num_array(string):
    num_array = []
    for char in string:
        try:
            num_array.append(int(char))
        except ValueError as e:
            pass
    return num_array
            
if __name__ == "__main__":
    path = sys.argv[1]
    print(load_graph(path))
