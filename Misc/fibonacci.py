def naive_fibonacci(n: int) -> int:
    # Natural approach to recursive fibonacci function.
    if n <= 1:
        return n
    return naive_fibonacci(n - 1) + naive_fibonacci(n - 2)


def iterative_fibonacci(n: int) -> int:
    # Bottom-up iterative approach
    first = 0
    second = 1
    for _ in range(n):
        first, second = second, first + second
    return first


def better_fibonacci(n: int) -> int:
    # Does fibonacci with a single recursive call.
    # Makes time-complexity O(n)

    def _internal(n):
        if n <= 1:
            return (n, 0)
        (a, b) = _internal(n - 1)
        return (a + b, a)

    return _internal(n)[0]


def memoized_fibonacci(n: int) -> int:
    # simple memoization of naive fibonacci implementation
    memo = {0: 0, 1: 1}
    def _internal(n):
        if n not in memo:
            memo[n] = memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)

    _internal(n)
    return memo[n]


def better_fibonacci_memoized(n: int) -> int:
    # simple memoization of improved recursive fibonacci
    memo = {0: 0, 1: 1}

    def _internal(n: int):
        if n in memo:
            return memo[n], memo[n - 1]
        else:
            memo[n], memo[n - 1] = _internal(n - 1)
            return (memo[n] + memo[n - 1], memo[n])

    return _internal(n)[0]


def Memoize(function):
    memo = {}

    def _wrapper(param):
        if param not in memo:
            memo[param] = function(param)
        return memo[param]

    return _wrapper


decorated_fib = Memoize(naive_fibonacci)

