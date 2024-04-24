import re

ALPHABET_PATTERN = "[a-z]+\\d*"


class Graph:
    """
    Class for creating graph object from list
    of expressions
    """

    def __init__(self, nodes) -> None:
        """
        Precreate graph nodes from equations
        with empty sets as values
        """
        self.__graph = {node: set() for node in nodes}

    def add_edges(self, node: str, edges: set) -> None:
        """
        Method for adding edges to graph node
        :param node: expression
        :param edges: dependecies extracted from expression LHS
        """
        self.__graph[node] = self.__graph[node].union(edges)

    def __sort_by_dependencies_len(self) -> None:
        """
        Method for sorting nodes by length of edges
        """
        self.__graph = dict(
            sorted(
                self.__graph.items(),
                key=lambda val: len(val[0])))

    def __sort_by_inter_dependencies(self) -> None:
        """
        Method for sorting nodes by inter-depencies
        """
        self.__sorted_expressions: list = list()
        index_flag = 0
        for node, edges in self.__graph.items():
            node_var: str = node.split("=")[0].strip()

            if not self.__sorted_expressions or not edges:
                self.__sorted_expressions.insert(0, node)
                index_flag += 1
                continue

            last_dep_idx = index_flag

            for idx in range(len(self.__sorted_expressions)):
                comp_exp: str = self.__sorted_expressions[idx]
                comp_exp_var: str = (comp_exp.split("=")[0].strip(),)
                if edges.intersection(set(comp_exp_var)):
                    last_dep_idx = idx + 1

                    # Check for cylic dependency
                    if node_var in self.__graph[comp_exp]:
                        self.__sorted_expressions = ["cyclic_dependency"]
                        return

            self.__sorted_expressions.insert(last_dep_idx, node)

    def display_sorted_expressions(self):
        self.__sort_by_dependencies_len()
        self.__sort_by_inter_dependencies()
        return self.__sorted_expressions


def filter_dependencies(dependencies: str) -> str:
    """
    Expression dependencies filter
    :param dependencies: RHS of expression
    :return list of dependencies
    """
    return re.findall(ALPHABET_PATTERN, dependencies)


def sortExpressions(expressions: list) -> dict[str, str]:
    """
    Expression sorter
    :param expressions: list of expressions
    :return list of sorted expressions
    """

    exp_graph: Graph = Graph(expressions)

    for equation in expressions:
        lhs_rhs: list = equation.split(" = ")

        dependencies: list = filter_dependencies(lhs_rhs[1])
        exp_graph.add_edges(equation, set(dependencies))

    return exp_graph.display_sorted_expressions()
