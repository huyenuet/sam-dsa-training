from functools import wraps
from time import time


def timeit(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start_time = time()

        try:
            result = f(*args, **kwargs)
        except:
            result = False

        end_time = time()

        print(f"Elapsed time: {round(end_time - start_time, 3)}")

        return result

    return wrapper


@timeit
def compute_sum(x):
    raise ValueError()
    sum = 0
    for i in range(x):
        sum += i
    return sum


x = compute_sum(1000)
print(x)
x = compute_sum(100000)
print(x)

