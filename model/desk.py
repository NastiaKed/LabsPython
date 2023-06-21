import abc


class Desk(abc.ABC):
    @abc.abstractmethod
    def __init__(self, height, width, length):
        self.height = height
        self.width = width
        self.length = length

    @abc.abstractmethod
    def adjust_height(self, centimeters: int):
        """adjust_height = increases the height of the table by the specified number of centimeters"""
        pass

    @abc.abstractmethod
    def move_down(self, centimeters: int):
        """move_down = decreases the height of the table by the specified number of centimeters"""
        pass

