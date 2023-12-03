# Task 2.1


# 1. Cобственный декоратор
def timing_decorator(func):
    import time

    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"Функция {func.__name__} отработала за {end - start} секунд")
        return result

    return wrapper


@timing_decorator
def meow():
    print("meow")


meow()


#######################
# 2. Напиши декоратор, где функция принимает параметры.


def cat_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<meow>{result}</meow>"

    return wrapper


@cat_decorator
def say_something(some_string: str):
    return some_string


print(say_something("""I'm a cat!"""))


#######################
# 3.Улучши и сделай, так, чтоб сам декоратор принимал параметры.


def upgraded_cat_decorator(meows=10):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(meows):
                print("meow!")
            print(f"<meow>{func(*args, **kwargs)}</meow>")
            return f"The function said meow {meows} times"

        return wrapper

    return actual_decorator


@upgraded_cat_decorator(3)
def say_something(some_string: str):
    return some_string


print(say_something("""I'm a cat!"""))
