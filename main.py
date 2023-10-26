from pymemcache.client.base import Client

client = Client(('localhost', 11211))

def cache(func):

    def wrapper(n):
        key = f'{func.__name__}_{n}'

        result = client.get(key)
        if result is not None:
            return int(result)

        result = func(n)
        client.set(key, result)

        return result
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(100))