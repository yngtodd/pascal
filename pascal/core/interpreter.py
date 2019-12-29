from pascal.core.types import Type
from pascal.core.token import Token
from pascal.core.lexer import Lexer


class NodeVisitor:

    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method.')


class Interpreter(NodeVisitor):

    def __init__(self, parser):
        self.parser = parser

    def visit_BinOp(self, node):
        if node.op.type == Type.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        if node.op.type == Type.MINUS:
            return self.visit(node.left) - self.visit(node.right)
        if node.op.type == Type.MULTIPLY:
            return self.visit(node.left) * self.visit(node.right)
        if node.op.type == Type.DIVISION:
            return self.visit(node.left) / self.visit(node.right)

    def visit_Num(self, node):
        return node.value

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)

