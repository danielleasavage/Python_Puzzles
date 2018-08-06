class Node:
    """
    class constructor should take one argument:
    dictionary with a name of the node as a key and a list of nodes it is
    connected to as value.
    For example
    Node({'A':['B','C']})

    Note 1,
    that the node may not have any connections, thus empty list is a
    legal dictionary value.
    >Node({'A':[]})

    Note 2,
    any other input to the node should result in an error.
    """

    def __init__(self, node_dict):
        if type(node_dict) == dict:
            node = list(node_dict.keys())
            if len(node) == 1 and type(node_dict[node[0]]) == list:
                self.node_dict = node_dict
                self.node = node[0]
                self.connections = node_dict[node[0]]
            else:
                raise ValueError(
                    'dictionary must contain infomation about a single node,' +
                    'node connections must be of type list')
        else:
            raise ValueError('node must be of type dict')

    def __str__(self):
        """
        returns string representation
        {"node:[vertex, vertex]}
        """
        return str(self.node_dict)


class Graph:

    def __init__(self, node_list=[]):
        """
        The constructor accepts a list of valid nodes, if no list is given,
        the graph is instantiated empty.
        """
        if all(type(n) == Node for n in node_list):
            self.node_list = node_list
            self.g = {}
            for n in node_list:
                self.g[n.node] = n
        else:
            raise ValueError('node_list contains invaild nodes')

    def add(self, node):
        """
        adds the node to the graph
        """
        if type(node) == Node:
            self.node_list.append(node)
            self.g[node.node] = node.connections
        else:
            raise ValueError('node must be of type Node')

    def delete(self, node):
        """
        deletes given node from the graph
        """
        self.node_list.remove(node)
        self.g.pop(node.node, None)

    def find_path_dfs(self, start_node, end_node):
        """
        return one path between start and end
        search is performed Depth-First
        Adapted from https://stackoverflow.com/questions/12864004/
        tracing-and-returning-a-path-in-depth-first-search?
        """
        stack = [(start_node.node, [start_node.node])]
        visited = []
        while stack:
            (vertex, path) = stack.pop()
            if vertex not in visited:
                if vertex == end_node.node:
                    return [self.g[v] for v in path]
                visited.append(vertex)
                for connection in self.g[vertex].connections:
                    stack.append((connection, path + [connection]))

        # If there is no path
        return []

    def find_path_bi(self, start_node, end_node):
        """
        return one path between start and end
        search is performed Bidirectional
        [Node 1, Node 2, Node 3]
        """
        # make this a queue instead of a stack to make better
        stackF = [(start_node.node, [start_node.node])]
        stackB = [(end_node.node, [end_node.node])]
        visitedF = []
        visitedB = []
        while stackF and stackB:
            (vertexF, pathF) = stackF.pop()
            if vertexF not in visitedF:
                if vertexF == end_node.node:
                    return [self.g[v] for v in pathF]
                visitedF.append(vertexF)
                for connectionF in self.g[vertexF].connections:
                    stackF.append((connectionF, pathF + [connectionF]))
            (vertex, pathB) = stackB.pop()
            if vertex not in visitedB:
                if vertex == start_node.node:
                    return [self.g[v] for v in pathB]
                visitedB.append(vertex)
                for connection in self.g[vertex].connections:
                    stackB.append((connection, [connection] + pathB))
        # If there is no path
        return []

    def find_all_paths(self, start_node, end_node):
        """
        returns a list with all paths between start and end, the list is empty
        if no path is found.
        bfs initally and extends to dfs whith out appending the end node
        to vistied
        """
        all_paths = []
        for c in start_node.connections:
            stack = [(c, [start_node.node, c])]
            visited = []
            while stack:
                (vertex, path) = stack.pop()
                if vertex not in visited:
                    if vertex == end_node.node:
                        new_path = [self.g[v] for v in path]
                        all_paths.append(new_path)
                    else:
                        visited.append(vertex)
                    for connection in self.g[vertex].connections:
                        stack.append((connection, path + [connection]))
        return [non_loop for non_loop in all_paths if
                len(non_loop) == len(set(non_loop))]

    def find_shortest_path(self, start_node, end_node):
        """
        returns the shortest path between start and end,
        or None if no path was found.
        """
        all_paths = self.find_all_paths(start_node, end_node)
        if all_paths != []:
            return min(all_paths, key=len)
        else:
            return None

    def has_route(self, start_node, end_node):
        """
        design an algorithm to return True if there is at least one path
        between start_node and end_node, otherwise returns False
        """
        a_path = self.find_path_dfs(start_node, end_node)
        if len(a_path) > 0:
            return True
        else:
            return False

    def print_path(self, path):
        """
        Given the path 'A' to 'B' to 'C', print the path in following format:
        'A'->'B'->'C'
        The node names have to come in order
        """
        path_w_names = [n.node for n in path]
        return '->'.join(path_w_names)

    def __str__(self):
        """
        returns a list representation with each node
        [{'A':['B','C']},{'D':['B','C']},{'B':['C','E']}]
        """
        string_list = [str(n) for n in self.node_list]
        string_joined = "[{}]".format(', '.join(string_list))
        return (string_joined)
