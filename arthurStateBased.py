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
    def parseMove(self, inputStr):

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

predicate_list[0].set_binding()


arthur_domain_0 = ArthurDomain()
print(arthur_domain_0.prettyPrint())

while not arthur_domain_0.playerWon:
