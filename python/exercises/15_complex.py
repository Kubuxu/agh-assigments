import IPython
import math

class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def real(self):
        return self.x
    def imag(self):
        return self.y

    def __str__(self):
        return f"{self.x}+{self.y}i"
    def __repr__(self):
        return f"Complex(x={self.x}, y={self.y})"
    def _repr_pretty_(self, p, cycle):
       p.text(str(self) if not cycle else '...')

    def __add__(self, val):
        if isinstance(val, Complex):
            return Complex(self.x + val.x, self.y + val.y)
        else:
            return Complex(self.x + val, self.y)
    def __radd__(self, val):
        return self.__add__(val)
    
    def __sub__(self, val):
        if isinstance(val, Complex):
            return Complex(self.x - val.x, self.y - val.y)
        else:
            return Complex(self.x - val, self.y)
    def __rsub__(self, val):
        if isinstance(val, Complex):
            return Complex(-self.x + val.x, - self.y + val.y)
        else:
            return Complex(-self.x + val, -self.y)

    def __mul__(self, val):
        if isinstance(val, Complex):
            return Complex(self.x*val.x - self.y*val.y, self.x*val.y + self.y*val.x)
        else:
            return Complex(val * self.x, val* self.y)
    def __rmul__(self, val):
        return self.__mul__(val)

    def reciprocal(self):
        x = self.x
        y = self.y
        deno = x*x+y*y
        return Complex(x/deno, y/deno)

    def __truediv__(self, val):
        if isinstance(val, Complex):
            return self.reciprocal() * val
        else:
            return Complex(self.x / val, self.y / val)
    def __rtruediv__(self, val):
        if isinstance(val, Complex):
            return val.__truediv__(self)
        else:
            return val * self.reciprocal()

    def abs(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def phase(self):
        return math.atan2(self.x, self.y)




i = Complex(0, 1)
print("You can use '1*i' for complex numbers")
IPython.embed()

