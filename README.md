# PythonComplex
A package for different operations on complex numbers.

## More details
- This package is essentially for mathematical operations on complex numbers.
- It is very easy and intuitif to use, as any mathematicain would expect.
- There is more to come on this class, like power of complex numbers.

## Installation

Use the package manager [pip](https://pypi.org/project/cmpx/) to install cmpx.

```bash
pip install cmpx
```

## Usage
### Importing Complex class
```python
from cmpx import Complex
```
### Different instanciations of Complex class
```python
# Instanciation 1
number = Complex() # --> Real = 0, Imaginary = 0
print(number)
# Instanctiation 2
number = Complex(42) # --> Real = 42, Imaginary = 0
print(number)
# Instanciation 3
number = Complex(12, -3.2) # --> Real = 12, Imaginary = -3.2
print(number)
# Instanciation 4
number = Complex(im=13.2, re=5) # --> Real = 5, Imaginary = 13.2
print(number)
# Instanciation 5
number = Complex(re=3, im=-2.4, restore=False) # restore argument is by default True, whenever an error occurs on operation, the last result will be restored to the object, else if it is False then the object will be simply None.
# Instanciation 6
number = Complex.fromComplex(4 - 3j - 2) # Real = 2, Imaginary = -3
# Keep in mind that the imaginary part 'j' must be always multiplied with a coefficient as follows
number = Complex.fromComplex(1 - 1j)
```
### Basic operations
```python
num1 = Complex(re=3, im=-2.5)
num2 = Complex(re=4.2, im=13.2)
# Summation
print('({}) + ({}) = {}'.format(num1, num2, num1 + num2))
# Substraction
print('({}) - ({}) = {}'.format(num1, num2, num1 - num2))
# Multiplication
print('({}) * ({}) = {}'.format(num1, num2, num1 * num2))
# Division
print('({}) / ({}) = {}'.format(num1, num2, num1 / num2))
# Floor division
print('({}) // ({}) = {}'.format(num1, num2, num1 // num2))
## Affecting the result directly on the number
# Summation
print('({}) += ({})'.format(num1, 2), end=' --> ')
num1 += 2
print(num1)
# Substraction
print('({}) -= ({})'.format(num1, num2), end=' --> ')
num1 -= num2
print(num1)
# Multiplication
print('({}) *= ({})'.format(num1, 2), end=' --> ')
num1 *= 2
print(num1)
# Division
print('({}) /= ({})'.format(num1, num2), end=' --> ')
num1 /= num2
print(num1)
# Floor division
print('({}) //= ({})'.format(num1, 2), end=' --> ')
num1 /= 2
print(num1)
# Congugated of a complex number
print('con({}) = {}'.format(num2, num2.con()))
# Module of a complex number
print('mod({}) = {}'.format(num2, num2.mod()))
# You can also make basic operations with non instanciated complex numbers like this
num1 *= (1 - 1j)
print(num1)
```
### Comparisons of Complex numbers
```python
num1 = Complex(im=3.1, re=-5)
num2 = Complex(im=-1.5, re=0.6)
# Greater than
if(num1 > num2): print('({}) > ({})'.format(num1, num2))
# Greater or equal
if(num1 >= num2): print('({}) >= ({})'.format(num1, num2))
# Less than
if(num1 < num2): print('({}) < ({})'.format(num1, num2))
# Less or equal
if(num1 <= num2): print('({}) <= ({})'.format(num1, num2))
# Equal
if(num1 == num2): print('({}) == ({})'.format(num1, num2))
# Not equal
if(num1 != num2): print('({}) != ({})'.format(num1, num2))
# You can also make comparisons with non instanciated complex numbers like this
if(num1 > (1 - 3j)): print('({}) != ({})'.format(num1, (1 - 3j)))
```
### Solving linear equation and second degree equation
#### Importing solve function
```python
from cmpx.equations import solve
```
#### Solving equations
```
solutions = solve(-1,2,3) # It will return a tuple of solutions
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
