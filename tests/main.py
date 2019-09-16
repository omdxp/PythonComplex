from cmpx import Complex
from cmpx.equations import solve

def main():
    a = Complex(1, 4, False)
    a /= 0
    print(a)

if __name__ == '__main__': main()