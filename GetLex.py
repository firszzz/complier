import Lexeme
import StatesTable


class GetLex(object):
    def __init__(self, test):
        self.keyWords = ["and", "array", "begin", "case", "const", "div", "do", "downto", "else", "end", "file", "for", "function", "goto", "if", "in", "label", "mod", "nil", "not", "of", "or", "packed", "procedure", "program", "record", "repeat", "set", "then", "to", "type", "until", "var", "while", "with"]
        self.delimiter = [".", ";", ",", "(", ")",  "[", "]", ":", "{", "}", "$", ".."]
        self.operators = ["+", "-", "*", "/", "=", ">", "<", "<>", ":=", ">=", "<=", "+=", "-=", "/=", "*="]
        self.separator = [" ", "\n", "\t", "\0", "\r"]
        self.state = "S"
        self.fr = open(test, "r")
        self.currChar = " "
        self.buf = ""
        self.lexStartsFrom = 0
        self.lexStartsFromLine = 0
        self.currIndexChar = 0
        self.currLine = 1
        self.stateTable = StatesTable.StatesTable()

    def getLex(self):
        ret = ""
        while True:
            match self.state:
                case "S":
                    self.buf = ""
                    self.lexStartsFrom = self.currIndexChar
                    self.lexStartsFromLine = self.currLine
                case "BACK":
                    self.state = "D"
                    bufNum = self.buf[len(self.buf) - 2]
                    self.buf = self.buf[len(self.buf) - 2:]
                    return Lexeme.Lexeme(bufNum, "Integer", self.lexStartsFromLine, self.lexStartsFrom, False)
                case "ERR":
                    return Lexeme.Lexeme(self.buf, ret, self.lexStartsFromLine, self.lexStartsFrom, True)

            prevState = self.state
            self.state = self.stateTable.getNewState(self.state, self.currChar)
            if self.state != "F":
                self.buf += self.currChar
            else:
                break

            self.currChar = self.fr.read(1)
            self.currIndexChar += 1

            if self.currChar == "\n":
                self.currIndexChar = 0
                self.currLine += 1

            match prevState:
                case "ENDSTR":
                    ret = "String"
                case "ID":
                    if self.buf in self.keyWords:
                        ret = "Keyword"
                    else:
                        ret = "Identifier"
                case "N":
                    ret = "Integer"
                case "NFP", "NFPORD", "NFPE", "NFPEO":
                    ret = "Float"
                case "D":
                    if self.buf in self.operators:
                        ret = "Operator"
                    elif self.buf in self.delimiter:
                        ret = "Delimiter"

            self.state = "S"
            if self.buf != "":
                return Lexeme.Lexeme(self.buf, ret, self.lexStartsFromLine, self.lexStartsFrom, False)
            else:
                return ""
