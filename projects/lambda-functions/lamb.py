# Lambda functions are anonymous, which means not bound to an identifier
# But, in Python, they can be ...

class Lamb:

    def __init__(self):
        pass

    double = lambda x: x + x

    def double_regular_function(self, x):
        return x + x

    def double_lambda_function(self, x):
        double = lambda s: s + s
        return double(x)


if __name__ == '__main__':
    lamb = Lamb()
    
