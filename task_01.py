#### TASK 01 ####
# Создайте реализацию паттерна Builder. Протестируйте работу созданного класса.

class Builder(object):
    def build_body(self):
        raise NotImplementedError()

    def build_battery(self):
        raise NotImplementedError()

    def build_button(self):
        raise NotImplementedError()

    def build_locking(self):
        raise NotImplementedError()


class Locking(object):

    def __init__(self, body, battery, button):
        self._lock = False
        self._body = body
        self._battery = battery
        self._button = button

    def on(self):
        self._lock = True

    def off(self):
        self._lock = False

    def __str__(self):
        lock = "on" if self._lock else "off"
        return f"Locking [{lock}]"


class Body(object):
    """Body"""


class Battery(object):
    """Battery"""


class Button(object):
    """Button"""


class LockingBuilder(Builder):

    def build_body(self):
        return Body()

    def build_battery(self):
        return Battery()

    def build_button(self):
        return Button()

    def create_locking(self):
        body = self.build_body()
        battery = self.build_battery()
        button = self.build_button()
        return Locking(body, battery, button)


builder = LockingBuilder()
locker = builder.create_locking()
locker.on()
print(locker)



