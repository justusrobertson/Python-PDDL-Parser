from Predicate import *


class Action:
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters
        self.bindings = HashTable(len(parameters))
        i = 0
        for parameter in self.parameters:
            self.bindings.set_val(parameter, f"?{parameter}")
            i += 1
        self.preconditions = []


    # precondition should be a Predicate
    def add_precondition(self, precondition):
        self.preconditions.append(precondition)
    def set_binding(self, parameter, binding_value):
        self.bindings.set_val(parameter, binding_value)
        for predicate in self.preconditions:
            predicate.set_binding(parameter, binding_value)


effectsList = [Predicate("at", ["mover", "location"])]
newAction = Action("move", ["mover", "oldLoc", "newLoc"])
newAction.add_precondition(Predicate("at", ["mover", "location"]))
print(newAction.parameters)
print(newAction.bindings)
print(newAction.preconditions[0])
