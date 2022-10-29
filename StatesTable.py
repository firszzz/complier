

class StatesTable(object):
    def __init__(self):
        # S - Start, F - Finish,
        # ID - Identifier, D - Delimiter,
        # N = Number, NF = Number Float, STR - String,
        # COM - comment, ERR - error

        self.states = {
            'S': {
                "": "F",
                "_": "ID",
                "\n": "S",
                "\t": "S",
                " ": "S",
                "'": "STR1",
                '"': "STR2",
                ";": "D",
                "@": "D",
                "^": "D",
                "+": "D",
                "*": "D",
                "-": "D",
                "/": "D",
                "(": "D",
                ")": "D",
                "[": "D",
                "]": "D",
                ",": "D",
                ".": "D",
                ":": "D",
                "<": "D",
                ">": "D",
                "=": "D",
                "{": "COM1",
                "}": "ERR",
            },
            'ID': {
                "": "F",
                "_": "ID",
                "\n": "F",
                "\t": "F",
                " ": "F",
                '"': "F",
                "'": "F",
                ";": "F",
                "@": "F",
                "^": "F",
                "+": "F",
                "*": "F",
                "-": "F",
                "/": "F",
                "(": "F",
                ")": "F",
                "[": "F",
                "]": "F",
                ",": "F",
                ".": "F",
                ":": "F",
                "<": "F",
                ">": "F",
                "=": "F",
            },
            'N': {
                "": "F",
                "_": "ERR",
                "\n": "F",
                "\t": "F",
                " ": "F",
                '"': "F",
                "'": "F",
                ";": "F",
                "@": "F",
                "^": "F",
                "+": "F",
                "*": "F",
                "-": "F",
                "/": "F",
                "(": "F",
                ")": "F",
                "[": "F",
                "]": "F",
                ",": "F",
                ".": "NFPORD",
                ":": "F",
                "<": "F",
                ">": "F",
                "=": "F"},
            'D': {
                "": "F",
                "_": "F",
                "\n": "F",
                "\t": "F",
                " ": "F",
                '"': "F",
                "'": "F",
                ";": "F",
                "@": "F",
                "^": "F",
                "+": "D",
                "*": "COM2",
                "-": "D",
                "/": "COMS",
                "(": "F",
                ")": "F",
                "[": "F",
                "]": "F",
                ",": "F",
                ".": "D",
                ":": "D",
                "<": "D",
                ">": "D",
                "=": "D",
            },
            'COMS': {
                "\n": "S",
                "\r": "S",
                "": "S",
            },
            'COM1': {
                "}": "S",
            },
            'COM2': {
                "*": "COM2RD",
            },
            'COM2RD': {
                ")": "S",
            },
            'STR1': {
                "'": "ENDSTR",
            },
            'STR2': {
                '"': "ENDSTR",
            },
            'NFPORD': {
                ".": "BACK",
            },
            'BACK': {},
            'NFP': {
                "_": "ERR",
                "\n": "F",
                "\t": "F",
                " ": "F",
                '"': "F",
                "'": "F",
                ";": "F",
                "@": "F",
                "^": "F",
                "+": "F",
                "*": "F",
                "-": "F",
                "/": "F",
                "(": "F",
                ")": "F",
                "[": "F",
                "]": "F",
                ",": "F",
                ".": "ERR",
                ":": "F",
                "<": "F",
                ">": "F",
                "=": "F",
            },
            'NFPEO': {
                "_": "ERR",
                "\n": "F",
                "\t": "F",
                " ": "F",
                '"': "F",
                "'": "F",
                ";": "F",
                "@": "F",
                "^": "F",
                "+": "F",
                "*": "F",
                "-": "F",
                "/": "F",
                "(": "F",
                ")": "F",
                "[": "F",
                "]": "F",
                ",": "F",
                ".": "ERR",
                ":": "F",
                "<": "F",
                ">": "F",
                "=": "F",
            },
            'NFPE': {
                "_": "ERR",
                "\n": "F",
                "\t": "F",
                " ": "F",
                '"': "F",
                "'": "F",
                ";": "F",
                "@": "F",
                "^": "F",
                "+": "NFPEO",
                "*": "F",
                "-": "NFPEO",
                "/": "F",
                "(": "F",
                ")": "F",
                "[": "F",
                "]": "F",
                ",": "F",
                ".": "ERR",
                ":": "F",
                "<": "F",
                ">": "F",
                "=": "F"
            }
        }

        self.fillStates()

    def fillStates(self):
        for i in range(65, 91) and range(97, 123):
            self.states["S"][chr(i)] = "ID"
            self.states["ID"][chr(i)] = "ID"
            self.states["D"][chr(i)] = "F"
        for i in range(97,123):
            self.states["S"][chr(i)] = "ID"
            self.states["ID"][chr(i)] = "ID"
            self.states["D"][chr(i)] = "F"
        for i in range(0, 10):
            self.states["S"][str(i)] = "N"
            self.states["ID"][str(i)] = "ID"
            self.states["N"][str(i)] = "N"
            self.states["NFPORD"][str(i)] = "NFP"
            self.states["NFP"][str(i)] = "NFP"
            self.states["NFPEO"][str(i)] = "NFPEO"
            self.states["NFPE"][str(i)] = "NFPE"
            self.states["D"][str(i)] = "F"
            self.states["NFPORD"][str(i)] = "NFP"
        self.states["NFPORD"]['E'] = "NFPE"
        self.states["NFPORD"]['e'] = "NFPE"
        self.states["NFP"]['E'] = "NFPE"
        self.states["NFP"]['e'] = "NFPE"
        self.states["N"]['E'] = "NFPE"
        self.states["N"]['e'] = "NFPE"

    def getNewState(self, _state: str, _char: str):
        match _state:
            case 'COMS':
                if _char == "":
                    return "S"
                if _char in self.states[_state].keys():
                    return self.states[_state][_char]
                else:
                    return _state
            case 'STR1':
                if _char == "":
                    return "S"
                if _char in self.states[_state].keys():
                    return self.states[_state][_char]
                else:
                    return _state
            case 'STR2':
                if _char == "":
                    return "S"
                if _char in self.states[_state].keys():
                    return self.states[_state][_char]
                else:
                    return _state
            case 'COM1':
                if _char == "":
                    return "S"
                if _char in self.states[_state].keys():
                    return self.states[_state][_char]
                else:
                    return _state
            case 'COM2':
                if _char == "":
                    return "S"
                if _char in self.states[_state].keys():
                    return self.states[_state][_char]
                else:
                    return _state
            case "COM2RD":
                if _char in self.states[_state].keys():
                    return self.states[_state][_char]
                else:
                    return "COM2"
            case "ENDSTR":
                return "F"

        if _state in self.states.keys():
            if _char in self.states[_state].keys():
                return self.states[_state][_char]
        return "ERR"
