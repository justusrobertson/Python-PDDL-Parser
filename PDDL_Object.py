
class PDDL_Object:
    def __init__(self, name, types):
        # a string
        self.name = name
        # an array of strings
        self.types = types

    def __str__(self):
        statement_to_print = ""
        if self.types:
            statement_to_print += f"{self.name} -"
        else:
            statement_to_print += f"{self.name} "
        for i in self.types:
            if i == self.types[-1]:
                statement_to_print += f" {i}"
            else:
                statement_to_print += f" {i},"
        return statement_to_print

