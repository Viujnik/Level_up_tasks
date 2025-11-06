from collections import deque


def memoize(limit_size=64):
    def decorator(func):
        cache = {}
        usage_order = deque()

        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in cache:
                usage_order.remove(key)
                usage_order.append(key)
                return cache[key]
            result = func(*args, **kwargs)
            cache[key] = result
            usage_order.append(key)
            if len(cache) > limit_size:
                oldest = usage_order.popleft()
                del cache[oldest]
            return result

        return wrapper

    return decorator


@memoize(3)
def expensive_function(n):
    print(f"We need a grab: {n}")
    return 2 ** n


print(expensive_function(10))
print(expensive_function(20))
print(expensive_function(10))
print(expensive_function(30))
print(expensive_function(40))
print(expensive_function(10))
print(expensive_function(50))
print(expensive_function(60))
print(expensive_function(30))
