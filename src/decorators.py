def log(filename):
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


# @log(filename="log.txt")
# def my_function(x, y):
#     return x + y
#
# my_function(20, "hello")
