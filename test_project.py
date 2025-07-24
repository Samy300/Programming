import os 
import pytest
from project import FileReader, RedFileReader

def test_line_reader_nonexisten():
    reader = FileReader("nonexistent.text")
    lines = list(reader.line_reader())
    assert lines == ["unavailable"]

def test_line_generator_color_white(tmp_path):
    file_path = tmp_path / "text.txt"
    file_path.write_text("line")

    reader = FileReader(str(file_path))
    lines = list(reader.line_generator())

    assert "\031[0:37m]" in lines[0] and "\033[0m]" in lines[0]
