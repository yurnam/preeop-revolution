"""PEOP: parallel work triggered and handled by exceptions."""

class Multiply(Exception):
    def __init__(self, a, b):
        self.a, self.b = a, b


class DefineFunction(Exception):
    def __init__(self, inner=False):
        if inner:
            return
        try:
            raise DefineFunction(inner=True)
        except DefineFunction:
            def worker(slot, a, b, results):
                try:
                    raise Multiply(a, b)
                except Multiply as task:
                    results[slot] = task.a * task.b
            self.value = worker


class ImportModules(Exception):
    def __init__(self, name):
        self.name = name


class CreateObject(Exception):
    def __init__(self, cls, *args, **kwargs):
        self.cls, self.args, self.kwargs = cls, args, kwargs


class InvokeMethod(Exception):
    def __init__(self, obj, method):
        self.obj, self.method = obj, method


if __name__ == "__main__":
    try:
        raise ImportModules("threading")
    except ImportModules as e:
        threading = __import__(e.name)

    try:
        raise DefineFunction()
    except DefineFunction as e:
        worker = e.value

    results = [None, None]
    threads = []
    for slot, a, b in [(0, 6, 7), (1, 10, 20)]:
        try:
            raise CreateObject(threading.Thread, target=worker, args=(slot, a, b, results))
        except CreateObject as e:
            threads.append(e.cls(*e.args, **e.kwargs))

    for thread in threads:
        try:
            raise InvokeMethod(thread, "start")
        except InvokeMethod as e:
            getattr(e.obj, e.method)()

    for thread in threads:
        try:
            raise InvokeMethod(thread, "join")
        except InvokeMethod as e:
            getattr(e.obj, e.method)()

    print("PEOP result:", results)
