from Predicate import *


class Action:
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters
        self.bindings = HashTable(len(parameters))
        for parameter in self.parameters:
            self.bindings.set_val(parameter, f"?{parameter}")
        self.preconditions = []
        self.effects = []

    # precondition should be a Predicate
    def add_precondition(self, precondition):
        # predicate input sanitization
        for parameter in precondition.parameters:
            if parameter not in self.parameters:
                print(f"The Predicate parameter '{parameter}' does not exist as an action parameter.")
                return
        self.preconditions.append(precondition)

    # effect should be a Predicate
    def add_effect(self, effect):
        # effect input sanitization
        for parameter in effect.parameters:
            if parameter not in self.parameters:
                print(f"The Effect parameter '{parameter}' does not exist as an action parameter.")
                return
        self.effects.append(effect)

    def set_binding(self, parameter, binding_value):
        self.bindings.set_val(parameter, binding_value)
        for predicate in self.preconditions:
            predicate.set_binding(parameter, binding_value)

    def __str__(self):
        statement_to_print = f"(:action {self.name}\n"
        statement_to_print += " \t:parameters ("
        for parameter in self.parameters:
            statement_to_print += f" {self.bindings.get_val(parameter)}"
        statement_to_print += ")\n"
        statement_to_print += "\t:precondition\n"
        statement_to_print += "\t\t(and\n"
        for precondition in self.preconditions:
            statement_to_print += f"\t\t\t{precondition}\n"

        statement_to_print += "\t\t)\n"
        statement_to_print += " \t:effect\n"
        statement_to_print += "\t\t(and\n"
        for effect in self.effects:
            statement_to_print += f"\t\t\t{effect}\n"
        statement_to_print += "\t\t)\n"
        return statement_to_print


# newAction = Action("move", ["mover", "oldLoc", "newLoc"])
# newAction.add_precondition(Predicate("at", ["mover", "oldLoc"], False))
# newAction.add_precondition(Predicate("at", ["mover", "newLoc"], True))
# newAction.add_effect(Predicate("at", ["mover", "oldLoc"], True))
# newAction.add_effect(Predicate("at", ["mover", "newLoc"], False))
#
# print(newAction.parameters)
# print(newAction.bindings)
# print(newAction)
