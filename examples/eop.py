"""EOP: imports, object creation, arithmetic and printing via exceptions."""

class ImportModules(Exception):
    def __init__(self, *names):
        self.names = names


class DefineClass(Exception):
    def __init__(self, inner=False):
        if inner:
            return
        try:
            raise DefineClass(inner=True)
        except DefineClass:
            class Calculator:
                pass
            self.value = Calculator


class CreateObject(Exception):
    def __init__(self, cls):
        self.cls = cls


class Multiply(Exception):
    def __init__(self, a, b):
        self.a, self.b = a, b


class PrintOutput(Exception):
    def __init__(self, text):
        self.text = text


if __name__ == "__main__":
    try:
        raise ImportModules("math")
    except ImportModules as e:
        modules = {name: __import__(name) for name in e.names}

    try:
        raise DefineClass()
    except DefineClass as e:
        Calculator = e.value

    try:
        raise CreateObject(Calculator)
    except CreateObject as e:
        calculator = e.cls()

    try:
        raise Multiply(6, 7)
    except Multiply as e:
        calculator.answer = modules["math"].prod((e.a, e.b))

    try:
        raise PrintOutput(calculator.answer)
    except PrintOutput as e:
        print("EOP result:", e.text)
