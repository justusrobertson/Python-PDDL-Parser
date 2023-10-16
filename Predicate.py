from HashMap import HashTable


class Predicate:
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters
        self.bindings = HashTable(len(parameters))
        for parameter in parameters:
            self.bindings.set_val(parameter, "object ")

    def to_string(self):
        statement_to_print = f"({self.name}"
        for parameter in self.parameters:
            statement_to_print += f" ?{parameter}"
            # print(f"{self.bindings.get_val(self.parameters[1])}")
        statement_to_print += ")"
        print(statement_to_print)


new_predicate = Predicate("at", ["obj", "location"])
new_predicate.to_string()