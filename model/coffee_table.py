from model.desk import Desk


class CoffeTable(Desk):

    def __init__(self, number_of_shelves, max_number_of_guests, height, width, length):
        self.number_of_shelves = number_of_shelves
        self.max_number_of_guests = max_number_of_guests
        super().__init__(height, width, length)
        self.material_list = {"iron", "glass"}

    def __str__(self):
        return f'CoffeTable(number_of_shelves={self.number_of_shelves}, ' \
               f'max_number_of_guests={self.max_number_of_guests})'

    def adjust_height(self, centimeters: int):
        """method that increases the height of the table (if it does not exceed the maximum allowed)"""
        raise NotImplementedError("CoffeTable height is not adjustable")

    def move_down(self, centimeters: int):
        """a method that reduces the height of the desk"""
        raise NotImplementedError("CoffeTable height is not adjustable")
