from functools import wraps


def log(filename=None):  # filename - имя файла для записи логов
    """Декоратор для логирования вызовов функции."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {e}. Inputs {args}, {kwargs}")

        return wrapper

    return decorator


@log("log_file")
def my_function(x, y):
    """Декорируемая функция"""
    return x + y


my_function(2, 0)
