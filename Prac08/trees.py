"""
CP1404/CP5632 Practical
Tree class with inherited (specialised tree) classes
Trevor Andersen
"""
import random

TREE_LEAVES_PER_ROW = 3


class Tree:
    """ represent a tree, with trunkHeight and a number of leaves """
    def __init__(self):
        """ initialise a Tree with trunkHeight of 1 and one full row of leaves """
        self._trunkHeight = 1
        self._leaves = TREE_LEAVES_PER_ROW

    def __str__(self):
        """ return a string representation of the full Tree, e.g.
         ###
         ###
          |
          |    """
        return self.getASCIILeaves() + self.getASCIITrunk()

    def getASCIILeaves(self):
        """ return a string representation of the tree's leaves """
        result = ""
        if self._leaves % TREE_LEAVES_PER_ROW > 0:
            result += "#" * (self._leaves % TREE_LEAVES_PER_ROW)
            result += "\n"
        for i in range(self._leaves // TREE_LEAVES_PER_ROW):
            result += "#" * TREE_LEAVES_PER_ROW
            result += "\n"
        return result

    def getASCIITrunk(self):
        """ return a string representation of the tree's trunk """
        result = ""
        for i in range(self._trunkHeight):
            result += " | \n"
        return result

    def grow(self, sunlight, water):
        """ take in an amount sunlight and water
        randomly grow the trunkHeight by a number between 0 and water
        randomly increase the leaves by a number between 0 and sunlight """
        self._trunkHeight += random.randint(0, water)
        self._leaves += random.randint(0, sunlight)


class EvenTree(Tree):
    """ represent an even tree, one that only grows leaves in full rows """

    def grow(self, sunlight, water):
        """ takes in an amount of sunlight and water
        grow like a normal tree, but fill out each row of leaves """
        Tree.grow(self, sunlight, water)
        while self._leaves % 3 != 0:
            self._leaves += 1


class UpsideDownTree(Tree):
    """ represent an upside-down tree; just like a normal tree, but appears upside-down """

    def __str__(self):
        """  return a string representation of the full tree, upside-down compared to a normal tree """
        return self.getASCIITrunk() + self.getASCIILeaves()


class WideTree(Tree):
    """ represent a wide tree: grows twice as wide as a normal tree, e.g.
 #####
 ######
 ######
   ||
   ||  """
    def getASCIITrunk(self):
        result = ""
        for i in range(self._trunkHeight):
            result += " || \n"
        return result

    def getASCIILeaves(self):
        result = ""
        if self._leaves % TREE_LEAVES_PER_ROW > 0:
            result += "#" * (2*(self._leaves % TREE_LEAVES_PER_ROW))
            result += "\n"
        for i in range(self._leaves // TREE_LEAVES_PER_ROW):
            result += "#" * (2*(TREE_LEAVES_PER_ROW))
            result += "\n"
        return result

class QuickTree(Tree):
    """ represent a tree that grows more quickly """

    def grow(self, sunlight, water):
        self._trunkHeight += water
        self._leaves += sunlight


class FruitTree(Tree):
    """ represent a tree that has fruit as well as leaves, e.g.
.
...
##
###
###
 |
 |  """
    def __init__(self):
        super().__init__()
        self.number_of_fruit = 1
        self.fruit = TREE_LEAVES_PER_ROW

    def grow(self, sunlight, water):
        fruit_number = random.randint(1,100)
        if fruit_number >= 50:
            self.number_of_fruit += 1
        elif fruit_number <= 20:
            self.number_of_fruit -= 1
        super().grow(sunlight,water)

    def getASCIILeaves(self):
        """ return a string representation of the tree's leaves """
        result = ""
        if self._leaves % TREE_LEAVES_PER_ROW > 0:
            result += "#" * (self.number_of_fruit % TREE_LEAVES_PER_ROW)
            result += "\n"
        if self.number_of_fruit % TREE_LEAVES_PER_ROW > 0:
            result += "." * (self.number_of_fruit % TREE_LEAVES_PER_ROW)
            result += "\n"
        for i in range(self._leaves // TREE_LEAVES_PER_ROW):
            result += "#" * TREE_LEAVES_PER_ROW
            result += "\n"
        for i in range(self.number_of_fruit // TREE_LEAVES_PER_ROW):
            result += "." * TREE_LEAVES_PER_ROW
            result += "\n"
        return result


class PineTree(Tree):
    """ represents a pine tree, e.g.
   *
  ***
 *****
*******
   |
   |    """
    pass