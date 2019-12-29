# -*- coding: utf-8 -*-
from pascal.core.lexer import Lexer
from pascal.core.parser import Parser
from pascal.core.interpreter import Interpreter


def main():
    while True:
        try:
            text = input('pascal> ')
        except EOFError:
            break

        if not text:
            continue

        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        print(result)


if __name__=='__main__':
    main()

