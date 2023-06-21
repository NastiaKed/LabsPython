class IsNotSnakeCase(Exception):
    def __init__(self):
        super().__init__("function name is not snake case")


class ToManyCalls(Exception):
    def __init__(self):
        super().__init__("function to many calls")
