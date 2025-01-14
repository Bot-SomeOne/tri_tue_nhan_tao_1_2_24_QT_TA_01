from src.input import Input
from src.core import Bfs
from src.output import Output
import os

def main():
    
    file_name = "data_1.json"
    path_file = os.path.join(os.getcwd(), "src", "data", file_name)

    data_input = Input(path_file).get_data()
        
    bfs = Bfs(data_input.get('n'), data_input.get('m'), data_input.get('edges'))
    
    output = Output(bfs.find_path(data_input['start'], data_input['end']), bfs.table)
    
    output.console_output()
    
if __name__ == "__main__":
    main()