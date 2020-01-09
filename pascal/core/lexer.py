from pascal.core.types import Type
from pascal.core.token import Token


class Lexer:

    def __init__(self, text):
        self.text = text
        self._reset()

    def _reset(self):
        self.pos = 0
        self.current_char = self.text[self.pos] 

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

            if self.current_char == '(':
                self.advance()
                return Token(Type.LPAREN, self.current_char)

            if self.current_char == ')':
                self.advance()
                return Token(Type.RPAREN, self.current_char)

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
