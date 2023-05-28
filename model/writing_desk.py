"""import Desk"""
from model.desk import Desk


class WritingDesk(Desk):
    """class"""
    __instance = None

    """class constructor """

    def __init__(self, number_of_drawers, has_keyboard_tray, max_weight_capacity,
                 current_height, max_height, height, width, length):
        if getattr(self, 'has_keyboard_tray', None) is not None:
            return
        self.__number_of_drawers = number_of_drawers
        self.has_keyboard_tray = has_keyboard_tray
        self.max_weight_capacity = max_weight_capacity
        self.current_height = current_height
        self.max_height = max_height
        super().__init__(height, width, length)
        self.material_list = {"iron", "wood"}

    def __new__(cls, *args, **kwargs):
        """responsible for checking and creating new instances"""
        if cls.__instance is None:
            cls.__instance = super(WritingDesk, cls).__new__(cls)
        return cls.__instance

    def adjust_height(self, centimeters: int):
        """method that increases the height of the table
        (if it does not exceed the maximum allowed)"""
        if self.current_height < self.max_height:
            self.current_height += centimeters

    def move_down(self, centimeters: int):
        """a method that reduces the height of the desk"""
        self.current_height -= centimeters

    def set_data(self, number_of_drawers, has_keyboard_tray,
                 max_weight_capacity, current_height, max_height):
        """method helps to initialize the table object with the specified characteristics"""
        self.__number_of_drawers = number_of_drawers
        self.has_keyboard_tray = has_keyboard_tray
        self.max_weight_capacity = max_weight_capacity
        self.current_height = current_height
        self.max_height = max_height

    def __str__(self):
        """цей метод виводить обʼєкти по певному шаблону"""
        return f'WritingDesk(number_of_drawers={self.__number_of_drawers}, has_keyboard_tray=' \
               f' {self.has_keyboard_tray}, max_weight_capacity={self.max_weight_capacity}, ' \
               f'current_height=' \
               f'{self.current_height}, max_height={self.max_height})'

