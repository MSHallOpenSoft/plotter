import numpy as np
from mayavi import mlab
from sympy import symbols,sympify
from sympy.plotting.experimental_lambdify import (vectorized_lambdify)
import sympyParsing
x = symbols('x')
y = symbols('y')
z = symbols('z')

# a, b, c = np.ogrid[-3:3:100j, -3:3:100j, -3:3:100j]
# str_expr=raw_input()
# expr = sympify(sympyParsing.symStr(str_expr))
# f = vectorized_lambdify((x, y,z), expr)
# print f(a,b,c)


# contour3d=mlab.contour3d(f(a,b,c), contours = [0])
# mlab.outline(contour3d, color=(.7, .7, .7))
# mlab.axes(color=(.7, .7, .7))
# mlab.show()


def mayavi_implicit_3d(str_expr,x_start=-10,x_end=10,no_x_points=100,y_start=-10,y_end=10,no_y_points=100,z_start=-10,z_end=10,no_z_points=100):
    expr = sympify(sympyParsing.symStr(str_expr))
    no_x_points=complex(0,no_x_points)
    no_y_points=complex(0,no_y_points)
    no_z_points=complex(0,no_z_points)

    X,Y,Z=np.ogrid[x_start:x_end:no_x_points , y_start:y_end:no_y_points , z_start:z_end:no_z_points]
    print X
    print Y
    print Z
    f = vectorized_lambdify((x, y,z), expr)

    print f(X,Y,Z)
    contour3d=mlab.contour3d(f(X,Y,Z), contours = [0])
    mlab.outline(contour3d, color=(.7, .7, .7))
if __name__ == "__main__":
    print ('Enter the expression: ' )
    expr_str=raw_input()
    mayavi_implicit_3d(expr_str)
    expr_str=raw_input()
    mayavi_implicit_3d(expr_str)
    mlab.axes(color=(.7, .7, .7))
    mlab.show()