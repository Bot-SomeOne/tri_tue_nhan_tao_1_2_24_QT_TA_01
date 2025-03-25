
import heapq
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
            
        self.data[u].append((v, w)) # u -> v 
    
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

# function Best First Search 
def best_first_search(graph, start, goal):
    """
        Best First Search
    """
    pq = [] # (priority, value)
    heapq.heappush(pq, (0, start))
    visited = set() # set have func find value
    parent = {start: None}
    
    table = [] # print step to step
    
    while pq:
        w, u = heapq.heappop(pq)
        
        if u in visited:
            continue
        visited.add(u)
        
        if u == goal:
            table.append([u, graph[u], []])
            print_table(table)
            print_path(parent, start, goal)
            return True
        
        for v, weight in graph[u]:
            if v not in visited:
                parent[v] = u
                heapq.heappush(pq, (weight, v))
        
        table.append([u, graph[u], sorted(pq.copy(), key=lambda x: (x[0], x[1]))]) 

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
        qu = []
        for item in list(data[i][2].copy()):
            qu.append([item[1], item[0]])
            
        data_print.append([data[i][0], data[i][1], qu])
        
    print(tabulate(data_print, headers=["Dinh", "Canh", "Queue"], tablefmt="pretty"))

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
    result = best_first_search(data, start, goal)
    print(result)
    
    
if __name__ == "__main__":
    main()