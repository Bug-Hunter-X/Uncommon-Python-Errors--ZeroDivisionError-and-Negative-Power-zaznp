def function_with_error_handling(a, b):
    try:
        if a == 0:
            return float('inf')  # Handle division by zero
        elif b < 0:
            if isinstance(a, int) or a > 0:
                return a ** b
            else:
                return 1/ a**abs(b) #Handle negative power with non integer
        else:
            return a + b
    except TypeError:
        return "Invalid input types"
    except Exception as e:
        return f"An error occurred: {e}"