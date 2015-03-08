from sympy import *
import numpy
x = symbols('x')
y = symbols('y')
z = symbols('z')
# print expr.subs([(x, 2),  (z, 0)])
# Adaptive Mesh

def symStr(str_expr):
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
		if (strLis[i]=='x' or strLis[i]=='z' or strLis[i]=='y' or strLis[i].isdigit()) and (strLis[i-1]=='x' or strLis[i-1].isdigit() or  strLis[i-1]=='z' or strLis[i-1]=='y'):
			strLis.insert(i,'*')
		if (strLis[i]=='x' or strLis[i].isdigit() or strLis[i]=='z' or strLis[i]=='y') and (strLis[i-1]==')'):
			strLis.insert(i,'*')
		if (strLis[i]=='(') and (strLis[i-1]=='x' or strLis[i-1].isdigit() or strLis[i-1]=='z' or strLis[i-1]=='y'):
			strLis.insert(i,'*')
		i=i+1
	return ''.join(strLis)

def exprParseSolve(str_expr,x_start,x_end,x_step=0.02):

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

def exprLatex(str_expr):
	str_expr = symStr(str_expr)
	expr = sympify(str_expr)
	return latex(expr)


if __name__ == "__main__":
	print 'Enter the expression: ' ,

	str_expr = raw_input()

	exprParseSolve(str_expr,1,4)





# val=expr.subs(x, num[0])
# print 'The value of expr at that num. is: ',val