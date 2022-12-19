import os.path
import sys

import GetLex
import Parse
import Semantic

# -*- coding: utf-8 -*-


if __name__ == '__main__':
    testtype = '4'
    starttest = 1
    try:
        testtype = sys.argv[1]
        starttest = int(sys.argv[2])
    except:
        pass
    if testtype == '1':
        directory = 'lexer_tests'
    elif testtype == '2':
        directory = 'parse_tests'
    elif testtype == '3':
        directory = 'parser_tests'
    elif testtype == '4':
        directory = 'semantic_tests'
    else:
        raise Exception(
            "Введите 1 для лексического анализатора, 2 для простых выражений, 3 для синтаксического анализатора, 4 для семантического.")

    length = len([name for name in os.listdir(directory) if os.path.isfile(directory + "\\" + name)]) // 2 + 1
    if (starttest >= length or starttest <= 0):
        starttest = 1
    correctd = int(length)

    for i in range(starttest, length):
        testname = directory + "\\" + str(i) + ".txt"
        answname = directory + "\\code_answ\\" + str(i) + ".txt"
        chackname = directory + "\\" + str(i) + "(answer).txt"

        print(testname)
        fw = open(answname, 'w', encoding="utf-8")
        if testtype == '1':
            lexAnalizer = GetLex.GetLex(testname)
            try:
                lexem = lexAnalizer.getLex()
                while lexem.lex:
                    fw.write(lexem.output() + '\n')
                    lexem = lexAnalizer.nextLex()
            except Exception as e:
                fw.write(str(e))
        elif testtype == '2':
            parserper = Parse.Parser(testname)
            try:
                result = parserper.parseExpression()
                result.Print(fw, 0)
            except Exception as e:
                fw.write(str(e))
        elif testtype == '3':
            parserper = Parse.Parser(testname)
            result = parserper.parseProgramm()
            result.Print(fw, 0)
        elif testtype == '4':
            parserper = Semantic.Parser(testname)
            result = parserper.parseProgramm()
            result.Print(fw, 0)
        fw.close()

        # Вывод итога теста:
        with open(answname, "r", encoding="utf-8") as thisf, open(chackname, "r", encoding="utf-8") as correct:
            while True:
                ar = thisf.readline()
                cr = correct.readline()
                if ar.split() != cr.split():
                    print(False)
                    print("ошбика в выражении " + str(cr))
                    print(cr + ar)
                    correctd -= 1
                    break
                if ar == "":
                    print(True)
                    break

    print('\n')
    print(f'Верных тестов {str(correctd - 1)}/{str(length - 1)}')
