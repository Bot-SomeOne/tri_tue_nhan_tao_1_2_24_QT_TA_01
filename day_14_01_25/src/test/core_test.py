
from src.core import Bfs
   
def main():
    """
    Main function
    """
    n = 9
    m = 13
    edges = [
        [1, 2, 3],
        [6, 7],
        [4],
        [2, 5],
        [6, 8],
        [8],
        [],
        [6],
        []
    ]
    start = 0
    end = 8
    
    r = Bfs(n, m, edges)
    
    c = r.find_path(start, end)
    if c == -1:
        print("No path found")
        return
    
    print(c)
    
    r.print_table()
    print(r.help_visited())
        
    
if __name__ == '__main__':
    main()