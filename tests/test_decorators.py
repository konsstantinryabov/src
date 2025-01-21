from src import decorators
import pytest

def test_log_decorator_error_write_loc():
    @decorators.log(filename="logs.txt")
    def my_function(x, y):
        return x + y


    with pytest.raises(Exception):
        my_function(20, "hello")

    file = open("logs.txt", "r")
    line = file.readlines()
    file.close()

    assert line[-1] == f"my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (20, 'hello'), {"{}"}\n"


def test_log_decorator_successfully_write_loc():
    @decorators.log(filename="logs.txt")
    def my_function(x, y):
        return x + y

    my_function(20, 40)

    file = open("logs.txt", "r")
    line = file.readlines()
    file.close()

    assert line[-1] == f"my_function ok\n"


def test_log_decorator_error_write_console(capsys):
    @decorators.log(filename="")
    def my_function(x, y):
        return x + y

    with pytest.raises(Exception):
        my_function(20, "hello")

    captured = capsys.readouterr()

    assert captured.out == (f"my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (20, 'hello'), {"{}"}\n\n")


def test_log_decorator_successfully_write_console(capsys):
    @decorators.log(filename="")
    def my_function(x, y):
        return x + y

    my_function(20, 40)

    captured = capsys.readouterr()

    assert captured.out == "my_function ok\n\n"
