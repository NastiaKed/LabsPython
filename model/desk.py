import abc


class Desk(abc.ABC):
    @abc.abstractmethod
    def __init__(self, height, width, length):
        self.height = height
        self.width = width
        self.length = length
        self.material_list = set()

    @abc.abstractmethod
    def adjust_height(self, centimeters: int):
        """adjust_height = increases the height of the table by the specified number of centimeters"""
        pass

    @abc.abstractmethod
    def move_down(self, centimeters: int):
        """move_down = decreases the height of the table by the specified number of centimeters"""
        pass

    def to_dict(self, type_=None):
        return {k: v for k, v in self.__dict__ if not callable(v) and (type_ is None or isinstance(v, type_))}

    def __iter__(self):
        return iter(self.material_list)

