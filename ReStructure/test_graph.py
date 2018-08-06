from graph import *


def test_empty_node():
    """
    tests creation of empty node
    """
    assert type(Node({'A': []})) == Node


def test_error_node():
    """
    tests creation of bad node
    Node({'a':'a'})
    have to pass since the test is written to test error
    """
    try:
        Node({'a': 'a'})
        raised_error = False
    except:
        raised_error = True

    assert raised_error == True


def test_good_node():
    """
    tests creation of bad node
    Node({'A':['B','C']})
    """
    assert type(Node({'A': ['B', 'C']})) == Node


def test_node_str():
    """
    test that node representation of string is
    "{'name':['list','of','vertex']}"
    """
    test_node = Node({'A': ['B', 'C']})
    assert str(test_node) == "{'A': ['B', 'C']}"


def test_empty_graph():
    """
    tests creation of empty graph
    """
    assert type(Graph()) == Graph


def test_graph_with_list():
    """
    tests creation of the graph with a list of nodes
    node_list = []
    node_list.append(Node({'A':['B','C']}))
    node_list.append(Node({'B':['C','D']}))
    node_list.append(Node({'C':['D']}))
    node_list.append(Node({'D':['C']}))
    Graph(node_list)
    """
    node_list = []
    node_list.append(Node({'A': ['B', 'C']}))
    node_list.append(Node({'B': ['C', 'D']}))
    node_list.append(Node({'C': ['D']}))
    node_list.append(Node({'D': ['C']}))

    assert type(Graph(node_list)) == Graph


def test_graph_with_list_fail():
    """
    tests creation of the graph with a list
    node_list = ["slippery list"]
    node_list.append(Node({'A':"['B','C']"}))
    node_list.append(Node({'B':['C','D']}))
    node_list.append(Node({'C':['D']}))
    node_list.append(Node({'D':['C']}))
    Graph(node_list)
    error should be raised
    """
    node_list = ["slippery list"]
    node_list.append(Node({'A': ['B', 'C']}))
    node_list.append(Node({'B': ['C', 'D']}))
    node_list.append(Node({'C': ['D']}))
    node_list.append(Node({'D': ['C']}))
    try:
        Graph(node_list)
        raised_error = False
    except:
        raised_error = True

    assert raised_error == True


def test_add_to_graph():
    """
    create graph and add nodes in a loop
    """
    added = 0
    node_list = []
    node_list.append(Node({'A': ['B', 'C']}))
    node_list.append(Node({'B': ['C', 'D']}))
    node_list.append(Node({'C': ['D']}))
    node_list.append(Node({'D': ['C']}))
    test_g = Graph()
    for n in node_list:
        try:
            test_g.add(n)
            added += 1
        except:
            break
    assert added == 4


def test_graph_str():
    """
    test string representation of the graphs
    should be
    "[{'A':['B','C']}, {'B':['C','D']}, {'C':['D']}]"
    """
    node_list = [Node({'A': ['B', 'C']}), Node({'B': ['C', 'D']}),
                 Node({'C': ['D']})]
    test_g = Graph(node_list)
    assert str(test_g) == "[{'A': ['B', 'C']}, {'B': ['C', 'D']}, {'C': ['D']}]"


def test_find_path_dfs():
    """
    you should test with graphs that have 0, 1, 3 paths
    """
    n1 = Node({'A': ['B', 'C']})
    n2 = Node({'B': ['C', 'D']})
    n3 = Node({'C': ['D']})
    n4 = Node({'D': ['C']})
    n5 = Node({'E': []})
    node_list = [n1, n2, n3, n4, n5]
    test_g = Graph(node_list)

    assert test_g.find_path_dfs(n1, n5) == []  # no path
    assert test_g.find_path_dfs(n1, n2) != []  # one path
    assert test_g.find_path_dfs(n1, n3) != []  # three paths


def test_find_path_bi():
    """
    you should test with graphs that have 0, 1, 3 paths
    """
    n1 = Node({'A': ['B', 'C']})
    n2 = Node({'B': ['C', 'D']})
    n3 = Node({'C': ['D']})
    n4 = Node({'D': ['C']})
    n5 = Node({'E': []})
    node_list = [n1, n2, n3, n4, n5]
    test_g = Graph(node_list)

    assert test_g.find_path_bi(n1, n5) == []  # no path
    assert test_g.find_path_bi(n1, n2) != []  # one path
    assert test_g.find_path_bi(n1, n3) != []  # three paths


def test_find_all_paths():
    """
    you should test with graphs that have 0, 1, 3 paths
    """
    n1 = Node({'A': ['B', 'C']})
    n2 = Node({'B': ['C', 'D']})
    n3 = Node({'C': ['D']})
    n4 = Node({'D': ['C']})
    n5 = Node({'E': []})
    node_list = [n1, n2, n3, n4, n5]
    test_g = Graph(node_list)

    assert len(test_g.find_all_paths(n1, n5)) == 0  # no path
    assert len(test_g.find_all_paths(n1, n2)) == 1  # one path
    assert len(test_g.find_all_paths(n1, n3)) == 3  # three paths


def test_find_shortest_path():
    """
    you should test with graphs that have 0, 1, 3 paths
    """
    n1 = Node({'A': ['B', 'C']})
    n2 = Node({'B': ['C', 'D']})
    n3 = Node({'C': ['D']})
    n4 = Node({'D': ['C']})
    n5 = Node({'E': []})
    node_list = [n1, n2, n3, n4, n5]
    test_g = Graph(node_list)

    assert test_g.find_shortest_path(n1, n5) == None  # no path
    assert len(test_g.find_shortest_path(n1, n2)) == 2  # one path
    assert len(test_g.find_shortest_path(n1, n3)) == 2  # three paths


def test_has_route():
    """
    you should test with graphs that have 0, 1, 3 paths
    """
    n1 = Node({'A': ['B', 'C']})
    n2 = Node({'B': ['C', 'D']})
    n3 = Node({'C': ['D']})
    n4 = Node({'D': ['C']})
    n5 = Node({'E': []})
    node_list = [n1, n2, n3, n4, n5]
    test_g = Graph(node_list)

    assert test_g.has_route(n1, n5) == False
    assert test_g.has_route(n1, n2) == True
    assert test_g.has_route(n1, n3) == True
