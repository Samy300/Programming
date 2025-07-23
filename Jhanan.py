import os

class MainReader:
    def __init__(self, file_name):

    def line_reader(self):
        if not os.path.exists(self.file_name):
            yield "Unaviable"
            return
        with open(self.file_name) as file:
            for line in file:
                yield line.strip()
        
    def play(self):
        for line in self.line_generator():
            print(line)
    
    @text_color("white"):
    def line_generator(self):
        return self.line_reader()
    
    def _concat(self, other,color_class):
        output_file = "concatenated.txt"
        with open(output_file, "w") as out:
            for fname in (self.file_name, other.file_name):
                if os.path.exists(fname):
                    with open(fname) as f:
                        out.writelines(f)
        return color_class(output_file)
    
    def __add__(self, other):
        return self.concat(other, color_class = self.__class__)

    def __add__(self,other):
        return self._concat(other, color_class=self.__class__)



    

