
class PDDL_Object:
    def __init__(self, name, types):
        # a string
        self.name = name
        # an array of strings
        self.types = types

    def __str__(self):
        statement_to_print = ""
        statement_to_print += f"{self.name}"
        for i in self.types:
            statement_to_print += f" {i}"
        return statement_to_print

