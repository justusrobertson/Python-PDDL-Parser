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
    def get_possible_actions(self, pddl_object, action_templates):
        possible_actions = []
        for action in action_templates:

            # is recursion needed here? I need a number of for loops = to the number of bindings
            for parameter in action.parameters:
                if len(action.parameters == 1):
                    possible_actions.append(action)
                    possible_actions[len(possible_actions) - 1].set_binding(parameter, parameter)
                    break
                # for parameterCombination in action.parameters:
                #     if parameter == parameterCombination:
                #         continue
                #
                #     possible_actions.append(action)
                #     possible_actions[len(possible_actions) - 1].set_binding(parameter, parameter)

    def compute_action_binds(self, objects, current_action, set_of_binds):
        if current_action


    def __str__(self):
        statement_to_print = ""
        for literal in self.literals:
            statement_to_print += f"{literal}\n"

        return statement_to_print


predicate_list = [
    Predicate("player", ["player"], False),
    Predicate("character", ["character"], False),
    Predicate("alive", ["character"], True)
]

predicate_list[0].set_binding("player", "arthur")
predicate_list[1].set_binding("character", "arthur")
predicate_list[2].set_binding("character", "arthur")

new_state = State(predicate_list)
print(new_state)

# print(predicate_list[0].to_string_ignoring_negation())
print(new_state.state_dictionary.get_val(f"{predicate_list[0].to_string_ignoring_negation()}"))
print(new_state.state_dictionary.get_val(f"{predicate_list[1].to_string_ignoring_negation()}"))
print(new_state.state_dictionary.get_val(f"{predicate_list[2].to_string_ignoring_negation()}"))

