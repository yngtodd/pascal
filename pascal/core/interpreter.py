from pascal.core.types import Type
from pascal.core.token import Token


class Interpreter:

    def __init__(self, text):
        self.text = text
        self._reset()

    def _reset(self):
        self.pos = 0
        self.current_token = None

    def get_next_token(self):
        """ Lexical analyzer 
       
        Splits up a sentence into tokens.
        """
        if self.pos > len(self.text)-1:
            return Token(Type.EOF, None)

        current_char = self.text[self.pos]

        if current_char.isdigit():
            token = Token(Type.INTEGER, int(current_char))
            self.pos += 1
            return token

        if current_char == '+':
            token = Token(Type.PLUS, current_char)
            self.pos += 1
            return token
        
        raise ValueError(f"Unknown token type: {current_char}")


    def eat(self, token_type):
        """ """
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            raise ValueError(f"Improper token type!")

    def expr(self):
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat(Type.INTEGER)

        op = self.current_token
        self.eat(Type.PLUS)

        right = self.current_token
        self.eat(Type.INTEGER)

        return left.value + right.value
