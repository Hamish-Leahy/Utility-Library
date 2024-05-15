# Example usage of debug_util.py

import debug_util

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        debug_util.print_exception_info()
        return None

def main():
    debug_util.debug_print("Starting program...")
    result = divide(10, 0)
    debug_util.debug_assert(result is None, "Division by zero should return None")

if __name__ == "__main__":
    main()
