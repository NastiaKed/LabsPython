from desk import Desk


class CoffeTable(Desk):

    def __init__(self, number_of_shelves, max_number_of_guests, height, width, length):
        self.number_of_shelves = number_of_shelves
        self.max_number_of_guests = max_number_of_guests
        super().__init__(height, width, length)

    def __str__(self):
        return f'CoffeTable(number_of_shelves={self.number_of_shelves}, max_number_of_guests={self.max_number_of_guests})'

    def adjust_height(self, centimeters: int):
        raise NotImplementedError("CoffeTable height is not adjustable")

    def move_down(self, centimeters: int):
        raise NotImplementedError("CoffeTable height is not adjustable")
