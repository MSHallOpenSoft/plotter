import numpy as np
import scipy
from sympy import symbols,sympify,latex,lambdify
import sympyParsing
from mayavi import mlab
t = symbols('t')

# X = 100 * scipy.rand(100, 3)

def mayaviParam3d(str_expr_x,str_expr_y,str_expr_z):
	expr_x=sympyParsing.symStr(str_expr_x)
	expr_y=sympyParsing.symStr(str_expr_y)
	expr_z=sympyParsing.symStr(str_expr_z)

	print expr_x,expr_y,expr_z


	# x_start = -10
	# x_end = 10
	# no_x_points=complex(0,100)
	# y_start = -10
	# y_end = 10
	# no_y_points=complex(0,100)
	# z_start = -10
	# z_end = 10
	# no_z_points=complex(0,100)
	# X,Y,Z=np.ogrid[x_start:x_end:no_x_points , y_start:y_end:no_y_points , z_start:z_end:no_z_points]
	T=np.ogrid[-10:10:200j]
	f = lambdify((t), expr_x,"numpy")
	xArr=f(T)
	f1 = lambdify((t), expr_y,"numpy")
	yArr=f1(T)
	f2 = lambdify((t), expr_z,"numpy")
	zArr=f2(T)
	print xArr,yArr,zArr
	# Visualize the points
	pts = mlab.points3d(xArr, yArr, zArr, zArr, scale_mode='none', scale_factor=0.2)

	# Create and visualize the mesh
	mesh = mlab.pipeline.delaunay2d(pts)
	surf = mlab.pipeline.surface(mesh)

	# mlab.view(47, 57, 8.2, (0.1, 0.15, 0.14))
	mlab.show()

if __name__=="__main__":
	print 'Enter 3 expressions: '
	expr1=raw_input()
	expr2=raw_input()
	expr3=raw_input()
	mayaviParam3d(expr1,expr2,expr3)


# import numpy as np

# # Create data with x and y random in the [-2, 2] segment, and z a
# # Gaussian function of x and y.
# np.random.seed(12345)
# x = 4 * (np.random.random(500) - 0.5)
# y = 4 * (np.random.random(500) - 0.5)


# def f(x, y):
#     return np.exp(-(x ** 2 + y ** 2))

# z = f(x, y)

# print x,y,z
# from mayavi import mlab
# mlab.figure(1, fgcolor=(0, 0, 0), bgcolor=(1, 1, 1))

# # Visualize the points
# pts = mlab.points3d(x, y, z, z, scale_mode='none', scale_factor=0.2)

# # Create and visualize the mesh
# mesh = mlab.pipeline.delaunay2d(pts)
# surf = mlab.pipeline.surface(mesh)

# mlab.view(47, 57, 8.2, (0.1, 0.15, 0.14))
# mlab.show()