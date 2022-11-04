import GetLex
import os.path

# -*- coding: utf-8 -*-

if __name__ == '__main__':
    directory = 'lexer_tests'

    # запуск и тестирование синтаксического анализатора:
    length = len([name for name in os.listdir(directory) if os.path.isfile(directory + "\\" + name)]) // 2 + 1
    for i in range(1, length):
        test_name = directory + "\\" + str(i) + ".txt"
        answer_name = directory + "\\code_answ\\" + str(i) + ".txt"
        check_name = directory + "\\" + str(i) + "(answer).txt"
        print(test_name)
        fw = open(answer_name, 'w', encoding="utf-8")
        lexeme_Analyzer = GetLex.GetLex(test_name)
        try:
            lexeme = lexeme_Analyzer.getLex()
            while lexeme.lex:
                fw.write(lexeme.output() + '\n')
                lexeme = lexeme_Analyzer.nextLex()
        except Exception as e:
            fw.write(str(e))
        fw.close()

        # Вывод итога теста:
        with open(answer_name, "r", encoding="utf-8") as current_file, open(check_name, "r",
                                                                            encoding="utf-8") as correct_file:
            while True:
                ar = current_file.readline()
                cr = correct_file.readline()
                if ar.split() != cr.split():
                    print(False)
                    print("Ошибка в выражении " + str(cr))
                    print('Ожидалось: ' + f'{cr}')
                    print('Получено: ' + f'{ar}' + '\n')
                    break
                if ar == "":
                    print(f'{True}' + '\n')
                    break
