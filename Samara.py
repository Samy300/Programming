import os

# Function to define the ANSi Colors
def text_color(color: str):
    colors = {
        "green" : "\033[0;32m",
        "blue": "\033[0;34m",
        "red" : "\033[0;31m",
        "white": "\033[0;37m"         
        }

    def clr(func):
        def wrapper(*args, **kwargs):
            for line in func (*args, **kwargs):
                yield f"{colors[color]}{line}\033[0m"
            return wrapper
    return color
