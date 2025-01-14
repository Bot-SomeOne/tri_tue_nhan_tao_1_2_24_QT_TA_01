from tabulate import tabulate

def convert_array_to_string(array):
    points = [array[0][0]]  # Start with the first point
    for tup in array:
        points.append(tup[1])
    return " -> ".join(map(str, points))

class Output:
    """
        Out put class to display the output
    """
    def __init__(self, path, table):
        self.path = path
        self.table = table
        
    def console_output(self):
        """
            Display the output in the console
        """
        header = ["Point", "Near", "Queue", "Visited"]
        data = []
        for line in self.table:
            temp = []
            for d in line:
                temp.append(d)
            data.append(temp)
            
        print(tabulate(data, headers=header, tablefmt="grid"))
        
        print("Path: ", convert_array_to_string(self.path))
        
        

    