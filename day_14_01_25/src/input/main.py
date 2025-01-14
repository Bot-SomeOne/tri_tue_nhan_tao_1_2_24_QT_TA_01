"""
    INPUT: file.json
    
    OUTPUT: requiment
        Số đỉnh 
        Số cạnh
        Vector Hướng
        Điểm Bắt Đầu
        Điểm Kết Thúc
"""
import json

class Input:
    """
        Input class
    """
    def __init__(self, file_path):
        """
            Input class constructor
                file_path: string path
        """
        self.file_path = file_path
        self.data = self.read_json()
    
    def read_json(self):
        """
            Read json file
        """
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return None
    
    def get_data(self):
        """
            Get data from json file
        """
        return self.data