# Лабораторная работа №1 по дисциплине "Логические основы интеллектуальных систем"
# выполнена студентом группы 021703 БГУИР Рабушка Алеся Александровна
# Файл с описанием модуля парсера сокращённого языка логики высказываний
# 06.03.2023




def is_correct_formula(formula: str) -> bool:
    """
    Проверяет наличие недопустимых символов
    """
    latin_alphabet = 'abcdeffghijklmnopqrstuvwxxyz'
    if len(formula) == 1:
        if formula in latin_alphabet.upper() or formula in '01':
            return True
        else:
            return False
    else:
        flag = False
        for symbol in formula:
            if symbol in '{}_=<@#$%^&*.,?|+23456789':
                return False
            if symbol in latin_alphabet:
                return False

        return True



def symbol_is_not_alone_in_brackets(formula: str) -> bool:
    """
    Проевряет, что атомарная формула указана без скобок
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for symbol_index in range(0, len(formula)):
        if formula[symbol_index] == '(' and is_correct_formula(formula[symbol_index + 1]) and formula[symbol_index + 2] == ')':
            return False
        elif formula[symbol_index] in alphabet.upper() and formula[symbol_index+1] in alphabet.upper():
            return False

    return True


def is_correct_operator(formula:str)->bool:
    """
    Проверяет, верно ли введены все бинарные операторы
    """
    new_formula = formula.replace('\/', 'v').replace('/\\', '^')
    for index in range(len(formula)):
        if formula[index] == '!':
            if formula[index - 1] != '(':
                return False
    if len(formula) == 1:
        return True
    elif '\\' in new_formula or '/' in new_formula:
        return False
    else:
        return True



def brackets_count(formula:str) -> bool:
    """
    Проверяет, что количество открывающихся круглых скобок равно количеству закрывающихся
    """
    left_bracket_count = 0
    right_bracket_count = 0
    i = 0
    for i in formula:
        if i == '(':
            left_bracket_count += 1
        elif i == ')':
            right_bracket_count += 1;

    if left_bracket_count == 0 and right_bracket_count == 0 and len(formula) == 1:
        return True
    elif left_bracket_count == 0 and right_bracket_count == 0 and len(formula) != 1:
        return False
    elif left_bracket_count == right_bracket_count:
        return True
    else:
        return False





def build_truth_table(formula:str, vars:list)->list:
    """
    Построение таблицы истинности
    """
    truth_table = []
    for index in range(2 ** len(vars)):
        binary_number = bin(index)[2::]
        # print(binary_number)
        if len(binary_number) != len(vars):
            truth_table_row = '0'*(len(vars)-len(binary_number))+binary_number

            truth_table.append(truth_table_row)
            # print(truth_table_row)
        else:
            truth_table.append(binary_number)

    truth_table_result = []

    for truth_table_row in truth_table:
        buf_formula = formula
        for symbol in formula:
            if symbol in vars:
                buf_formula = buf_formula.replace(symbol, truth_table_row[vars.index(symbol)])

        # print(buf_formula)
        try:
            truth_table_result.append(eval(buf_formula))
        except:
            print('Неверный формат формулы')
            raise SystemExit
    # print(truth_table_result)
    return truth_table, truth_table_result



def modify_formula(formula:str)->str:
    """
    Преобразует формулу в вид, необходимый для произведения вычислений
    """
    new_formula = ''
    vars = []
    for symbol in formula:
        if symbol not in 'v^>~!()':
            if symbol not in vars:
                vars.append(symbol)
            new_formula += symbol
        elif symbol == '(' or symbol == ')':
            new_formula += symbol
        elif symbol == '!':
            new_formula += ' not '
        elif symbol == '^':
            new_formula += ' and '
        elif symbol == 'v':
            new_formula += ' or '
        elif symbol == '~':
            new_formula += ' == '
        elif symbol == '>':
            new_formula += ' <= '

    return new_formula, vars

def alphabet_symbols_count(formula:str)->int:
    """
    Метод считает количество символов, принадлежащих алфавиту
    :param formula:
    :return:
    """
    alphabet = 'abcdeffghijklmnopqrstuvwxxyz01'
    count = 0
    for symbol in formula:
        if symbol in alphabet.upper():
            count += 1
    return count


def build_pdnf(formula:str):
    """
    Построение СДНФ в соответствии с таблицей истиности
    :param formula:
    :return:
    """
    formula, vars = modify_formula(formula)
    truth_table, truth_table_result = build_truth_table(formula, vars)

    pdnf_formula = ''
    if alphabet_symbols_count(formula) != 1:
        pdnf_formula += '('
    pdnf_formulas_list = []
    truth_table_pdnf = []

    for index in range(len(truth_table_result)):
        if truth_table_result[index] == 1:
            truth_table_pdnf.append(truth_table[index])
    # print(truth_table)
    # print(truth_table_pdnf)

    for expression in truth_table_pdnf:
        pdnf_formula_expression = []
        for value_index in range(len(expression)):
            if expression[value_index] == '0':
                pdnf_formula_expression.append(f'(!{vars[value_index]})')
            else:
                pdnf_formula_expression.append(f'{vars[value_index]}')

        pdnf_formulas_list.append(pdnf_formula_expression)
        # print(pdnf_formula_expression)
    # print(pdnf_formulas_list)

    for expression in pdnf_formulas_list:
        if pdnf_formulas_list.index(expression) == len(pdnf_formulas_list)-1:
            if len(expression) == 1:
                pdnf_formula += f'{expression[0]}'
            else:
                for value in expression:
                    if expression.index(value) == len(expression)-1:
                        pdnf_formula += f'{value})'
                    else:
                        pdnf_formula += f'({value}/\\'
        else:
            for value in expression:
                if expression.index(value) == len(expression)-1:
                    pdnf_formula += f'{value})\/'
                else:
                    pdnf_formula += f'({value}/\\'

    if not brackets_count(pdnf_formula):
        pdnf_formula += ')'

    return pdnf_formula





def is_logical_formula(formula: str)->bool:
    """
    Проверяет, правильно ли введена формула
    """
    if is_correct_formula(formula) and brackets_count(formula) and is_correct_operator(formula) and ' ' not in formula:
        if len(formula) != 1:
            if symbol_is_not_alone_in_brackets(formula):
                formula = formula.replace('\/', 'v').replace('/\\', '^').replace('->', '>')
                # print(formula)
                pdnf = build_pdnf(formula)
                return pdnf
        else:
            formula = formula.replace('\/', 'v').replace('/\\', '^').replace('->', '>')
            # print(formula)
            pdnf = build_pdnf(formula)
            return pdnf

    else:
        print('Ошибка ввода формулы\n')



def compare(sdnf, formula):
    """
    Сравнивает полученную формулу СДНФ и введенную пользователем формулу
    """
    sdnf = sdnf.replace('(', '').replace(')', '').replace('/\\', '^').replace('\/', 'v')
    sdnf_expressions = sdnf.split('v')
    sdnf_symbols = []
    for expression in sdnf_expressions:
        sdnf_symbols.append(expression.split('^'))
    # print(sdnf_symbols)

    formula = formula.replace('(','').replace(')','').replace('/\\','^').replace('\/', 'v')
    formula_expressions = formula.split('v')
    formula_symbols = []
    for expression in formula_expressions:
        formula_symbols.append(expression.split('^'))
    # print(formula_symbols)

    if len(formula_symbols) != len(sdnf_symbols):
        return 'Формула не является СДНФ'
    # [item in b for item in a]
    compare_list = []
    for item1 in sdnf_symbols:
        for item2 in formula_symbols:
            if set(item1) == set(item2):
                compare_list.append(True)

    # for sdnf_pare in sdnf_symbols:
    #     for formula_pare in formula_symbols:
    #         if sdnf_pare[0] in formula_pare and sdnf_pare[1] in formula_pare:
    #             compare_list.append(True)

    # print(compare_list)

    if False in compare_list or len(compare_list) == 0:
        return 'Формула не является СДНФ'
    else:
        return 'Формула является СДНФ'





#(((!P)/\Q)\/(P/\(!Q))\/(Q/\P))
#(((!P)/\Q)\/(P/\(!Q))\/((!Q)/\(!P)))
if __name__ == '__main__':
    formula = input('Введите СДНФ формулу:    ')
    # print(is_logical_formula(formula))
    try:
        sdnf = is_logical_formula(formula)
        if sdnf:
            print('Полученная СДНФ формула:', sdnf)
            print(compare(sdnf, formula))
    except:
        print('Возникла ошибка')
        raise SystemExit
