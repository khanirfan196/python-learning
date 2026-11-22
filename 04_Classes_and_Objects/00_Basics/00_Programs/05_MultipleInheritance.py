
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
        print("Watch fetches current timestamp from bios")
        return datetime.datetime.now()

    def __str__(self):
        return f"""
            Watch configurations - 
                color: {self.color}
                Watch dial: {self.dial_size}
                Watch strap: {self.strap_len}
            """

class Android():
    _android_version = "1.0.0"
    _user_interface = "one_ui"

    def __init__(self):
        pass

    def connect_bluetooth(self):
        pass 

    def show_battery_level(self):
        pass

    def update_os(self):
        pass

    def current_time(self):
        print("Android fetches current timestamp from server.")
        return datetime.datetime.now()


class SmartWatch(Android, Watch):

    def __init__(self, dial_size, strap_len, color):
        # 1. Initialize the Android side explicitly (takes no args)
        Android.__init__(self)
        
        # 2. Initialize the Watch side explicitly (takes the 3 args)
        Watch.__init__(self, dial_size, strap_len, color)


if __name__ == "__main__":

    # wrist_watch = Watch(32, 7.5, "blue")

    # print(wrist_watch)
    # print(wrist_watch.current_time())

    smart_watch = SmartWatch(32, 7.5, "blue")
    # smart_watch = SmartWatch()
    print(smart_watch)
    # below output will print current_time() method based on the order of 
    # parent classes specified in the child class.
    # If Watch class is first meaning SmartWatch(Watch, Android), then current_time()
    # of Watch class is called if order is reversed, i.e. SmartWatch(Android, Watch), then
    # current_time() of Android parent class is called.
    print(smart_watch.current_time())

    # special method to list the order of parent classes specified in a child class.
    # print(SmartWatch.__mro__)