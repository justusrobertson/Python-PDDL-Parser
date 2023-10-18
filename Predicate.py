from HashMap import HashTable


class Predicate:
    def __init__(self, name, parameters, binding_values):
        self.name = name
        self.parameters = parameters
        self.bindings = HashTable(len(parameters))
        i = 0
        for parameter in self.parameters:
            self.bindings.set_val(parameter, binding_values[i])
            i += 1

    def get_predicate_form(self):
        statement_to_print = f"({self.name}"
        for parameter in self.parameters:
            statement_to_print += f" ?{parameter}"
        statement_to_print += ")"
        print(statement_to_print)

    def __str__(self):
        statement_to_print = f"({self.name}"
        for parameter in self.parameters:
            statement_to_print += f" {self.bindings.get_val(parameter)}"
        statement_to_print += ")"
        return statement_to_print

# new_predicate = Predicate("at", ["obj", "location"], ["var 1", "var 2"])
# new_predicate.get_predicate_form()
# print(new_predicate)

