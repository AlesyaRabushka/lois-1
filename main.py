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
def is_atomic_formula(formula):
    latin_alphabet = 'abcdeffghijklmnopqrstuvwxxyz'
    if formula in latin_alphabet.upper():
        return True
    else:
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
    print(is_logical_formula(formula))
    print(is_atomic_formula(formula))