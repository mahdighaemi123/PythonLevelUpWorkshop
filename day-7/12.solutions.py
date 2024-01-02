# solution 1
import time


def timer(func):

    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        execution_time = end_time - start_time
        print(
            f"Function '{func.__name__}' took {execution_time:.6f} seconds to execute.")

    return wrapper


@timer
def test_function():
    for i in range(1000):
        print(i)


test_function()
