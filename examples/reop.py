"""REOP: a self-recursive function must descend before multiplication."""

class DefineFunction(Exception):
    def __init__(self, inner=False):
        if inner:
            return
        try:
            raise DefineFunction(inner=True)
        except DefineFunction:
            def multiply(a, b, depth=0):
                if depth < 40:
                    return multiply(a, b, depth + 1)
                return a * b
            self.value = multiply


if __name__ == "__main__":
    try:
        raise DefineFunction()
    except DefineFunction as e:
        multiply = e.value
    print("REOP result:", multiply(6, 7))
