from HashMap import HashTable


class Predicate:
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters
        self.bindings = HashTable(len(parameters))
        i = 0
        for parameter in self.parameters:
            self.bindings.set_val(parameter, f"?{parameter}")
            i += 1

    def set_binding(self, parameter, binding_value):
        self.bindings.set_val(parameter, binding_value)

    def get_predicate_form(self):
        statement_to_print = f"({self.name}"
        for parameter in self.parameters:
            statement_to_print += f" ?{parameter}"
        statement_to_print += ")"
        print(statement_to_print)

    # Prints the parameter by default, prints the binding otherwise.
    def __str__(self):
        statement_to_print = f"({self.name}"
        for parameter in self.parameters:
            statement_to_print += f" {self.bindings.get_val(parameter)}"
        statement_to_print += ")"
        return statement_to_print


new_predicate = Predicate("at", ["obj", "location"])
# new_predicate.get_predicate_form()
print(new_predicate)
new_predicate.set_binding("obj", "arthur")
print(new_predicate)
new_predicate.set_binding("location", "woods")
print(new_predicate)

