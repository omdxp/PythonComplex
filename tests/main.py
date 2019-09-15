from cmpx import Complex

def main():
    a = 4 + 3 - 5j
    print(a.real)
    print(a.imag)
    cmplx = Complex(a, 1)
    print(cmplx)

if __name__ == '__main__': main()