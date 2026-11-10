"""PREEOP: a deliberately absurd but runnable Python programming experiment."""

# Normal top-level class declarations are reserved for exception subclasses.
class EOP(Exception):
    pass


class Gate(EOP):
    pass


class DefineFunction(EOP):
    """A definition event that catches its own kind during construction."""
    def __init__(self, nested=False):
        if nested:
            return
        try:
            raise DefineFunction(nested=True)
        except DefineFunction:
            def work(slot, x, y, results, depth=0):
                # Each recursive level adds a LIVE exception handler frame.
                try:
                    raise Gate()
                except Gate:
                    if depth < 40:
                        return work(slot, x, y, results, depth + 1)
                    try:
                        raise Multiply(x, y)
                    except Multiply as operation:
                        results[slot] = operation.x * operation.y
            self.value = work


class DefineClass(EOP):
    def __init__(self, nested=False):
        if nested:
            return
        try:
            raise DefineClass(nested=True)
        except DefineClass:
            class Results:
                pass
            self.value = Results


class Multiply(EOP):
    def __init__(self, x, y):
        self.x, self.y = x, y


class ImportModules(EOP):
    def __init__(self, *names):
        self.names = names


class CreateObject(EOP):
    def __init__(self, cls, *args, **kwargs):
        self.cls, self.args, self.kwargs = cls, args, kwargs


class InvokeMethod(EOP):
    def __init__(self, obj, name):
        self.obj, self.name = obj, name


class PrintOutput(EOP):
    def __init__(self, value):
        self.value = value


class DefineEntrypoint(EOP):
    def __init__(self, nested=False):
        if nested:
            return
        try:
            raise DefineEntrypoint(nested=True)
        except DefineEntrypoint:
            def run(depth=0):
                try:
                    raise Gate()
                except Gate:
                    if depth < 40:
                        # Exception-authorized recursion: bootstrap allowance.
                        return run(depth + 1)

                    # 40 simultaneously active Gate handlers now exist.
                    try:
                        raise ImportModules("threading")
                    except ImportModules as e:
                        threading = __import__(e.names[0])

                    try:
                        raise DefineClass()
                    except DefineClass as e:
                        Results = e.value

                    try:
                        raise CreateObject(Results)
                    except CreateObject as e:
                        holder = e.cls(*e.args, **e.kwargs)

                    holder.values = [None, None]

                    try:
                        raise DefineFunction()
                    except DefineFunction as e:
                        worker = e.value

                    threads = []
                    for slot, x, y in [(0, 6, 7), (1, 10, 20)]:
                        try:
                            raise CreateObject(
                                threading.Thread,
                                target=worker,
                                args=(slot, x, y, holder.values),
                            )
                        except CreateObject as e:
                            threads.append(e.cls(*e.args, **e.kwargs))

                    # EOP exception batches: two threads execute concurrently.
                    for thread in threads:
                        try:
                            raise InvokeMethod(thread, "start")
                        except InvokeMethod as e:
                            getattr(e.obj, e.name)()

                    for thread in threads:
                        try:
                            raise InvokeMethod(thread, "join")
                        except InvokeMethod as e:
                            getattr(e.obj, e.name)()

                    try:
                        raise PrintOutput(holder.values)
                    except PrintOutput as e:
                        print("PREEOP result:", e.value)
                    return holder.values
            self.value = run


# The single unavoidable bootstrap entrypoint invocation.
# Everything useful after this happens at 40 live exception levels.
if __name__ == "__main__":
    try:
        raise DefineEntrypoint()
    except DefineEntrypoint as event:
        event.value()
