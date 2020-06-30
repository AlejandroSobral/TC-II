
from scipy import signal

from sympy import *


from splane import pzmap, grpDelay, bodePlot


num=[1,0,0,0,0]
den = [1,1.87,6.71,7.48,12.43,7.48,6.71,1.87,1]

sys=signal.TransferFunction(num, den)

bodePlot(sys)

pzmap(sys)

grpDelay(sys);

"""
S = symbols('S')

este seria el caso de Wb

print(expand((S**2+S*1.93+ 1)*(S**2+S*1.414+ 1)*(S**2+S*0.518+ 1)))
num = [1]
den = [1,3.86,7.46,9.137,7.46,3.862,1]
print("Complete")


"""
"""

S = symbols('S')

"este seria el caso de no aplicar el wb y conseguir el diagrama de polos y ceros con wo=8.2"
num=[8.2]
den = [1,4.64,10.7564,15.80848,15.489216,9.621504,2.985984]
print(expand((S**2+S*2.32+ 1.2**2)*(S**2+S*1.7+ 1.2**2)*(S**2+S*0.62+ 1.2**2)))
print("Complete")
"""

"""
S, J = symbols('S J')
"Pasa banda N=4"
num=[1,0,0,0,0,0,0,0,0]
den = [591.72,0,4733.76,0,16568.16,0,33136.32,0,41421.4,0,33136.32,0,16568.16,0,4733.76,0,591.72]
"este seria es un caso similar al de wb que lo pase por "
"J=((S**2 +1)/0.45*S)"
"print(simplify(J**2 +0.54*J+1)*(J**2 +1.33*J+1))"
print(expand((S**4 +0.54*S**3 +3*S**2 + 0.54*S +1)*(S**4 +1.33*S**3 +3*S**2 + 1.33*S +1)))
print("Complete")
"""

"""
S = symbols('S')
"Pasabajos n=5"
num=[1,0,0,0,0,0]
den = [1,3.238,5.239,5.239,3.238,1]
"este seria es un caso similar al de wb que lo pase por "

"print(expand((S+1)*(S**2+0.618*S+1)*(S**2+1.62*S+1)))"
print(simplify(1/((1/S)**5 + 3.238*(1/S)**4 + 5.23916*(1/S)**3 + 5.23916*(1/S)**2 + 3.238*(1/S) + 1)))
print("Complete")
"""

