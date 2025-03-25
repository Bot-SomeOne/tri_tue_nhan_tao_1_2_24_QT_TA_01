import heapq
import os
from tabulate import tabulate

class Input:
    """
        Đọc file txt input đầu vào:
        - Dòng đầu (0) n đỉnh m cạnh.
        - n dòng tiếp theo lưu trọng số từng đỉnh tương ứng.
        - m dòng tiếp theo lưu cạnh tương ứng từ có hướng.
        - Dòng cuối cùng lưu đỉnh bắt đầu và đỉnh kết thúc.
    """
    def __init__(self, path_file):
        self.path_file = path_file
        self.n = 0
        self.m = 0
        self.weights = {}
        self.edges = []
        self.start = None
        self.goal = None
    
    def read_input(self):
        """
            Đọc file input và lưu vào các biến tương ứng
        """
        file = open(self.path_file, "r")
        # Đọc số lượng đỉnh và cạnh
        self.n, self.m = file.readline().strip().split()
        self.n = int(self.n)
        self.m = int(self.m)
        # Đọc trọng số các đỉnh
        for i in range(self.n):
            # Đỉnh u có trọng số w
            u, w = file.readline().strip().split()
            u = int(u)
            w = int(w)
            self.weights[u] = w
        # Đọc các cạnh
        for i in range(self.m):
            # Cạnh u -> v
            u, v = file.readline().strip().split()
            u = int(u)
            v = int(v)
            self.edges.append((u, v))
        # Đọc đỉnh bắt đầu và đỉnh kết thúc
        self.start, self.goal = file.readline().strip().split()
        self.start = int(self.start)
        self.goal = int(self.goal)
        file.close()
        
    def get_so_dinh(self):
        """
            Trả về số lượng đỉnh
        """
        return self.n
    
    def get_so_canh(self):
        """
            Trả về số lượng cạnh
        """
        return self.m
    
    def get_trong_so(self, u):
        """
            Trả về trọng số của các đỉnh u
        """
        return self.weights[u]
    
    def get_dinh_ke(self, u):
        """
            Trả về danh sách các đỉnh kề của đỉnh u
        """
        res = []
        for edge in self.edges:
            if edge[0] == u:
                res.append(edge[1])
        return res
    
    def get_dinh_bat_dau(self):
        """
            Trả về đỉnh bắt đầu
        """
        return self.start
    
    def get_dinh_ket_thuc(self):
        """
            Trả về đỉnh kết thúc
        """
        return self.goal
    
def show_data_input(input: Input):
    """
        Hiển thị thông tin đã đọc được từ file
    """
    # Hiển thị thông tin đã đọc được từ file
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

class BestFirstSearch:
    """
        Thuật toán Best First Search
    """
    def __init__(self, input: Input):
        self.input = input
        self.start = input.get_dinh_bat_dau()
        self.goal = input.get_dinh_ket_thuc()
        self.table = {}
        self.header_table = ["Đỉnh", "Cạnh Kề", "Danh Sách"]
        self.parent_node = {}
        
        
    def table_describes_step(self):
        """
            Tạo bảng mô tả từng bước của thuật toán
        """
        table = []
        ################################################
        # Biến khởi tạo
        node = (self.input.get_trong_so(self.start), self.start) # Trong so - Dinh
        adj = [] # Danh sach ( trong so - dinh ) ke voi dinh 
        # Khởi tạo danh sách kề
        for val in self.input.get_dinh_ke(self.start):
            adj.append((self.input.get_trong_so(val), val))
        # print(adj)
        # Tạo list
        list = [] 
        # Thêm vào list
        for i in adj:
            list.append(i)
        heapq.heapify(list)
        ################################################
        # Tạo dữ liệu bảng - { Đỉnh - Trọng số }
        table.append([node, adj, sorted(list)])
        # print(table)
        ################################################
        while node[1] != self.goal:
            if not list:  # Check if the heap is empty
                raise ValueError("Không có đường dẫn thoả mãn!")
            min_node = heapq.heappop(list)  # Lấy đỉnh có trọng số nhỏ nhất
            self.parent_node[min_node[1]] = node[1]
            node = min_node
            adj = []
            for val in self.input.get_dinh_ke(node[1]):  # Use node[1] to get the current node
                adj.append((self.input.get_trong_so(val), val))
            # Tạo list
            for i in adj:
                list.append(i)
            heapq.heapify(list)
            # Thêm dữ liệu bảng
            table.append([node, adj, sorted(list)])
            
        self.table = table
    
    def show_table_step(self):
        """
            Hiển thị bảng mô tả từng bước của thuật toán
        """
        print("Đỉnh bắt đầu:", self.start)
        print("Đỉnh kết thúc:", self.goal)
        print(tabulate(self.table, headers=self.header_table, tablefmt="grid"))
        print()
        self.print_path_step()
        print()
        
    def get_path_step(self):
        """
            Trả về đường đi từ đỉnh bắt đầu đến đỉnh kết thúc
        """
        path = []
        node = self.goal
        while node != self.start:
            path.append(node)
            node = self.parent_node[node]
        path.append(self.start)
        path.reverse()
        return path
    
    def print_path_step(self):
        """
            In đường đi từ đỉnh bắt đầu đến đỉnh kết thúc
        """
        path = self.get_path_step()
        print("Đường đi từ đỉnh bắt đầu đến đỉnh kết thúc:")
        for i in range(len(path)):
            if i == len(path) - 1:
                print(path[i], end="")
            else:
                print(path[i], end=" -> ")
        print()
    
class Output:
    """
        Lưu kết quả đầu ra vào file
    """
    def __init__(self, path_file, table, path_step_node, start, end):
        self.path_file = path_file
        self.table = table
        self.parent = path_step_node
        self.start = start
        self.end = end
    
    def write_output(self):
        """
            Ghi kết quả đầu ra vào file
        """
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
    

def main():
    """
        Main function
    """
    pathFile = os.path.join(os.path.dirname(__file__), "data_v2.txt")
    input = Input(pathFile)
    input.read_input()
    # Hiển thị thông tin đã đọc được từ file
    # show_data_input(input)
    # Thuật toán Best First Search
    bfs = BestFirstSearch(input)
    bfs.table_describes_step()

    bfs.show_table_step()
    
    pathFileOut = os.path.join(os.path.dirname(__file__), "output.txt")
    output = Output(pathFileOut, bfs.table, bfs.get_path_step(), bfs.start, bfs.goal)
    output.write_output()
    print("Kết quả đã được ghi vào file output.txt")
    
if __name__ == "__main__":
    main()
    
        
                