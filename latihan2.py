def hitung(angka1, operator, angka2):
    if operator == '+':
        return angka1 + angka2
    elif operator == '-':
        return angka1 - angka2
    elif operator == '*':
        return angka1 * angka2
    elif operator == '/':
        return angka1 / angka2
    else:
        return "Operator yang dimasukkan salah!"