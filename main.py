from model.writing_desk import WritingDesk
from model.coffee_table import CoffeTable
from manager.desk_manager import DeskManager


if __name__ == '__main__':
    manager = DeskManager()

    manager.add_desk(WritingDesk(1, True, 80, 100, 180, 80, 120, 200))
    manager.add_desk(WritingDesk(2, True, 80, 100, 150, 80, 120, 200))
    manager.add_desk(WritingDesk(3, True, 80, 100, 120, 80, 120, 200))
    manager.add_desk(CoffeTable(4, False, 70, 100, 180))
    manager.add_desk(CoffeTable(3, True, 100, 100, 180))
    manager.add_desk(CoffeTable(2, False, 40, 100, 180))

    for desk in manager.get_desks():
        print(id(desk), desk)
