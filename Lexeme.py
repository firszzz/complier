class Lexeme(object):

    def __init__(self, _lex, _type, _line, _char, _er):
        self.lex = _lex
        self.type = _type
        self.line = _line
        self.char = _char
        self.error = _er

    def output(self):
        if not self.error:
            return f'{self.line}' + '\t' + f'{self.char}'+'\t' + f'{self.type}'+'\t' + f'{self.lex}'
        else:
            return f'{self.line}' + '\t' + f'{self.char}'+'\t' + 'ошибка в лексеме ' + f'{self.lex}'
