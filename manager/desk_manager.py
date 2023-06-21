from loggin import ExceptionLogger
from model import desk
from utils import limiter


class DeskManager:
    def __init__(self):
        """class constructor"""
        self.desks = []

    def __len__(self):
        return len(self.desks)

    def add_desk(self, desk):
        """This method increases the list by adding a new object"""
        self.desks.append(desk)

    def __getitem__(self, index):
        try:
            return self.desks[index]
        except IndexError:
            return None

    def __iter__(self):
        """
        :return:  iterator for insects
        """
        return iter(self.desks)

    def get_desk(self, index):
        """this method provides access to individual elements of the "desk" list, which can be useful
        when performing some operations or obtaining information about a specific desk"""
        return self.desks[index]

    def get_desks(self):
        """this method goes through each element of "self.desks" and with the word yield each element will be returned
        which causes the method to pause and return a value. The method then saves its state so that the next call
        continues from the next element in the collection."""
        for desk in self.desks:
            yield desk

    def list_of_results(self):
        """

        :return: list of heights of desks
        """
        return [desk.height for desk in self.desks]

    def enumerate_list(self):
        """

        :return: ///
        """
        return [(desk.__str__(), index) for index, desk in enumerate(self.desks)]

    @ExceptionLogger(Exception, 'console')
    @limiter(3)
    def list_of_result_heights(self):
        """

        :return: ///
        """
        result = self.list_of_results()
        return [(desk,res) for desk, res in zip(self.desks, result)]

    def test_objects(self, test_function):
        return {"all": all(map(test_function, self.desks)), "any": any(map(test_function, self.desks))}


