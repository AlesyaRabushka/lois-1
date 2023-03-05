# Лабораторная работа №1 по дисциплине "Логические основы интеллектуальных систем"
# выполнена студентом группы 021703 БГУИР Рабушка Алеся Александровна
#
#



# 0 или 1
def is_logical_const(formula):
    if formula == '0' or formula == '1':
        return True
    return False




# латинская заглавная
def is_correct_formula(formula: str) -> bool:
    """
    Проверяет наличие недопустимых символов
    """
    if len(formula) == 1:
        latin_alphabet = 'abcdeffghijklmnopqrstuvwxxyz'
        if formula in latin_alphabet.upper():
            return True
        else:
            return False
    else:
        for symbol in formula:
            if symbol in '{}_=<@#$%^&*.,?|+':
                return False
        return True



def symbol_is_not_alone_in_brackets(formula: str) -> bool:
    """
    Проевряет, что атомарная формула указана без скобок
    """
    for symbol_index in range(0, len(formula)):
        if formula[symbol_index] == '(' and is_correct_formula(formula[symbol_index + 1]) and formula[symbol_index + 2] == ')':
            return False
    return True

def is_correct_operator(formula:str)->bool:
    """
    Проверяет, верно ли ввелены все бинарные операторы
    """
    if is_correct_formula(formula):
        print('here')
        return True
    else:
        new_formula = formula.replace('\/', 'v').replace('/\\', '^')
        if '\\' in new_formula or '/' in new_formula:
            return False
        else:
            return True



# ( ! formula )
def is_unary_complex_formula(formula: str) -> bool:
    """
    Проверяет, что формула является унарной сложной формулой
    """
    if formula[0] == '(' and formula[len(formula)-1] == ')' and formula[1] == '!':
        if is_formula(formula[2:len(formula)-1]):
            return True
    else:
        return False

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
    if left_bracket_count == right_bracket_count:
        return True
    else:
        return False



def is_binary_complex_formula(formula):
    left_brackets_count, right_brackets_count = brackets_count(formula)
    if left_brackets_count == right_brackets_count:
        if formula[0] == '(' and formula[len(formula)-1] == ')':
            count(formula)
            if is_binary_complex_formula(formula[1:len(formula)-1]):
                pass
            else:
                for index in range(1, len(formula)-1):
                    if formula[index] == '\\' and formula[index + 1] == '/':
                        first_formula = formula[1:index]
                        if is_binary_complex_formula(first_formula):
                            print('it is binary complex')
                        else:
                            print('it is not binary complex')
                        second_formula = formula[index + 2:len(formula)-1]
                        # print(first_formula, second_formula)
                    elif formula[index] == '/' and formula[index + 1] == '\\':
                        print('/\ ')
                    elif formula[index] == '-' and formula[index + 1] == '>':
                        print('->')
                    elif formula[index] == '~':
                        print('~')
        else:
            return False
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
        truth_table_result.append(eval(buf_formula))
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



def build_pdnf(formula:str):
    formula, vars = modify_formula(formula)
    truth_table, truth_table_result = build_truth_table(formula, vars)
    pdnf_formula = '('
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
        print(pdnf_formula_expression)
    # print(pdnf_formulas_list)

    for expression in pdnf_formulas_list:
        if pdnf_formulas_list.index(expression) == len(pdnf_formulas_list)-1:
            for value in expression:
                if expression.index(value) == len(expression)-1:
                    pdnf_formula += f'{value}))'
                else:
                    pdnf_formula += f'({value}/\\'
        else:
            for value in expression:
                if expression.index(value) == len(expression)-1:
                    pdnf_formula += f'{value})\/'
                else:
                    pdnf_formula += f'({value}/\\'

    return pdnf_formula





def is_logical_formula(formula: str)->bool:
    """
    Проверяет, правильно ли введена формула
    """
    if is_correct_formula(formula) and brackets_count(formula) and is_correct_operator(formula) and ' ' not in formula and symbol_is_not_alone_in_brackets(formula):
        print('Формула введена верно')
        formula = formula.replace('\/', 'v').replace('/\\', '^').replace('->', '>')
        print(formula)
        print(build_pdnf(formula))
        raise SystemExit
    else:
        print('Ошибка ввода формулы\n')








if __name__ == '__main__':
    while True:
        formula = input('Введите формулу: ')
        # print(is_logical_formula(formula))
        is_logical_formula(formula)