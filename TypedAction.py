from Predicate import *


class TypedAction:
    # bindings are not required so that we may have 'action templates'
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters
        self.bindings = dict()
        for parameter in self.parameters:
            self.bindings[parameter] = None
        self.preconditions = []
        self.effects = []

    def __copy__(self, other):
        self.name = other.name
        self.parameters = other.parameters
        self.bindings = dict()
        for parameter in self.parameters:
            self.bindings[parameter] = other.bindings[parameter]
        for precondition in other.preconditions:
            current_predicate = Predicate("", "", False)
            current_predicate.__copy__(precondition)
            self.add_precondition(current_predicate)

        for effect in other.effects:
            current_predicate = Predicate("", "", False)
            current_predicate.__copy__(effect)
            self.add_effect(current_predicate)

    # precondition should be a Predicate
    def add_precondition(self, precondition):
        # predicate input sanitization
        for parameter in precondition.parameters:
            for self_params in self.parameters:
                if parameter not in self_params.name and self.parameters[-1] == self_params:
                    print(f"The Predicate parameter '{parameter}' does not exist as an action parameter.")
                    return
                if parameter == self_params.name:
                    self.preconditions.append(precondition)
                    return

    # effect should be a Predicate
    def add_effect(self, effect):
        # effect input sanitization
        #TODO probably implement __eq__(other) in whatever type of object parameter is
        for parameter in effect.parameters:
            for self_params in self.parameters:
                if parameter not in self_params.name and self.parameters[-1] == self_params:
                    print(f"The Effect parameter '{parameter}' does not exist as an action parameter.")
                    return
                if parameter == self_params.name:
                    self.effects.append(effect)
                    return

    def is_fully_bound(self):
        for parameter in self.parameters:
            if self.bindings[parameter] == None:
                return False

        return True

    def set_binding(self, parameter, binding_value):
        self.bindings[parameter] = binding_value
        for predicate in self.preconditions:
            predicate.set_binding(parameter, binding_value)
        for predicate in self.effects:
            predicate.set_binding(parameter, binding_value)

    def __str__(self):
        statement_to_print = f"(:action {self.name}\n"
        statement_to_print += " \t:parameters ("
        for parameter in self.parameters:
            statement_to_print += f" {self.bindings[parameter]}"
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

#
# newAction = Action("move", ["mover", "oldLoc", "newLoc"])
# newAction.add_precondition(Predicate("at", ["mover", "oldLoc"], False))
# newAction.add_precondition(Predicate("at", ["mover", "newLoc"], True))
# newAction.add_effect(Predicate("at", ["mover", "oldLoc"], True))
# newAction.add_effect(Predicate("at", ["mover", "newLoc"], False))
#
# print(newAction.is_fully_bound())
#
# newAction.set_binding("mover", "arthur")
# newAction.set_binding("oldLoc", "woods")
#
# print(newAction.parameters)
# print(newAction.bindings)
# print(newAction)
#
# copyAction = Action("", [])
# copyAction.__copy__(newAction)
# newAction.set_binding("newLoc", "lake")
#
# print(newAction.is_fully_bound())
#
# print(copyAction.bindings)
# print(newAction)
# print(copyAction)
