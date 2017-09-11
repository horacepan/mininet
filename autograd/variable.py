import math

class Variable:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return Add(self, other)

    def __radd__(self, other):
        return Add(self, other)

    def __sub__(self, other):
        return Sub(self, other)

    def __rsub__(self, other):
        return Sub(self, other)

    def __mul__(self, other):
        return Mult(self, other)

    def __rmul__(self, other):
        return Mult(self, other)

    def derivative(self):
        return 1

    def evaluate(self, var_dict):
        # Base variable is just the input value
        if self.name in var_dict:
            return var_dict[self.name]
        else:
            raise ValueError

    def forward(self, **kwargs):
        return self.evaluate(kwargs)

    def __repr__(self):
        return self.name

class Constant(Variable):
    def __init__(self, value):
        self.val = value

    def __repr__(self):
        return "Constant({})".format(self.val)

    def evaluate(self, var_dict):
        return self.val

    def derivative(self):
        return 0

    def backward(self):
        return 0

class Add(Variable):
    def __init__(self, larg, rarg):
        if isinstance(larg, (float, int, long)):
            larg = Constant(larg)
        if isinstance(rarg, (float, int, long)):
            rarg = Constant(rarg)
        self.larg = larg
        self.rarg = rarg

    def evaluate(self, var_dict):
        return self.larg.evaluate(var_dict) + self.rarg.evaluate(var_dict)

    def backward(self):
        return self.larg.backward() + self.rarg.backward

    def __repr__(self):
        return "({} + {})".format(self.larg, self.rarg)

class Sub(Variable):
    def __init__(self, larg, rarg):
        if isinstance(larg, (float, int, long)):
            larg = Constant(larg)
        if isinstance(rarg, (float, int, long)):
            rarg = Constant(rarg)

        self.larg = larg
        self.rarg = rarg

    def evaluate(self, var_dict):
        return self.larg.evaluate(var_dict) - self.rarg.evaluate(var_dict)

    def backward(self):
        return self.larg.backward() + self.rarg.backward

    def __repr__(self):
        return "({} + {})".format(self.larg, self.rarg)

class Mult(Variable):
    def __ini__(self, loperand, roperand):
        if isinstance(larg, (float, int, long)):
            larg = Constant(larg)
        if isinstance(rarg, (float, int, long)):
            rarg = Constant(rarg)

        self.larg = larg
        self.rarg = rarg

    def evaluate(self, var_dict):
        return self.larg.evaluate(var_dict) * self.rarg.evaluate(var_dict)

    def backward(self):
        return self.larg.backward() * self.rarg + \
               self.larg * self.rarg.backward

    def __repr__(self):
        return "({} * {})".format(self.larg, self.rarg)

class Sin(Variable):
    def __init__(self, arg):
        if isinstance(arg, (float, int, long)):
            val = Constant(arg)

        self.arg = arg

    def evaluate(self, var_dict):
        return math.sin(self.arg.evaluate(var_dict))

    def backward(self):
        return Cos(val) * val.backward()

    def __repr__(self):
        return "Sin({})".format(self.arg.__repr__())

class Cos(Variable):
    def __init__(self, arg):
        self.arg = arg

    def evaluate(self, var_dict):
        return math.cos(self.arg.evaluate(var_dict))

    def backward(self):
        return Sin(val) * val.backward()

    def __repr__(self):
        return "Cos({})".format(self.arg.__repr__())


def main():
    x = Variable('x')
    expr = Sin(x) + x + 5
    print expr
    print expr.evaluate({'x':math.pi})

if __name__ == '__main__':
    main()
