def log(filename):
    """Декоратор автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки. Принимает на вход файл для записи логов.
    На выходе записывает логи либо в файл, либо в консоль."""

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                rezult = func(*args, **kwargs)

            except Exception as error:
                try:
                    file = open(filename, "a")
                except FileNotFoundError:
                    print(f"{func.__name__} error: {error}. Inputs: {args}, {kwargs}\n")
                else:
                    file.write(f"{func.__name__} error: {error}. Inputs: {args}, {kwargs}\n")
                    file.close()
                raise Exception(f"Error: {error}")

            else:
                try:
                    file = open(filename, "a")
                except FileNotFoundError:
                    print(f"{func.__name__} ok\n")
                else:
                    file.write(f"{func.__name__} ok\n")
                    file.close()
                return rezult

        return wrapper

    return decorator
