def limiter(max_calls):
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_calls = getattr(func, "calls", 0)
            if current_calls >= max_calls:
                raise Exception("to many calls")
            setattr(func, "calls", current_calls + 1)
            return func(*args, **kwargs)
        return wrapper
    return decorator

def test_snake_case(func):
    def wrapper(*args, **kwargs):
        if not func.__name__.islower():
            raise Exception("is not snake case")
        return func(*args, **kwargs)
    return wrapper
