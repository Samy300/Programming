class GreenFileReader(MainReader):
    @text_color("green")
    def line_generator(self):
        return self.line_reader()

class BlueFileReader(MainReader):
    @text_color("blue"):
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

