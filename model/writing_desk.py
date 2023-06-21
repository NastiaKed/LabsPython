from model.desk import Desk


class WritingDesk(Desk):
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

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(WritingDesk, cls).__new__(cls)
        return cls.__instance

    def adjust_height(self, centimeters: int):
        if self.current_height < self.max_height:
            self.current_height += centimeters

    def move_down(self, centimeters: int):
        self.current_height -= centimeters

    def set_data(self, number_of_drawers, has_keyboard_tray, max_weight_capacity, current_height, max_height):
        """method helps to initialize the table object with the specified characteristics"""
        self.__number_of_drawers = number_of_drawers
        self.has_keyboard_tray = has_keyboard_tray
        self.max_weight_capacity = max_weight_capacity
        self.current_height = current_height
        self.max_height = max_height

    def __str__(self):
        """цей метод виводить обʼєкти по певному шаблону"""
        return f'WritingDesk(number_of_drawers={self.__number_of_drawers}, has_keyboard_tray=' \
               f' {self.has_keyboard_tray}, max_weight_capacity={self.max_weight_capacity}, current_height=' \
               f'{self.current_height}, max_height={self.max_height})'

    # @staticmethod
    # def get_instance():
    #     if WritingDesk.__instance is None:
    #         WritingDesk.__instance = WritingDesk()
    #     return WritingDesk.__instance
