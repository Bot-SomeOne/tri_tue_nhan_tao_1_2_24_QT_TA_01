
class Bfs:
    """
        INPUT: 
            Số đỉnh 
            Số cạnh
            Vector Hướng
            Điểm Bắt Đầu
            Điểm Kết Thúc
    """
    def __init__(self, n, m, edges, start, end):
        self.n = n
        self.m = m
        self.edges = edges
        self.start = start
        self.end = end
        self.graph = [[] for _ in range(n)]
        
        for edge in edges:
            self.graph[edge[0]].append(edge[1])