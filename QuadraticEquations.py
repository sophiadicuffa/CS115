'''
Sophia DiCuffa
4/21/22
I pledge my honor that I've abided by the stevens honor code
'''


import math # need for sqrt function

class QuadraticEquation:
    def __init__(self, a, b, c): # takes three values and converts to floats
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

      # Methods for calculating  
    def discriminant(self):
        return ((self.b)**2) - (4 * self.a * self.c)

    def root1(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.b + math.sqrt(self.discriminant())) / (2 * self.a)
    def root2(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.b - math.sqrt(self.discriminant())) / (2 * self.a)
       
    def __str__ (self):
        # converting to string for concatination
        a1 = str(self.a)
        b1 = str(self.b)
        c1 = str(self.c)
        #soo many conditions - there's prob an easier way to do this that idk
        if self.a < 0:
            a1 = '-'
        if self.a == 1:
            a1 = ''
        if self.b == 1 or self.b == -1:
            b1 = ''
        if self.b < 0 and self.c > 0:
            if b1 == '':
                return a1 + 'x^2 - ' + b1 + 'x + ' + c1 + ' = 0'
            else:
                b1 = str(abs(self.b))
                return a1 + 'x^2 - ' + b1 + 'x + ' + c1 + ' = 0'
        if self.c < 0 and self.b > 0:
            c1 = str(abs(self.c))
            return a1 + 'x^2 + ' + b1 + 'x - ' + c1 + ' = 0'
        if self.b < 0 and self.c < 0:
            b1 = str(abs(self.b))
            c1 = str(abs(self.c))
            return a1 + 'x^2 - ' + b1 + 'x - ' + c1 + ' = 0'
        if self.b == 0 and self.c == 0:
            return a1 + 'x^2' + ' = 0'
        if self.b == 0:
            c1 = str(abs(self.c))
            return a1 + 'x^2 - ' + c1 + ' = 0'
        if self.c == 0:
            b1 = str(abs(self.b))
            return a1 + 'x^2 + ' + b1 + 'x = 0'
        return a1 + 'x^2 + ' + b1 + 'x + ' + c1 + ' = 0'
    
a = QuadraticEquation(9.0, -1, 81.0)
print (a.__str__()) # 9.0x^2 - x + 81.0 = 0, one test that doesn't work

