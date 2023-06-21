

class DeskManager:
    def __init__(self):
        self.desks = list()

    def add_desk(self, desk):
        self.desks.append(desk)

    def get_desk(self, index):
        return self.desks[index]

    def get_desks(self):
        for desk in self.desks:
            yield desk
