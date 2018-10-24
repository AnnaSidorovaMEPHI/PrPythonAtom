def cache_decorator(f):
    mem_cache = {}
    
    def cached_fucntion(arg):
        if arg in mem_cache:
            print('I used cache!')
            return mem_cache[arg]
        else:
            print('i dont use cache!')
            mem_cache[arg] = f(arg)
            return mem_cache[arg]
    
    return cached_fucntion
@cache_decorator
def fib(n):
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: return fib(n-1)+fib(n-2)