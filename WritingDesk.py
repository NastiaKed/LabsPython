class WritingDesk:

    def __init__(self, number_of_drawers, has_keyboard_tray, max_weight_capacity, current_height, max_height):
        self.__number_of_drawers = number_of_drawers
        self.__has_keyboard_tray = has_keyboard_tray
        self.__max_weight_capacity = max_weight_capacity
        self.__current_height = current_height
        self.__max_height = max_height

    def adjust_height(self, centimeters: int):
        if self.__current_height < self.__max_height:
            self.__current_height += centimeters

    def move_down(self, centimeters: int):
        if self.__current_height - centimeters > 0:
            self.__current_height -= centimeters

    def set_data(self, number_of_drawers, has_keyboard_tray, max_weight_capacity, current_height, max_height):
        self.__number_of_drawers = number_of_drawers
        self.__has_keyboard_tray = has_keyboard_tray
        self.__max_weight_capacity = max_weight_capacity
        self.__current_height = current_height
        self.__max_height = max_height

    def __str__(self):
        return f'number of drawers: {self.__number_of_drawers}, has keyboard tray:' \
               f' {self.__has_keyboard_tray}, max weight capacity: {self.__max_weight_capacity}, current height: ' \
               f'{self.__current_height}, max height: {self.__max_height}'

writing_desk1 = WritingDesk(1, True, 80, 100, 180)
print(writing_desk1)

writing_desk2 = WritingDesk(4, False, 70, 100, 180)
print(writing_desk2)

writing_desk3 = WritingDesk(3, True, 100, 100, 180)
print(writing_desk3)

writing_desk4 = WritingDesk(2, False, 40, 100, 180)
print(writing_desk4)
