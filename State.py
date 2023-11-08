from Action import *


class State:
    # literals should be fully bound predicates when being passed in
    def __init__(self, literals):
        # for iterating, perhaps using dict in the future will eliminate need
        # for this if it's iterable
        self.literals = literals
        self.state_dictionary = HashTable(len(literals))
        for literal in literals:
            self.state_dictionary.set_val(f"{literal.to_string_ignoring_negation()}", not literal.is_negated)

    # action_templates is a list of Actions
    def get_possible_actions(self, pddl_objects, action_templates, set_of_binds):
        possible_actions = []
        for action in action_templates:
            self.compute_action_binds(pddl_objects, action, set_of_binds)

    # current action is an action that's initially unbound.
    def compute_action_binds(self, objects, current_action, set_of_binds):
        if not current_action.is_fully_bound():
            for pddl_object in objects:
                copy_action = Action("", "")
                copy_action.__copy__(current_action)
                # find the first unbound parameter the break
                for parameter in copy_action.parameters:
                    if copy_action.bindings.get_val(parameter).__contains__("?"):
                        copy_action.set_binding(parameter, pddl_object)
                        self.compute_action_binds(objects, copy_action, set_of_binds)

        else:
            set_of_binds.append(current_action)

        return set_of_binds

    def __str__(self):
        statement_to_print = ""
        for literal in self.literals:
            statement_to_print += f"{literal}\n"

        return statement_to_print


object_list = ["arthur", "bill"]

predicate_list = [
    Predicate("player", ["player"], False),
    Predicate("character", ["character"], False),
    Predicate("alive", ["character"], True)
]

predicate_list[0].set_binding("player", object_list[0])
predicate_list[1].set_binding("character", object_list[0])
predicate_list[2].set_binding("character", object_list[0])

action_list = [
    Action("kill", ["victim"]),
    Action("transform", ["preTransformCharacter", "postTransformCharacter"])
]
action_list[0].add_precondition(Predicate("alive", ["victim"], True))
action_list[0].add_effect(Predicate("alive", ["victim"], False))
action_list[1].add_precondition(Predicate("character", ["preTransformCharacter"], False))
action_list[1].add_effect(Predicate("character", ["preTransformCharacter"], True))
action_list[1].add_effect(Predicate("character", ["postTransformCharacter"], False))

new_state = State(predicate_list)
print(new_state)
set_of_new_bindings = []
new_state.get_possible_actions(object_list, action_list, set_of_new_bindings)
# new_state.compute_action_binds(object_list, action_list[1], set_of_new_bindings)

for fully_bound_action in set_of_new_bindings:
    print(fully_bound_action)
# print(predicate_list[0].to_string_ignoring_negation())
# print(new_state.state_dictionary.get_val(f"{predicate_list[0].to_string_ignoring_negation()}"))
# print(new_state.state_dictionary.get_val(f"{predicate_list[1].to_string_ignoring_negation()}"))
# print(new_state.state_dictionary.get_val(f"{predicate_list[2].to_string_ignoring_negation()}"))

