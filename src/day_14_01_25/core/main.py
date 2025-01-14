
class Bfs:
    """
        INPUT: 
            Số đỉnh 
            Số cạnh
            Vector Hướng
            Điểm Bắt Đầu
            Điểm Kết Thúc
    """
    def __init__(self, n, m, edges):
        """
            Khởi Tạo
                n: số đỉnh
                m: số cạnh
                edges: vector hướng của các cạnh
        """
        self.n = n
        self.m = m
        self.edges = edges
        
        self.visited = [False] * (n + 1)
        self.queue = []
        self.parent_node = []
        self.table = []
        
    def find_path(self, start, end):
        """
            Tìm đường đi từ start -> end
            Trả về đường đi thoả mãn từ start -> end
        """

        # clear cache
        self.clear_cache()
        
        self.queue.append(start)
        self.visited[start] = True
        
        # save in table to show progress
        self.table.append([start, self.edges[start], self.queue.copy(), self.visited.copy()])
        
        while len(self.queue) > 0:
            u = self.queue.pop(0)
            
            # Save the state after popping the node
            self.table.append([u, self.edges[u], self.queue.copy(), self.visited.copy()])
            
            if u == end:
                return self.helpper_find_path(start, end)
            
            for v in self.edges[u]:
                if not self.visited[v]:
                    self.visited[v] = True
                    self.queue.append(v)
                    self.parent_node.append((u, v))
        
        return []
    
    def helpper_find_path(self, start, end):
        """
            Hàm Trả về đường đi từ start -> end
        """
        path = []
        while end != start:
            for i in range(len(self.parent_node)):
                if self.parent_node[i][1] == end:
                    path.append(self.parent_node[i])
                    end = self.parent_node[i][0]
                    break
        return path[::-1]
    
    def clear_cache(self):
        """
            clear cache
        """
        self.visited = [False] * (self.n + 1)
        self.queue = []
        self.parent_node = []

    def table(self):
        """
            Trả về bảng trạng thái mỗi bước duyệt
        """
        return self.table