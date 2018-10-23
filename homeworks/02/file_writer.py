import os
import pickle as pkl
class FileWriter:
    def __init__(self, path):
        if self._check_path(os.path.dirname(path))==True:
            self.path_ = path
            self.file = None
        else:
            print("this path does not exist!")
            
    def _check_path(self, path):
        return(os.path.exists(path))
    
    def __enter__(self):
        self.file = open(self.path_, "a+")
        return self
    
    def __exit__(self, type, value, traceback):
        if self.file is not None:
            self.file.close()
            self.file = None
   
    def print_file(self):
        if self._check_path(self.path_):
            with open(self.path_, "a+") as file:
                smtg=file.read()
                print(smtg)
                file.close()
        else:
            print("this path does not exist!")

    
    def write(self, some_string):
        if self._check_path(self.path_):
            with open(self.path_, "a+") as file:
                file.write(some_string)
                file.close()
        else:
            print("this path does not exist!")
    
    def save_yourself(self, file_name):
        with open(file_name, "wb+") as file:#откроем для записи в двоичном формате
            pkl.dump(self, file)
            
    @property
    def path(self):
        return (self.path_)
    
    @path.deleter
    def path(self):
        self.path_=None
        
    @path.setter
    if self._check_path(os.path.dirname(path))==True:
        self.path_ = path
    else:
        print("this path does not exist!")
        
    @classmethod
    def load_file_writer(cls, pickle_file):
        with open(pickle_file, "rb+") as file:#для чтения в двоичном
            wrtr=pkl.load(file)
        return(wrtr)
  
    