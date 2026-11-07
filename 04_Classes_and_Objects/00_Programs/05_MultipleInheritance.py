
# Multiple Inheritance is bit tricky. 
# Python uses MRO scan while calling super() functions for initialization
# when there are same methods in parent classes. 

import datetime


class Watch():

    _dial_size = [32, 34, 36]
    _strap_len = [6.5, 7.5, 8.5]
    _colors = ["black", "brown", "blue"]

    def __init__(self, dial_size, strap_len, color):
        if dial_size not in self._dial_size:
            raise ValueError("Wrong dial size. Should be either 32, 34, or 36")
        self.dial_size = dial_size
        if strap_len not in self._strap_len:
            raise ValueError("Wrong strap size. Should be either 6.5, 7.5, or 8.5")
        self.strap_len = strap_len
        if color not in self._colors:
            raise ValueError("Wrong color. Should be either blue, black, or brown")
        self.color = color

    def current_time(self):
        return datetime.datetime.now()

    def __str__(self):
        return f"""
Watch configurations - 
    color: {self.color}
    Watch dial: {self.dial_size}
    Watch strap: {self.strap_len}"""

class Android():
    pass


if __name__ == "__main__":

    wrist_watch = Watch(32, 7.5, "blue")

    print(wrist_watch)
    print(wrist_watch.current_time())