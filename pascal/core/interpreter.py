from pascal.core.types import Type
from pascal.core.token import Token


class Interpreter:

    def __init__(self, text):
        self.text = text
        self._reset()

    def _reset(self):
        self.pos = 0
        self.current_char = self.text[self.pos] 
        self.current_token = None

    def get_next_token(self):
        """ Lexical analyzer 
       
        Splits up a sentence into tokens.
        """
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(Type.INTEGER, self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(Type.PLUS, self.current_char)

            if self.current_char == '-':
                self.advance()
                return Token(Type.MINUS, self.current_char)

            if self.current_char == '*':
                self.advance()
                return Token(Type.MULTIPLY, self.current_char)
 
            if self.current_char == '/':
                self.advance()
                return Token(Type.DIVIDE, self.current_char)
        
            raise ValueError(f"Unknown token type: {current_char}")

        return Token(Type.EOF, None)

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def advance(self):
        """ Move to the next character """
        self.pos += 1
        if self.pos > len(self.text)-1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def eat(self, token_type):
        """ """
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            raise ValueError(f"Improper token type!")

    def term(self):
        token = self.current_token
        self.eat(Type.INTEGER)
        return token.value

    def expr(self):
        self.current_token = self.get_next_token()

        result = self.term()
        while self.current_token.type in (
                Type.PLUS, Type.MINUS, Type.MULTIPLY, Type.DIVIDE):

            token = self.current_token

            if token.type == Type.PLUS:
                self.eat(Type.PLUS)
                result += self.term()
            elif token.type == Type.MINUS:
                self.eat(Type.MINUS)
                result -= self.term()
            elif token.type == Type.MULTIPLY:
                self.eat(Type.MULTIPLY)
                result *= self.term()
            elif token.type == Type.DIVIDE:
                self.eat(Type.DIVIDE)
                result /= self.term()

        return result
