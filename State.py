from Action import *


class State:
    # literals should be fully bound predicates when being passed in
    def __init__(self, literals):
        # for iterating, perhaps using dict in the future will eliminate need
        # for this if it's iterable
        self.literals = literals
        self.state_dictionary = HashTable(len(literals))
        for literal in literals:
            self.state_dictionary.set_val(literal.name, True)

    def __str__(self):
        statement_to_print = ""
        for literal in self.literals:
            statement_to_print += f"{literal}\n"

        return statement_to_print


predicate_list = [
    Predicate("player", ["player"], False),
    Predicate("character", ["character"], False),
    Predicate("alive", ["character"], False)
]

predicate_list[0].set_binding("player", "arthur")
predicate_list[1].set_binding("character", "arthur")
predicate_list[2].set_binding("character", "arthur")

new_state = State(predicate_list)
print(new_state)
