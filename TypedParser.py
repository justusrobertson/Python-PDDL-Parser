import copy
from TypedState import TypedState
from TypedAction import TypedAction
from TypedPredicate import TypedPredicate
from PDDL_Object import PDDL_Object
from Parameter_Object import Parameter_Object


class TypedParser:
    def readObjects(self, fileName):
        localArray = []
        with open(fileName) as file:
            for line in file:
                # Reads only after the objects token
                if '(:objects' in line:
                    line = line.split()
                    line.pop(0)
                    
                    if not line:
                        line = file.readline().split()

                    while ')' not in line[0].strip():
                        while line[0] != '-':
                            pddlObject = PDDL_Object(line.pop(0), [])
                            localArray.append(pddlObject)

                        if line[0] == '-':
                            line.pop(0)
                            for objs in localArray:
                                objs.types.append(line[0])
                                objects_array.append(objs)
                            localArray = []
                            line.pop(0)

                        if len(line) == 0:
                            line = file.readline().split()

    def readTypes(self, fileName):
        localDictionary = {}
        newType = ''
        with open(fileName) as file:
            for line in file:
                # Reads only after the types token
                if '(:types' in line:
                    line = line.split()
                    line.pop(0)

                    while '(:constants' not in line[0].strip():
                        newType = line.pop(-1).strip(')')
                        line.pop(-1)
                        localDictionary[newType] = line
                        line = file.readline().split()

                    for obj in objects_array:
                        for objType in obj.types:
                            for key in localDictionary:
                                for newTypeDict in localDictionary[key]:
                                    if objType == newTypeDict:
                                        obj.types.append(key)
                                        break

    # Reads in the initial state from the problem file
    def readInitState(self, fileName):
        localPred = ''
        localArray = []
        with open(fileName) as file:
            for line in file:
                # Reads only after the initial token
                if '(:init' in line:
                    line = file.readline().split()
                    # Reads until it reaches the next token
                    while '(:goal' not in line:
                        # Reads until the line is empty
                        while len(line) != 0:
                            # Adds the predicate to the array
                            if '(' in line[0]:
                                line[0] = line[0].lstrip('(')
                                localPred = line.pop(0)

                            if line[0] == (')'):
                                return
                            
                            i = 0
                            while i < len(objects_array):
                                
                                line[0] = line[0].rstrip(')')
                                if objects_array[i].name == line[0]:
                                    pddlObject = objects_array[i]
                                    line.pop(0)
                                    localArray.append(pddlObject)
                                    # Creating the predicate
                                    if not line or '(' in line[0]:
                                        fileParser.setPredsToObjects(init_array, localPred, localArray)
                                        localArray = []
                                        i = 0
                                        break
                                i += 1
                        if len(line) == 0:
                            line = file.readline().split()
                            #print(line)

    # Reads in the possible predicates from the domain file
    def readPredicate(self, fileName):
        localName = ''
        localArray = []
        localType = []
        with open(fileName) as file:
            for line in file:
                # Reads only after the predicate token
                if '(:predicates' in line:
                    line = file.readline()
                    # Reads until the final ')' - takes up whole line
                    while line.strip()[0] != ')':
                        # Gets rid of whitespace and '('
                        line = line.strip().lstrip('(').split()
                        localName = line.pop(0)
                        # Goes over the remaining variables in the sliceLine array
                        while line:
                            if '?' in line[0]:
                                localArray.append(line[0].strip('?'))
                                line.pop(0)

                            if '-' in line[0]:
                                line.pop(0)
                                localType.append(line[0].strip(')'))
                                line.pop(0)

                        # Creates new predicate object and sets it to the dictionary
                        #predicate_dictionary[localName] = TypedPredicate(localName, localArray, localType, False)
                        predicate_dictionary[localName] = TypedPredicate(localName, localArray, False)
                        
                        localType = []
                        localArray = []
                        # Reads in the next line
                        line = file.readline()
        
    # Sets the objects to the corresponding variable in the initial state
    def setPredsToObjects(self, array, localName, localArray):
        pred = copy.deepcopy(predicate_dictionary[localName])
        i = 0
        while i < len(pred.parameters):
            pred.set_binding(pred.parameters[i], localArray[i])
            i += 1
        init_array.append(pred)

    def readActions(self, fileName):
        # Name of action
        actionName = ''
        # List of parameters
        parameters = []
        paramObject_array = []
        local_Param_array = []
        
        with open(fileName) as file:
            for line in file:
                line = line.split()

                # Read (:action token - take rest of the line and assign it to the actionName
                if '(:action' in line:
                    actionName = line.pop(-1)

                # Read :parameters token - take the rest before the ')' and add them to a list
                if ':parameters' in line:
                    line.pop(0)
                    
                    i = 0
                    for params in line:
                        if params.strip()[-1] == ')':
                            action_dictionary.append(TypedAction(actionName, paramObject_array))

                            parameters = []
                            paramObject_array = []

                        # typed
                        if params == '-':
                            paramType = line[i + 1].strip(')')
                            paramObject = Parameter_Object(parameters[len(parameters) - 1], paramType)
                            paramObject_array.append(paramObject)
                            local_Param_array.append(paramObject)

                        else:
                            parameters.append(params.strip('(?'))

                        i += 1
                        
                    i = 0
                    while i <= (len(action_dictionary) - 1):
                        pred = copy.deepcopy(action_dictionary[i])
                        if action_dictionary[-1].is_fully_bound():
                            break
                        for actionsBindings in pred.bindings:
                            for actionsParams in pred.parameters:
                                if actionsBindings.name == actionsParams.name:
                                    pred.set_binding(actionsBindings, actionsParams)
                                    break
                        action_dictionary[i] = pred
                        i += 1

                if ':precondition' in line:
                    fileParser.readActionsHelper(file, 'precondition')
                    print()
                
                if ':effect' in line:
                    fileParser.readActionsHelper(file, 'effect')
                    print()

            line = file.readline()
    
    def readActionsHelper(self, file, token):
        localName = ''
        localArray = []
        negated = False

        line = file.readline()
        line = file.readline().split()

        # Reads until the final ')' - takes up whole line
        while ')' not in line[0].strip():
            if 'not' in line[0]:
                negated = True
                line.pop(0)

            # Gets the name
            if '(' in line[0]:
                line[0] = line[0].lstrip('(')
                localName = line.pop(0)

            while '?' in line[0]:
                line[0] = line[0].strip('?')

                if ')' in line[0]:
                    localArray.append(line[0].strip(')'))
                    predicateObject = TypedPredicate(localName, localArray, negated)
                    localArray = []
                    line.pop(0)
                    length = len(action_dictionary) - 1

                    if token == 'effect':
                        action_dictionary[length].add_effect(predicateObject)
                    
                    if token == 'precondition':
                        action_dictionary[length].add_precondition(predicateObject)

                    if len(line) == 0:
                        line = file.readline().split()
                        break
                    
                else:
                    localArray.append(line.pop(0))

            negated = False

    def getObjects(self):
        return objects_array
    
    def getinitState(self):
        return init_array
    
    def getPredicateDict(self):
        return predicate_dictionary
    
    def getActions(self):
        return action_dictionary


predicate_dictionary = {}
predicate_dictionary_copy = {}
pred = {}
action_dictionary = []
objects_array = []
init_array = []
fileParser = TypedParser()

domainFile = 'oz-typed/domain.pddl'
probFile = 'oz-typed/prob01.pddl'

fileParser.readPredicate(domainFile)
fileParser.readObjects(probFile)
fileParser.readTypes(domainFile)
fileParser.readInitState(probFile)
fileParser.readActions(domainFile)

print("\nObjects Array:")
print([str(x) for x in objects_array])

print("\nInit State:")
i = 0
while i < len(init_array):
    print(init_array[i])
    i += 1

print("\nPredicate Array:")
for key in predicate_dictionary:
    print(predicate_dictionary[key])

print("\nActions:")
for action in action_dictionary:
    print(action)