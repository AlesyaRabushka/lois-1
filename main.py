# Лабораторная работа №1 по дисциплине "Логические основы интеллектуальных систем"
# выполнена студентом группы 021703 БГУИР Рабушка Алеся Александровна
#
#



# 0 или 1
def is_logical_const(formula):
    if formula == '0' or formula == '1':
        return True
    return False


def is_number(formula):
    numbers = '1234567890'
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUYWXVZ'
    for index in formula:
        if index in numbers and index not in alphabet:
            return False
    return True

# латинская заглавная
def is_atomic_formula(formula: str) -> bool:
    latin_alphabet = 'abcdeffghijklmnopqrstuvwxxyz'
    if formula in latin_alphabet.upper():
        return True
    else:
        return False

def symbol_is_not_alone_in_brackets(formula: str) -> bool:
    """

    """
    for symbol_index in range(0, len(formula)):
        if formula[symbol_index] == '(' and is_atomic_formula(formula[symbol_index + 1]) and formula[symbol_index + 2] == ')':
            return False
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
    Проверяет, что количество открывающих круглых скобок равно количеству закрывающих
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
                        print(first_formula, second_formula)
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


# unary complex | binary complex
def is_complex_formula(formula):
    if is_unary_complex_formula(formula):
        return True
    elif is_binary_complex_formula(formula):
        return True
    else:
        return False


def is_formula(formula):
    if is_logical_const(formula):
        return True
    elif is_atomic_formula(formula):
        return True
    elif is_complex_formula(formula):
        return True
    else:
        return False


def is_correct_formula_input(formula: str)->bool:
    """
    Проверяет, правильно ли введена формула
    """
    if brackets_count(formula) and not is_number(formula) and is_atomic_formula(formula) and ' ' not in formula and symbol_is_not_alone_in_brackets(formula):
        print('Формула введена верно')
        return True
    else:
        print('Ошибка ввода формулы')
        return False


def is_logical_formula(formula):
    if is_atomic_formula(formula):
        return True
    elif is_logical_const(formula):
        return True
    elif is_number(formula):
        return False





if __name__ == '__main__':
    formula = input('Введите формулу: ')
    # print(is_logical_formula(formula))
    is_correct_formula_input(formula)