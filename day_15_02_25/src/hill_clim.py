
import os
from tabulate import tabulate

class Data:
    """
       So dinh
       So Canh
       Cap gia tri canh     
       tra vang mang cap 3 phan tu
       [(dinh, dinh, gia tri), ...]
    """
    def __init__(self, path_file):
        self.path_file = path_file
        self.dinh = 0
        self.canh = 0
        self.data = {}
        
        self.process_create_data()
    
    def them_canh(self, u, v, w):
        if u not in self.data:
            self.data[u] = []
        if v not in self.data:
            self.data[v] = []
            
        self.data[u].append((v, w))
    
    def get_data(self):
        return self.data
    
    def process_create_data(self):
        f = open(self.path_file, "r")
        self.dinh = int(f.readline())
        self.canh = int(f.readline())
        for _ in range(self.canh):
            d = f.readline().strip('\n').split()
            if len(d) >= 3:
                u = int(d[0])
                v = int(d[1])
                w = int(d[2])
                self.them_canh(u, v, w)
        f.close()

# function hill climb
def hill_climb_search(graph, start, goal):
    """
        Hill climb search
    """
    pq = [] # (w, v) stack
    pq.append((0, start))
    
    visited = set() # set have func find value
    parent = {start: None}
    
    table = [] # print step to step
    
    while pq:
        w, u = pq.pop()
        
        if u in visited:
            continue
        visited.add(u)
        
        if u == goal:
            table.append([u, graph[u], [], []])
            print_table(table)
            print_path(parent, start, goal)
            return True
        
        lAdj = sorted(graph[u], key=lambda x: (x[1], x[0]), reverse=True)
        
        for v, weight in lAdj:
            if v not in visited:
                parent[v] = u
                pq.append((weight, v))
        
        st_show = pq.copy()
        st_show.reverse()
        
        table.append([
                u, 
                graph[u], 
                sorted(lAdj.copy(), key=lambda x: (x[1], x[0])),
                st_show
        ]) 

    print_table(table)
    print("Khong tim thay duong di!")
    return False

# print table data 
def print_table(data):
    """
        Print table
    """
    data_print = []
    for i in range(len(data)):
        st = []
        for j in range(len(data[i][3])):
            st.append([data[i][3][j][1], data[i][3][j][0]])
        data_print.append([data[i][0], data[i][1], data[i][2], st])
        
    print(tabulate(
        data_print, 
        headers=["Dinh", "Canh", "List adj", "Stack"], 
        tablefmt="pretty"))

# print path
def print_path(parent, start, goal):
    """
        Print path
    """
    cur = goal
    path = []
    while cur != start:
        path.append(cur)
        cur = parent[cur]
    path.append(start)
    path.reverse()
    print(path)

def main():
    """
        Main function
    """
    pathFile = os.path.join(os.path.dirname(__file__), "data.txt")
    # print("Reading data from file: ", pathFile)
    
    obj = Data(pathFile)
    data = obj.get_data()
    # print(data)
    
    start = 0
    goal = 1
    result = hill_climb_search(data, start, goal)
    print(result)
    
    
if __name__ == "__main__":
    main()