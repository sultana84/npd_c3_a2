def hello_universe(f):
    def decorated(*args, **kwargs):
        print('Hello Universe!')
    return decorated

def __call__(self, *args, **kwargs):
    print ('Hello Universe %s!' % self.f.f_name)
    _ret = self.f(*args, **kwargs)
    return _ret

@hello_universe
def multiply(arg1, arg2):
    print('Multiplying %r and %r: %r!'%(arg1, arg2, arg1*arg2))
    return arg1*arg2

@hello_universe
def subtract(arg1, arg2):
    print('Subtracting %r and %r: %r!'%(arg1, arg2, arg1-arg2))
    return arg1-arg2
