def function_with_uncommon_error(a, b):
    if a == 0:
        return 1 / a  # ZeroDivisionError
    elif b < 0:
        return a ** b  # Negative power error for non-integer a
    else:
        return a + b