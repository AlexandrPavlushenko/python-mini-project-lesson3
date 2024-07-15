def log(filename=None):  # filename - имя файла для записи логов
    """Декоратор для логирования вызовов функции."""

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write("my_function ok")
                else:
                    print("my_function ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(f"my_function error: {e}. Inputs: {args}, {kwargs}")
                else:
                    print(f"my_function error: {e}. Inputs {args}, {kwargs}")
                raise

        return wrapper

    return decorator


@log()
def my_function(x, y):
    return x + y


my_function(1, 2)
