class Singleton:
    _instances = {}

    def __init__(self, class_):
        self._class = class_
        # self._instances = {}

    def __call__(self, *args, **kwargs):
        if self._class not in self._instances:
            self._instances[self._class] = self._class(*args, **kwargs)
        return self._instances[self._class]


@Singleton
class FirstClass:
    def __init__(self, m):
        self.val = m


a = FirstClass(100)
b = FirstClass(25)

print(a is b)  # True
print(a.val)
print(b.val)
