from pascal.core.types import Type


class Token:
    """ Token to be interpreted 
   
    Args:
        type_: The type of token
    """

    def __init__(self, type_: Type, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f'Token(type_={self.type}, value={self.value})'

