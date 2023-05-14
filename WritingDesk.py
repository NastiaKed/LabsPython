class WritingDesk:
    __number_of_drawers = None
    __has_keyboard_tray = None
    __max_weight_capacity = None
    __current_height = None
    __max_height = None

    def __init__(self, number_of_drawers, has_keyboard_tray, max_weight_capacity, current_height, max_height):
        self.__number_of_drawers = number_of_drawers
        self.__has_keyboard_tray = has_keyboard_tray
        self.__max_weight_capacity = max_weight_capacity
        self.__current_height = current_height
        self.__max_height = max_height
        self.get_data()

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

    def get_data(self):
        print("Writing Desk:", " number of drawers:", self.__number_of_drawers, " has keyboard tray:",
              self.__has_keyboard_tray, " max weight capacity:", self.__max_weight_capacity, " current height:",
              self.__current_height, " max height:", self.__max_height)


writing_desk1 = WritingDesk(1, True, 80, 100, 180)

writing_desk2 = WritingDesk(4, False, 70, 100, 180)

writing_desk3 = WritingDesk(3, True, 100, 100, 180)

writing_desk4 = WritingDesk(2, False, 40, 100, 180)
