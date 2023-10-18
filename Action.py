from Predicate import *


class Action:
    def __init__(self, name, parameters, binding_values, preconditions):
        self.name = name
        self.parameters = parameters
        self.bindings = HashTable(len(parameters))
        i = 0
        for parameter in self.parameters:
            self.bindings.set_val(parameter, binding_values[i])
            i += 1
        self.preconditions = preconditions



newAction = Action("move", ["mover", "oldLoc", "newLoc"], ["arthur", "forest", "lake"], "")

print(newAction.parameters)
print(newAction.bindings)

