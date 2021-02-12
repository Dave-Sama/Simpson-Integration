import sympy as sy
from texttable import Texttable

talbe = Texttable()

x = sy.symbols("x")
from math import pi, sqrt, ceil

class Simpson:

    def __init__(self):
        self.epsilon = self.CreateEpsilon()
        self.function = self.CreateFunction()
        self.boundary = self.CreateBoundary()
        self.derivative = self.Derivative(self.function)
        self.doubleDerivative = self.Derivative(self.derivative)
        self.max = self.MaximumValue()
        self.example = self.doubleDerivative.subs(x, self.function.subs(x, self.max))

        print(f'max: {self.max}')

        self.n = self.FindSlices()
        if self.n % 2 == 1:
            self.n -= 1

    def CreateFunction(self):  ## step 1 - choose a polynom
        ##fast example   x**4+x**3-3*x**2
        funcInput = '(sin(x**2+5*x+6))/(2*E**-x)'
        func = sy.sympify(funcInput)
        return func


    def CreateEpsilon(self):  ## step 3 - choose an epsilon
        return 0.00001


    def CreateBoundary(self):  ## step 2 - choose an a and b
        # a = 0
        # b = 0
        # while a >= b:
        #     print("\nA Note: A < B")
        #     a = sy.sympify(input('please choose boundary A: '))
        #     b = sy.sympify(input('please choose boundary B: '))
        return [0, 1]

    def MaximumValue(self):
        max = -2000
        step = self.boundary[0]
        while step <= self.boundary[1]:
            if max < self.function.subs(x, step):
                max = self.function.subs(x, step)
            step += 0.001
        return max

    def Derivative(self,func):
        return sy.diff(func, x)

    def SimpsonCalc(self):
        talbe.set_precision(10)
        rows = [['INDEX', 'X', 'F(X)', 'SUM']]
        index = 0
        simpsonNum = ceil(self.n / 2)
        denumertor = 4
        h = (self.boundary[1] - self.boundary[0]) / self.n
        i = self.boundary[0] + h
        sum = self.function.subs(x, self.boundary[0])
        print(f'n: {self.n}')
        while i < self.boundary[1]:
            temp = float(self.function.subs(x, i))
            sum += (denumertor * temp)
            rows.append([index, i, temp, sum])
            index += 1
            if denumertor == 4:
                denumertor = 2
            else:
                denumertor = 4
            i += h

        sum += self.function.subs(x, i)
        temp = float(self.function.subs(x, i))
        rows.append([index, i, temp, sum])
        talbe.add_rows(rows)
        print(talbe.draw())

        print(f'\nmultiply {float(sum)} with (1/3)*{h}: ')
        sum *= h * 1 / 3

        print(f'\n(*) the Integral between {self.boundary[0]} and {self.boundary[1]} is: {float(sum)} (*)')
        print(f'(*) the error is: {float(self.ErrorCalc(h))} (*)')

    def FindSlices(self):
        a = float(((self.boundary[1] - self.boundary[0]) ** 3) * self.example)
        b = float(12 * self.epsilon)
        return ceil(sqrt(abs(a / b)))

    def ErrorCalc(self,h):
        return (1/180)*(h**4)*(self.boundary[1]-self.boundary[0])*(self.function.subs(x,self.max))


mySimpson = Simpson()
mySimpson.SimpsonCalc()
