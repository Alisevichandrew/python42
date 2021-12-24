def decorator_func(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        print('start')
        import pdb; pdb.set_trace()
        if args[0].isdigit():
            raise ValueError('Name must be string')
        func(*args, **kwargs)
        print('end')
        end = time.time()
        print(f'Time of work {end - start}')
    return wrapper

@decorator_func
def hello(name):
    print(f'hello, {name}')
hello('123')
