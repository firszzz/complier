import GetLex

if __name__ == '__main__':
    for i in range(1, 12):
        testName = "tests\\" + str(i) + ".txt"
        answerName = "tests\\code_answ\\" + str(i) + ".txt"
        print('\n' + testName + '\n')
        fw = open(answerName, 'w')
        lexAnalyzer = GetLex.GetLex(testName)
        lexeme = lexAnalyzer.getLex()
        while lexeme:
            print(lexeme.output())
            fw.write(lexeme.output() + '\n')
            if lexeme.error:
                break
            lexeme = lexAnalyzer.getLex()
