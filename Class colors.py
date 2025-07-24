#Jhanan + Samara colors class
import os 

def text_color(color: str):
    colors = {
        "green": "\033[0;32m",
        "blue": "\033[0;34m",
        "red": "\033[0;31m",
        "white": "\033[0;37m"         
    }

    def clr(func):
        def wrapper(*args, **kwargs):
            for line in func(*args, **kwargs):
                yield f"{colors[color]}{line}\033[0m"
        return wrapper
    return clr

class MainReader:
    def _init_(self, file_name):
        self.file_name = file_name

    def line_reader(self):
        if not os.path.exists(self.file_name):
            yield "Unavailable"
            return
        with open(self.file_name) as file:
            for line in file:
                yield line

    def play(self):
        for line in self.line_generator():
            print(line)

    def _concat(self, file_2):
        output_file = "concatenated.txt"
        with open(output_file, "w") as out:
            for fname in (self.file_name, file_2.file_name):
                if os.path.exists(fname):
                    with open(fname) as f:
                        out.writelines(f)
        return self.__class__(output_file)

    def _add_(self, other):
        return self.concat(other)


class GreenFileReader(MainReader):
    @text_color("green")
    def line_generator(self):
        return self.line_reader()

class BlueFileReader(MainReader):
    @text_color("blue")
    def line_generator(self):
        return self.line_reader()

class RedFileReader(MainReader):
    @text_color("red")
    def line_generator(self):
        return self.line_reader()

class WhiteFileReader(MainReader):
    @text_color("white")
    def line_generator(self):
        return self.line_reader()


def main():
    readers = [
        GreenFileReader("text_1.txt"),
        BlueFileReader("text_2.txt"),
        RedFileReader("text_3.txt"),
    ]

    for reader in readers:
        reader.play()

    (readers[0] + readers[1]).play()

if _name_ == "_main_":
    main()
