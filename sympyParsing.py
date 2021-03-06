from sympy import symbols,sympify,latex
import sympyPlot_implicit

import numpy
x = symbols('x')
y = symbols('y')
z = symbols('z')
# print expr.subs([(x, 2),  (z, 0)])
# Adaptive Mesh

def symStr(str_expr):
        # print('--------------')
        # print(str_expr)
        # print('************')
        # print(str_expr)
	indOfXor=str_expr.find('^')

	# Changes x^2 to x**2
	if indOfXor!=-1:
		str_expr=str_expr.replace("^","**")

	# Changes x=y to x-(y)... as sympy accepts only expressions which are equated to 0
	indOfEq=str_expr.find('=')
	indOfDEq=str_expr.find('==')
	if indOfEq!=-1 and indOfEq!=indOfDEq:
		splitExpr=str_expr.split('=')
		if len(splitExpr)==2:
			str_expr=splitExpr[0] + ' - ('+splitExpr[1]+')'


	# Changes xy,yz,zx.. ,x(,..,x).. to x*y,...x*(,...)*x
	strLis=list(str_expr)
	i=1
	while i<len(strLis):
		if (strLis[i]=='x' or strLis[i]=='z' or strLis[i]=='y' ) and (strLis[i-1]=='x' or strLis[i-1].isdigit() or  strLis[i-1]=='z' or strLis[i-1]=='y'):
			strLis.insert(i,'*')
		if (strLis[i]=='x' or strLis[i].isdigit() or strLis[i]=='z' or strLis[i]=='y') and (strLis[i-1]==')'):
			strLis.insert(i,'*')
		if (strLis[i]=='(') and (strLis[i-1]=='x' or strLis[i-1].isdigit() or strLis[i-1]=='z' or strLis[i-1]=='y'):
			strLis.insert(i,'*')
		i=i+1
	return ''.join(strLis)

def exprParseSolve2D(str_expr,x_start,x_end,x_step=0.02):

	str_expr = symStr(str_expr)
	expr = sympify(str_expr)	#Parses the string to sympy object

	# print 'Sympy expression is: ',expr
	xArr=numpy.arange(x_start, x_end,x_step)
	f = lambdify(x, expr, "numpy")
	findyRoot=f(xArr)
	# if type(findyRoot) !='numpy.ndarray':
	# 	print solve(findyRoot,y)
	# else:
	# print findyRoot
	yArr=[]
	for exp in findyRoot:
		yArr.append( solve(exp,y) )
	# print xArr
	# print yArr

	return xArr,yArr
def exprParseSolve3D(str_expr,x_start,x_end,y_start,y_end,x_step=0.02,y_step=0.02):
	str_expr = symStr(str_expr)
	expr = sympify(str_expr)	#Parses the string to sympy object

	# print 'Sympy expression is: ',expr
	xArr=numpy.arange(x_start, x_end,x_step)
	yArr=numpy.arange(y_start, y_end,y_step)
	f = lambdify(x, expr, "numpy")
	findyRoot=f(xArr)
	zArr=[]
	for exp in findyRoot:
		# exp=exp.subs(y,x)
		f2=lambdify(y,exp,"numpy")
		findyRoot2=f2(yArr)
		for exp2 in findyRoot2:
			zArr.append( solve(exp2,z) )
	return xArr,yArr,zArr
	

def exprLatex(str_expr):
	str_expr = symStr(str_expr)
	expr = sympify(str_expr)
	return latex(expr)


# if __name__ == "__main__":
# 	print 'Enter the expression: ' ,

# 	str_expr = raw_input()

# 	print exprParseSolve2D(str_expr,1,4)
# 	print exprParseSolve3D(str_expr,1,1.06,1,1.06)

def plot_implicit_3d(expr, x_var=None, y_var=None, z_var_start=-5,z_var_end=5, **kwargs):
    # np = import_module('numpy')
    z=symbols('z')
    zArr=numpy.linspace(z_var_start, z_var_end,num=50)
    # mesh_z=np.meshgrid(zArr)
    print (expr)
    # f = lambdify(z, expr)
    f = lambdify(z, expr , "numpy")
    zExpr = f(zArr)
    xArrF=[]
    zArrF=[]
    yArrF=[]
    
    for i in xrange(0,len(zExpr)):
    	xArrL,yArrL=sympyPlot_implicit.plot_implicit_3d(zExpr[i],show=False)
    	zArrL=[zArr[i]] * len(xArrL)
    	xArrL=numpy.array(xArrL)
    	yArrL=numpy.array(yArrL)
    	zArrL=numpy.array(zArrL)
    	xArrF.append(xArrL)
    	yArrF.append(yArrL)
    	zArrF.append(zArrL)
    mesh_z=numpy.array(zArrF)
    mesh_y=numpy.array(yArrF)
    mesh_x=numpy.array(xArrF)
    print type(mesh_x)
    print type(mesh_x[0])
    print mesh_x
    # fig=matplotlib.figure.Figure()
    # ax=fig.add_subplot(111,projection='3d')
    # # sympy.plotting.plot3d
    # ax.plot_surface(mesh_x,mesh_y,mesh_z)
    # fig.show()
    return mesh_x,mesh_y,mesh_z
	# print len(xArrF)
	# print len(zArrF)


    # for i in xrange(1,len(zExpr)):
    # 	p.extend(sympyPlot_implicit.plot_implicit(zExpr[i],show=False))
    # 	break
    # p.show()



if __name__ == "__main__":
    print ('Enter the expression: ' )
    expr_str=raw_input()
    q=plot_implicit_3d(sympify(expr_str))




# val=expr.subs(x, num[0])
# print 'The value of expr at that num. is: ',val
