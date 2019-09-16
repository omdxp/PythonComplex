from cmpx import Complex
from cmpx.equations import solve

def main():
    arr = []
    for i in range(10):
        print(i)
        arr.append(Complex(i, 2*i))
    
    for i in range(1,10):
        print(arr[i])
    
    a = Complex()
    print(a)

if __name__ == '__main__': main()