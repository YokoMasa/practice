class Dijkstra:

    def __init__(self, graph):
        self.graph = graph
        self.nodes = self.init_node_list()

    def the_best_way_to(self, goal_key):
        result = []
        check_flag = True
        current = self.nodes[goal_key]
        cost = current.cost
        result.append(current)

        while check_flag:
            if current.previous == "":
                check_flag = False
            else:
                current = self.nodes[current.previous]
                result.append(current)
        result.reverse()
        path_names = map(lambda r: r.name, result)
        print("cost: " + str(cost))
        print(" -> ".join(path_names))

    def set_start(self, start_key):
        self.start_key = start_key
        self.nodes = self.init_node_list()

        check_flag = True
        mother = self.nodes[start_key]
        mother.cost = 0
        mother.cost_defined = True
        mother.locked = True
        
        while check_flag:
           self.calc_cost()
           mother = self.get_smallest_unlocked()
           if mother is None:
               check_flag = False
           else:
               mother.locked = True
                

    def calc_cost(self):
        for key in self.nodes.keys():
            node = self.nodes[key]
            if not node.cost_defined:
                continue
            
            links = self.graph[node.name]
            for link in links:
                to_node = self.nodes[link.to]
                if not to_node.locked:
                    cost_from_start = node.cost + link.weight
                    if cost_from_start < to_node.cost:
                        to_node.cost = cost_from_start
                        to_node.previous = node.name
                        to_node.cost_defined = True

    def get_smallest_unlocked(self):
        result = None
        for key in self.nodes.keys():
            node = self.nodes[key]
            if not node.locked:
                if (result is None):
                    result = node
                else:
                    if (node.cost < result.cost):
                        result = node
        return result
                
        
    def init_node_list(self):
        node_list = {}
        for key in self.graph.keys():
            node_list[key] = Node(key)
        return node_list
    

class Node:

    def __init__(self, name):
        self.name = name
        self.cost = 10000000
        self.cost_defined = False
        self.locked = False
        self.previous = ""

    def get_name(self):
        return self.name

    def set_cost(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost

    def set_previous(self, name):
        self.previous = previous

    def get_previous(self):
        return self.previous

    def is_locked(self):
        return self.locked

    def set_locked(self, locked):
        self.locked = locked

    def print_content(self):
        text = "name: " + self.name + " cost: " + str(self.cost) + " previous: " + self.previous
        print(text)

import sys
import graph
if __name__ == "__main__":
    g = graph.load_graph(sys.argv[1])
    dijkstra = Dijkstra(g)
    dijkstra.set_start("C")
    dijkstra.the_best_way_to("B")
    
    
