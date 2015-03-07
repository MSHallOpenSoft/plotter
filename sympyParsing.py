from sympy import *
import numpy
x = symbols('x')
y = symbols('y')
z = symbols('z')
# expr = x**3 + 4*x*y - z
# print expr.subs([(x, 2),  (z, 0)])



print 'Enter the expression: ' ,

str_expr = raw_input()
indOfEq=str_expr.find('=')
indOfDEq=str_expr.find('==')

if indOfEq!=-1 and indOfEq!=indOfDEq:
	splitExpr=str_expr.split('=')
	if len(splitExpr)==2:
		combinedStr=splitExpr[0] + ' - ('+splitExpr[1]+')'
		expr=sympify(combinedStr)
elif indOfEq==-1:
	expr = sympify(str_expr)	#Parses the string to sympy object



print expr
print 'Enter the values of x: ' ,

num = map(int, raw_input().split())
numArr=numpy.array(num)
f = lambdify(x, expr, "numpy")
findyRoot=f(numArr)
if type(findyRoot) !='numpy.ndarray':
	print solve(findyRoot,y)
else:
	for exp in findyRoot:
		print solve(exp,y)
	
# val=expr.subs(x, num[0])
# print 'The value of expr at that num. is: ',val