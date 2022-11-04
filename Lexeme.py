# -*- coding: utf-8 -*-

class Lexeme(object):

    def __init__(self, _lex, _type, _line, _char_num):
        self.lex = _lex.lower()
        self.type = _type
        self.line = _line
        self.char_num = _char_num
        self.mean = self.is_mean_num()

    def is_mean_num(self):
        if self.lex:
            if self.lex[0] == "$":
                return int(self.lex[1:], 16)
            elif self.lex[0] == "&":
                return int(self.lex[1:], 8)
            elif self.lex[0] == "%":
                return int(self.lex[1:], 2)
            elif self.type == "String":
                mean = self.lex[1:len(self.lex) - 1]
                return mean
            try:
                mean = float(self.lex)
                if mean.is_integer():
                    return int(mean)
                return mean
            except:
                pass
        return ""

    def output(self):
        if self.type == "Empty":
            return ''
        if self.mean != '':
            num_mean = self.mean
            if type(self.mean) is int:
                num_mean = self.mean
            elif type(self.mean) is str:
                num_mean = self.mean
            else:
                num_mean = "{0:.15f}".format(self.mean).rstrip('0')
            return f'{self.line}' + '\t' + f'{self.char_num}' + '\t' + f'{self.type}' + '\t' + f'{self.lex}' + '\t' + f'{num_mean} '
        return f'{self.line}' + '\t' + f'{self.char_num}' + '\t' + f'{self.type}' + '\t' + f'{self.lex}'
