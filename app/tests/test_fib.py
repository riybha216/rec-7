from app.fib import fibonacci

# Test cases for the fibonacci function
def test_first_fibonacci():
    assert fibonacci(1) == 1


def test_zero_fibonacci():
    try:
        fibonacci(0)
    except ValueError:
        return True
