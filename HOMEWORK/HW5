1.有限體是一個包含有限個元素的集合，且在該集合內定義了加法、減法、乘法和除法，其運算結果仍屬於該集合內，並滿足以封閉性、結合律、交換律、單位元、反元素、分配律。
2、3.class FiniteFieldElement:
    def __init__(self, value, p):
        self.value = value % p
        self.p = p

    def __add__(self, other):
        return FiniteFieldElement((self.value + other.value) % self.p, self.p)

    def __mul__(self, other):
        return FiniteFieldElement((self.value * other.value) % self.p, self.p)

    def __eq__(self, other):
        return self.value == other.value and self.p == other.p
4.def check_distributivity(a, b, c):
    left = a * (b + c)
    right = (a * b) + (a * c)
    return left == right
5、6.class Fp:
    def __init__(self, value, p):
        self.value = value % p
        self.p = p

    def __add__(self, other): return Fp(self.value + other.value, self.p)
    def __sub__(self, other): return Fp(self.value - other.value, self.p)
    def __mul__(self, other): return Fp(self.value * other.value, self.p)
    
    def __pow__(self, exponent):
        return Fp(pow(self.value, exponent, self.p), self.p)

    def __truediv__(self, other):
        if other.value == 0: raise ZeroDivisionError
        # 使用費馬小定理求乘法反元素
        inv = other ** (self.p - 2)
        return self * inv

    def __repr__(self):
        return f"{self.value} (mod {self.p})"
7.有限體保證了在一個有限的數字範圍內，我們依然可以像處理實數一樣進行四則運算，而不會出現小數或無窮大。
