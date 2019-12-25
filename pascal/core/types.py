from enum import Enum


class Type(Enum):
    INTEGER = "INTEGER"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    LPAREN = "("
    RPAREN = ")"
    EOF = "EOF"
