import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans


def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.exp(x**2)*x, (x,0, 2))
    return ans

def my_solution():
    A = np.array( [[1,1,1,1,1,1,1,1,1,1], [1,2,1,1,1,1,1,1,1,1],
[1,1,2,1,1,1,1,1,1,1],[1,1,1,2,1,1,1,1,1,1],[1,1,1,1,2,1,1,1,1,1],
[1,1,1,1,1,2,1,1,1,1],[1,1,1,1,1,1,2,1,1,1],[1,1,1,1,1,1,1,2,1,1],
[1,1,1,1,1,1,1,1,2,1],[1,1,1,1,1,1,1,1,1,2]] )
    b = np.array([55,57,58,59,60,61,62,63,64,65])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1303042
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
