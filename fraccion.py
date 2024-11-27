import math

class Fraccion:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        self.numerador = numerador
        self.denominador = denominador
        self.decimal = numerador / denominador

    def simplificar(self):
        mcd = math.gcd(self.numerador, self.denominador)
        self.numerador //= mcd
        self.denominador //= mcd

    def __str__(self):
        return f"{self.numerador}/{self.denominador} ≈ {self.decimal:.4f}"

    def __eq__(self, other):
        return self.numerador * other.denominador == self.denominador * other.numerador

    def __add__(self, other):
        nuevo_numerador = self.numerador * other.denominador + other.numerador * self.denominador
        nuevo_denominador = self.denominador * other.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

print(Fraccion(2,3))