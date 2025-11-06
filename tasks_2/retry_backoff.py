import time
from functools import wraps


def retry_backoff(retries, base_delay):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == retries - 1:
                        print(f'It was last try - {attempt + 1}/{retries}')
                        raise e
                    backoff = base_delay * (2 ** attempt)
                    print(f'Retry {attempt + 1} was failed. Backing off {backoff} seconds...')
                    time.sleep(backoff)
            return None

        return wrapper

    return decorator


def unreliable_operation():
    if not hasattr(unreliable_operation, "calls"):
        unreliable_operation.calls = 0

    unreliable_operation.calls += 1

    if unreliable_operation.calls <= 3:
        print(f" -> Call's retry {unreliable_operation.calls}: failed.")
        raise IOError("Network Error")
    else:
        print(f" -> Call's retry {unreliable_operation.calls}: success.!")
        return "Data received."


@retry_backoff(retries=5, base_delay=1)
def make_api_call():
    return unreliable_operation()


try:
    result = make_api_call()
    print(f"Result: {result}")
except Exception as e:
    print(f"Critical error after all attempts: {e}")
