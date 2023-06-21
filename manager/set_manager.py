class SetManager:
    def __init__(self, desk_manager):
        self.desks = []
        self.position = 0
        for desk in desk_manager.get_desks():
            self.desks += [i for i in desk]

    def __iter__(self):
        self.position = 0
        return self

    def __next__(self):
        if self.position >= len(self.desks):
            raise StopIteration
        self.position += 1
        return self.desks[self.position - 1]

    def __len__(self):
        return len(self.desks)

    def __getitem__(self, item):
        return self.desks[item]

    