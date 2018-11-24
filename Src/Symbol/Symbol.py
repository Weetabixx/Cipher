import string
from enum import Enum
import svgwrite


class Symbol:

    def __init__(self):
        pass
        # self.svg
        # self.name
        # self.letter
        # self.dot
        # self.long
        # self.linePosition
        # self.dotSize
        # self.dotPosition
        # self.thickness


def generateBaseSymbols():
    abc = list(string.ascii_lowercase)
    for letter in abc:
        symbol = Symbol()
        symbol.name = "topLeft"
        symbol.letter = letter
        symbol.dot = False
        symbol.long = False

        svgName = letter + '-cipher.svg'
        dwg = svgwrite.Drawing(svgName, profile='tiny')
        dwg.add(dwg.line((0, 20), (20, 20), stroke=svgwrite.rgb(10, 10, 16, '%')))
        dwg.add(dwg.line((20, 0), (20, 20), stroke=svgwrite.rgb(10, 10, 16, '%')))
        dwg.save()
        symbol.svg = dwg


class LinePosition(Enum):
    TOP_LEFT = 1
    TOP_RIGHT = 2
    RIGHT_TOP = 3
    RIGHT_BOTTOM = 4
    BOTTOM_RIGHT = 5
    BOTTOM_LEFT = 6
    LEFT_BOTTOM = 7
    LEFT_TOP = 8
