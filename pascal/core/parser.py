from pascal.core.types import Type
from pascal.core.token import Token
from pascal.core.lexer import Lexer
from pascal.core.ast import Num
from pascal.core.ast import BinOp


class Parser:

    def __init__(self, lexer):
        self.lexer = lexer 
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):
        """ """
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise ValueError(f"Improper token type!")

    def factor(self):
        """ Factor in the grammar
       
        factor : INTEGER | LPAREN expr RPAREN
        """
        token = self.current_token
        if token.type == Type.INTEGER:
            self.eat(Type.INTEGER)
            return Num(token)
        elif token.type == Type.LPAREN:
            self.eat(Type.LPAREN)
            node = self.expr()
            self.eat(Type.RPAREN)
            return node

    def term(self):
        """ Term in the grammar
       
        term : factor ((MULTIPLY | DIVIDE) factor)*
        """
        node = self.factor()

        while self.current_token.type in (Type.MULTIPLY, Type.DIVIDE):
            token = self.current_token
            if token.type == Type.MULTIPLY:
                self.eat(Type.MULTIPLY)
            elif token.type == Type.DIVIDE:
                self.eat(Type.DIVIDE)

            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def expr(self):
        node = self.term()

        while self.current_token.type in (Type.PLUS, Type.MINUS):

            token = self.current_token

            if token.type == Type.PLUS:
                self.eat(Type.PLUS)
            elif token.type == Type.MINUS:
                self.eat(Type.MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node

    def parse(self):
        return self.expr()
