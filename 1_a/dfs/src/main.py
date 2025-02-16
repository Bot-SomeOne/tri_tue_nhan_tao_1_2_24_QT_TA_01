
from tabulate import tabulate

class Graph:
    """
        Graph class
    """
    def __init__(self, n, m, edges):
        """
            Constructor
            @param n : int
            @param m : int
            @param edges : dict {int: list}
        """
        self.n = n
        self.m = m
        self.edges = edges
        
def ReadInput(pathFile) -> Graph:
    """
        Read input and return graph object
        @param pathFile : str
        @return : Graph object or None if error occurred during reading input file
    """
    try:
        with open(pathFile, "r") as file:
            n, m = map(int, file.readline().split())
            edges = {}
            for _ in range(m):
                u, v = map(int, file.readline().split())
                if u not in edges:
                    edges[u] = []
                edges[u].append(v)
                
            return Graph(n, m, edges)
    except Exception as e:
        print(f"Error: {e}")
        return None

def DFS(graph, initState, goal):
    """
        Depth First Search
    """
    stack = [initState]
    visited = set()
    parent = {} # Help print path inti -> goal
    stepToStep = [] # Help print step to step
    
    parent[initState] = -1
    visited.add(initState)

    while stack:
        state = stack.pop()

        if state == goal:
            stepToStep.append([state, [], [], []])
            helpPrintHandle(stepToStep, parent, initState, goal, 0)
            return True
        
        for neighbor in graph.edges[state]:
            if neighbor not in visited:
                stack.append(neighbor)  
                visited.add(state)              
                parent[neighbor] = state
                
        stepToStep.append([state, graph.edges[state].copy(), stack.copy(), visited.copy()])
    
    helpPrintHandle(stepToStep, parent, initState, goal, 1)
    return False

def helpPrintHandle(dataTable, parent, initState, goal, typeState: int):
    """
        Print handle when use dfs
            - Table | expanded | adj | stack | visited |
            - Path to goal initState -> ... -> goal
            
        @param dataTable : list
        @param parent : dict
        @param initState : int
        @param goal : int
        @param typeState : int (0: true, 1: false)
    """
    helpPrintTable(dataTable)
    if typeState == 0:
        helpPrintPath(parent, initState, goal)

def helpPrintPath(parent, initState, goal):
    """
        Print path from initState to goal
        @param parent : dict
        @param initState : int
        @param goal : int
    """
    res = []
    while goal!= initState:
        res.append(goal)
        goal = parent[goal]
    res.append(initState)
    print("Path from initState to goal:")
    print("\t", res[::-1])

def helpPrintTable(dataTable):
    """
        Print table
        @param dataTable : list
    """
    p = tabulate(
        dataTable, 
        headers=["Expanded", "Adj", "Stack", "Visited"],
        tablefmt="pretty"
    )
    print(p)

def main():
    """
        Main function
    """
    pathFile = "src/input/data1.txt"
    graph = ReadInput(pathFile)
    if graph:
        print("Graph read successfully:")
        print("\t", graph.n, graph.m, graph.edges)
    else:
        print("Error: Can't read input file")
        
    initState = 0
    goal = 8
    if not DFS(graph, initState, goal):
        print(f"Goal {goal} not found.")
    else:
        print(f"Goal {goal} found!")
    
if __name__ == "__main__":
    main()