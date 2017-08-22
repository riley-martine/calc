from inspect import getsource

def get_source(f):
    return getsource(f).strip()



if __name__ == '__main__':
    f = lambda x: x**2
    print(get_source(f))
