import contextlib
import datetime
import time

class cm_timer_1:
    def __enter__(self):
        self.start = datetime.datetime.now()
        return self

    def __exit__(self, *args):
        self.finish = datetime.datetime.now()
        print("time: ", self.finish - self.start)

@contextlib.contextmanager
def cm_timer_2():
    start = datetime.datetime.now()
    yield
    finish = datetime.datetime.now()
    print("time: ", finish - start)

if __name__ == "__main__":
    with cm_timer_1():
        time.sleep(5.5)

    with cm_timer_2():
        time.sleep(5.5)