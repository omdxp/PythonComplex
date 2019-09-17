from cmpx import Complex
from cmpx.equations import solve

def main():
    arr = []
    for i in range(10):
        arr.append(Complex(i, 2*i))
    
    print(arr)

if __name__ == '__main__': main()