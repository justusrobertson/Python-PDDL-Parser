import enum
import collections
import typing
import math
import re
from State import State
from Action import Action
from Predicate import Predicate


class ArthurDomain():
    def __init__(self, literals, pddl_objects):
        self.state = State(literals)
        self.objects = pddl_objects
        self.playerWon = False

    def copyTo(self, other):
        assert isinstance(other, ArthurDomain)
        other.state = self.state
        other.playerWon = False

    def getCurrState(self):
        return self.state

    def getLegalNextMoves(self):
        return self.state.check_fully_bound_actions(self.state.get_possible_actions())

    # should be some number from 0 to the number of enabled actions
    def parseMove(self):
        # TODO: work on parsing the action
        return True

    def doMove(self, move):
        assert isinstance(Action, ArthurDomain)

        # do user sanitization and validation here
        self.state.update(move)

    def prettyPrint(self):
        return self.state.__str__()


object_list = ["ARTHUR", "EXCALIBUR", "WOODS", "LAKE"]

predicate_list = [
    Predicate("player", ["x"], False),
    Predicate("character", ["x"], False),
    Predicate("alive", ["x"], False),
    Predicate("at", ["x", "y"], False),
    Predicate("location", ["x"], False),
    Predicate("connected", ["x", "y"], False),
    Predicate("location", ["x"], False),
    Predicate("connected", ["x", "y"], False),
    Predicate("sword", ["x"], False),
    Predicate("at", ["x", "y"], False),
]

predicate_list[0].set_binding(predicate_list[0].parameters[0], object_list[0])
predicate_list[1].set_binding(predicate_list[1].parameters[0], object_list[0])
predicate_list[2].set_binding(predicate_list[2].parameters[0], object_list[0])

predicate_list[3].set_binding(predicate_list[3].parameters[0], object_list[0])
predicate_list[3].set_binding(predicate_list[3].parameters[1], object_list[2])

predicate_list[4].set_binding(predicate_list[4].parameters[0], object_list[2])

predicate_list[5].set_binding(predicate_list[5].parameters[0], object_list[2])
predicate_list[5].set_binding(predicate_list[5].parameters[1], object_list[3])

predicate_list[6].set_binding(predicate_list[6].parameters[0], object_list[3])

predicate_list[7].set_binding(predicate_list[7].parameters[0], object_list[3])
predicate_list[7].set_binding(predicate_list[7].parameters[1], object_list[2])

predicate_list[8].set_binding(predicate_list[8].parameters[0], object_list[1])

predicate_list[9].set_binding(predicate_list[9].parameters[0], object_list[1])
predicate_list[9].set_binding(predicate_list[9].parameters[1], object_list[3])

arthur_domain_0 = ArthurDomain(predicate_list, object_list)
print(arthur_domain_0.prettyPrint())

# while not arthur_domain_0.playerWon:
