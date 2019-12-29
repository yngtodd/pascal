class AST:
    """ Base class for abstract syntax trees """
    pass


class BinOp(AST):
    """ Binary operation for abstract syntax trees """

    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Num(AST):
    """ Node for numbers in abstract syntax trees """

    def __init__(self, token):
        self.token = token
        self.value = token.value

