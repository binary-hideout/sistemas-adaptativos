class Membresias():
    """Contiene las funciones de membresía como métodos estáticos.
    """
    @staticmethod
    def triangular(x, a, b, c):
        """Fusifica 'x' en una función triangular.
        """
        if x > a and x <= b:
            return (x - a) / (b - a)
        elif x > b and x < c:
            return (c - x) / (c - b)
        else:
            return 0

    @staticmethod
    def trapezoidal(x, a, b, c, d):
        """Fusifica 'x' en una función trapezoidal completa.
        """
        if x >= a and x <= b:
            return (x - a) / (b - a)
        elif x >= b and x <= c:
            return 1
        elif x >= c and x <= d:
            return (d - x) / (d - c)
        else:
            return 0

    @staticmethod
    def trapezoidalR(x, c, d):
        """Fusifica 'x' en una función trapezoidal-R.
        """
        if x > d:
            return 0
        elif x >= c and x <= d:
            return (d - x) / (d - c)
        elif x < c:
            return 1

    @staticmethod
    def trapezoidalL(x, a, b):
        """Fusifica 'x' en una función trapezoidal-L.
        """
        if x < a:
            return 0
        elif x >= a and x <= b:
            return (x - a) / (b - a)
        elif x > b:
            return 1