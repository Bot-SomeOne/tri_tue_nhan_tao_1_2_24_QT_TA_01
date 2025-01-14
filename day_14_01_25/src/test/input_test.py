"""
    Test input data from file .json
"""
from src.input import Input
import os

def main():
    
    file_name = "data_1.json"
    path_file = os.path.join(os.getcwd(), "src", "data", file_name)

    print(path_file)
    
    ip  = Input(path_file)
    print(ip.get_data())
    
if __name__ == "__main__":
    main()