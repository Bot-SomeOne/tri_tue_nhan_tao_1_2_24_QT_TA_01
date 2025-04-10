import heapq
import os
from tabulate import tabulate

class Input:
    def __init__(self, path_file):
        self.path_file = path_file
        self.n = 0
        self.m = 0
        self.weights = {}
        self.edges = []
        self.start = None
        self.goal = None
    
    def read_input(self):
        file = open(self.path_file, "r")
        
        self.n, self.m = file.readline().strip().split()
        self.n = int(self.n)
        self.m = int(self.m)
        
        for i in range(self.n):
            u, w = file.readline().strip().split()
            u = str(u)
            w = int(w)
            self.weights[u] = w
            
        for i in range(self.m):
            u, v = file.readline().strip().split()
            u = str(u)
            v = str(v)
            self.edges.append((u, v))
            
        self.start, self.goal = file.readline().strip().split()
        self.start = str(self.start)
        self.goal = str(self.goal)
        
        file.close()
        
    def get_dinh_ke(self, u):
        res = []
        for edge in self.edges:
            if edge[0] == u:
                res.append(edge[1])
        return res
        
    def get_so_dinh(self):
        return self.n
    
    def get_so_canh(self):
        return self.m
    
    def get_trong_so(self, u):
        return self.weights[u]
    
    def get_dinh_bat_dau(self):
        return self.start
    
    def get_dinh_ket_thuc(self):
        return self.goal
    
class BestFirstSearch:
    def __init__(self, input: Input):
        self.input = input
        self.start = input.get_dinh_bat_dau()
        self.goal = input.get_dinh_ket_thuc()
        self.table = {}
        self.header_table = ["Đỉnh", "Cạnh Kề", "Danh Sách"]
        self.parent_node = {}
        
    def table_describes_step(self):
        table = []
        node = (self.input.get_trong_so(self.start), self.start)
        
        adj = []
        for val in self.input.get_dinh_ke(self.start):
            adj.append((self.input.get_trong_so(val), val))
            self.parent_node[val] = self.start
        
        list = [] 
        for i in adj:
            list.append(i)
        heapq.heapify(list)
        table.append([[node[1], node[0]], self.beaty_out(adj), self.beaty_out(sorted(list))])
        
        while node[1] != self.goal:
            if not list: 
                raise ValueError("Không có đường dẫn thoả mãn!")
            node = heapq.heappop(list) 
            
            adj = []
            for val in self.input.get_dinh_ke(node[1]):
                adj.append((self.input.get_trong_so(val), val))
                if val not in self.parent_node:
                    self.parent_node[val] = node[1]
                    
            for i in adj:
                list.append(i)
            heapq.heapify(list)
            
            # table.append([node, adj, sorted(list)])
            table.append([[node[1], node[0]], self.beaty_out(adj), self.beaty_out(sorted(list))])
            
        self.table = table
        
    
    def beaty_out(self, arr):
        res = []
        for node in arr:
            if type(node) == tuple:
                res.append((node[1], node[0]))
            else:
                res.append(node)
        return res
    
    def show_table_step(self):
        print("Đỉnh bắt đầu:", self.start)
        print("Đỉnh kết thúc:", self.goal)
        print(tabulate(self.table, headers=self.header_table, tablefmt="grid"))
        print()
        self.print_path_step()
        print()
        
    def get_path_step(self):
        path = []
        node = self.goal
        
        while node != self.start:
            path.append(node)
            node = self.parent_node[node]
            
        path.append(self.start)
        path.reverse()
        return path
    
    def print_path_step(self):
        path = self.get_path_step()
        print("Đường đi từ đỉnh bắt đầu đến đỉnh kết thúc:")
        for i in range(len(path)):
            if i == len(path) - 1:
                print(path[i], end="")
            else:
                print(path[i], end=" -> ")
        print()
    
class Output:
    def __init__(self, path_file, table, path_step_node, start, end):
        self.path_file = path_file
        self.table = table
        self.parent = path_step_node
        self.start = start
        self.end = end
    
    def write_output(self):
        file = open(self.path_file, "w")
        file.write("Đỉnh bắt đầu: " + str(self.start) + "\n")
        file.write("Đỉnh kết thúc: " + str(self.end) + "\n")
        
        file.write("Bảng mô tả từng bước của thuật toán:\n")
        file.write(tabulate(self.table, headers=["Đỉnh", "Cạnh Kề", "Danh Sách"], tablefmt="grid") + "\n")
        
        file.write("Đường đi từ đỉnh bắt đầu đến đỉnh kết thúc:\n")
        for i in range(len(self.parent)):
            if i == len(self.parent) - 1:
                file.write(str(self.parent[i]) + "\n")
            else:
                file.write(str(self.parent[i]) + " -> ")
        file.write("\n")
        
        file.close()
    
def show_data_input(input: Input):
    print("Số lượng đỉnh:", input.get_so_dinh())
    print("Số lượng cạnh:", input.get_so_canh())
    print("Trọng số các đỉnh:")
    for u in input.weights:
        print(f"Đỉnh {u}: {input.get_trong_so(u)}")
        print(f"Các cạnh kệ của đỉnh {u}: {input.get_dinh_ke(u)}")
        print()
    print("Các cạnh:")
    for edge in input.edges:
        print(f"Cạnh {edge[0]} -> {edge[1]}")
        print()
    start = input.get_dinh_bat_dau()
    goal = input.get_dinh_ket_thuc()
    print("Đỉnh bắt đầu:", start)
    print("Đỉnh kết thúc:", goal)

def main():
    pathFile = os.path.join(os.path.dirname(__file__), "input.txt")
    input = Input(pathFile)
    input.read_input()
   
    bfs = BestFirstSearch(input)
    bfs.table_describes_step()

    bfs.show_table_step()
    
    pathFileOut = os.path.join(os.path.dirname(__file__), "output.txt")
    output = Output(pathFileOut, bfs.table, bfs.get_path_step(), bfs.start, bfs.goal)
    output.write_output()
    print("Kết quả đã được ghi vào file output.txt")
    
if __name__ == "__main__":
    main()
    