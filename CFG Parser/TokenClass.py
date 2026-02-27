class Token:
    def __init__(self, type, value, line):
        self.value = value
        self.type = type
        self.line = line
    # self.column = column

    def print_token(self):
        print("Token:")
        print(f"  Type : {self.type}")
        print(f"  Value: {self.value}")
        print(f"  Line : {self.line}")


# pre-defined tokens for testing

tokens = [
    Token("IDENTIFIER", "x", 1),
    Token("ASSIGN", "=", 1),
    Token("NUMBER", "10", 1),
    Token("SEMICOLON", ";", 1),

    Token("FOR", "for", 2),
    Token("LEFT_PAREN", "(", 2),
    Token("IDENTIFIER", "i", 2),
    Token("ASSIGN", "=", 2),
    Token("NUMBER", "0", 2),
    Token("SEMICOLON", ";", 2),

    Token("IDENTIFIER", "i", 2),
    Token("LESS_THAN", "<", 2),
    Token("NUMBER", "5", 2),
    Token("SEMICOLON", ";", 2),

    Token("IDENTIFIER", "i", 2),
    Token("ASSIGN", "=", 2),
    Token("IDENTIFIER", "i", 2),
    Token("PLUS", "+", 2),
    Token("NUMBER", "1", 2),
    Token("RIGHT_PAREN", ")", 2),

    Token("LEFT_BRACE", "{", 2),

    Token("IDENTIFIER", "y", 3),
    Token("ASSIGN", "=", 3),
    Token("IDENTIFIER", "i", 3),
    Token("MULTIPLY", "*", 3),
    Token("NUMBER", "2", 3),
    Token("SEMICOLON", ";", 3),

    Token("IDENTIFIER", "y", 4),
    Token("ASSIGN", "=", 4),
    Token("IDENTIFIER", "x", 4),
    Token("SEMICOLON", ";", 4),

    Token("IDENTIFIER", "z", 5),
    Token("ASSIGN", "=", 5),
    Token("NUMBER", "2", 5),
    Token("PLUS", "+", 5),
    Token("IDENTIFIER", "i", 5),
    Token("SEMICOLON", ";", 5),

    Token("RIGHT_BRACE", "}", 6)
]
