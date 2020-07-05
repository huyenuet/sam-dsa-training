import time


class Timer:

    def register(self, timeout: int):
        print(f"self.on_timeout will be called after {timeout} seconds")
        time.sleep(timeout)
        self.on_timeout()

    def on_timeout(self):
        pass


class Door:
    def __init__(self):
        self.is_open = False

    @staticmethod
    def lock():
        print("Lock the door")

    @staticmethod
    def unlock():
        print("Unlock the door")


class TimedDoor(Door):
    def __init__(self):
        super().__init__()
        self.timer = Timer()

    def on_timeout(self):
        self.lock()


timed_door = TimedDoor()
timed_door.timer.register(10)

# after 10 seconds
# timed_door.on_timeout() is called automatically
