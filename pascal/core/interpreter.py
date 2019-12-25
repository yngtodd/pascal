from pascal.core.types import Type
from pascal.core.token import Token
from pascal.core.lexer import Lexer


class Interpreter:

    def __init__(self, text):
        self.lexer = Lexer(text)
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):
        """ """
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise ValueError(f"Improper token type!")

    def factor(self):
        """ Return an INTEGER token value.

        factor : INTEGER
        """
        token = self.current_token
        self.eat(Type.INTEGER)
        return token.value

    def term(self):
        result = self.factor()

        while self.current_token.type in (Type.MULTIPLY, Type.DIVIDE):
            token = self.current_token
            if token.type == Type.MULTIPLY:
                self.eat(Type.MULTIPLY)
                result *= self.factor()
            elif token.type == Type.DIVIDE:
                self.eat(Type.DIVIDE)
                result /= self.factor()

        return result

    def expr(self):
        result = self.term()

        while self.current_token.type in (Type.PLUS, Type.MINUS):

            token = self.current_token

            if token.type == Type.PLUS:
                self.eat(Type.PLUS)
                result += self.term()
            elif token.type == Type.MINUS:
                self.eat(Type.MINUS)
                result -= self.term()

        return result
