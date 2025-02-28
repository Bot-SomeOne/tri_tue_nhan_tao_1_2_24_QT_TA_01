
import os


class Graph:
    """
        Graph class
    """
    def __init__(self, n, m):
        """
            Constructor
            Initialize graph with n nodes and m edges
            @param n: number of nodes
            @param m: number of edges
        """    
        self.n = n
        self.m = m
        self.graph = {}
        self.trongSoDinh = {}
        
    def add_edge(self, u, v, d, w):
        """
            Add edge
        """
        
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((d, v))
        self.trongSoDinh[v] = w
        
    def get_graph(self):
        """
            Get graph
        """
        
        return self.graph
    
    def get_list_trong_so(self):
        """
            Get list trong so dinh
        """
        
        return self.trongSoDinh
    
    def get_edges(self):
        """
            Get edges
        """
        
        edges = []
        
        for u in self.graph:
            for v in self.graph[u]:
                edges.append((u, v))
                
        return edges
    
    def get_nodes(self):
        """
            Get nodes
        """
        
        nodes = []
        
        for u in self.graph:
            nodes.append(u)
            
        return nodes
    
    def get_neighbors(self, u):
        """
            Get neighbors
        """
        
        return self.graph[u]
    
    def get_trong_so_dinh(self, u):
        """
            Get trong so dinh
        """
        
        return self.trongSoDinh[u]
    
    def __str__(self):
        """
            String representation
        """
        
        return str(self.graph)


class Data:
    """
       So dinh
       So Canh
       Cap gia tri canh     
       tra vang mang cap 4 phan tu - [(dinh 1, dinh 2, khoang canh, trong so dinh 2), ...]
    """
    def __init__(self, path_file):
        self.path_file = path_file
        self.dinh = 0
        self.canh = 0
        self.data = {}
        
        self.process_create_data()
    
    def get_data(self):
        return self.data
    
    def get_graph(self):
        return self.data.get_graph()
    
    def get_trong_so(self):
        return self.data.get_list_trong_so()
    
    def process_create_data(self):
        f = open(self.path_file, "r")
        self.dinh = int(f.readline())
        self.canh = int(f.readline())
        
        dataTemp = Graph(self.dinh, self.canh)
        for _ in range(self.canh):
            line = f.readline().strip('\n').split()
            if len(line) >= 4:
                u = int(line[0])
                v = int(line[1])
                d = int(line[2])
                w = int(line[3])
                dataTemp.add_edge(u, v, d, w)
        f.close()
        self.data = dataTemp


def main():
    """
        Main function
    """
    pathFile = os.path.join(os.path.dirname(__file__), "data.txt")
    # print(pathFile)
    data = Data(pathFile)
    print(data.get_graph())
    print(data.get_trong_so())
    
    
if __name__ == '__main__':
    main()