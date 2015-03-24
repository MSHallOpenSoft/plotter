import Tkinter
import tkMessageBox
import numpy as np
import sympyParsing
from sympy import symbols,sympify,lambdify
from sympy.plotting.experimental_lambdify import vectorized_lambdify,experimental_lambdify


def OwnPlot(str_expr,xStart=-10,xEnd=10,yStart=-10,yEnd=10,Nop=50):
	x = symbols('x')
	expr = sympify(sympyParsing.symStr(str_expr))
	print expr
	top = Tkinter.Tk()

	C = Tkinter.Canvas(top,  height=800, width=800)
	C.configure(scrollregion=(-8*Nop, -8*Nop, 2*Nop, 6*Nop))
	# coord = 10, 50, 240, 210
	# arc = C.create_line(0,0,100,100)

	# def F(x):
	# 	return x**3 
	xArr=np.ogrid[xStart:xEnd:100j]
	xArr1=np.array(xArr, dtype=float)
	# print x
	print xArr
	print 'uff',expr
	f = lambdify([x], expr, "numpy")
	# f = vectorized_lambdify((x), expr)
	print 'asdf'

	# y=xArr
	# for i in xrange(len(xArr)):
	# 	y[i]=-1*expr.subs(x, xArr[i])
	# print 'lol',f
	y= f(xArr1)
	print y
	print xArr
	for i in xrange(len(y)):
		y[i]=-1*y[i]
	
	print xStart
	# print xStart
	arc = C.create_line(xStart*Nop,0,xEnd*Nop,0,fill='green')
	arc = C.create_line(0,yStart*Nop,0,yEnd*Nop,fill='green')
	
	for i in xrange(1,len(xArr)):
		if y[i]>(yEnd*Nop) or y[i]<(yStart*Nop) or np.isnan(y[i]) or np.isnan(y[i-1]):
			print y[i]
			continue
		# print xArr[i],y[i]
		arc = C.create_line(xArr[i-1]*Nop,y[i-1]*Nop,xArr[i]*Nop,y[i]*Nop,fill='red')
	
	# arc = C.create_line(-100,200,100,-200,fill='blue')
	C.pack()
	top.mainloop()

if __name__ == "__main__":
	exp_str=raw_input()
	OwnPlot(exp_str)
	# print 'Enter x,y range: '
	# xArr = map(int, raw_input().split())
	# Y = map(int, raw_input().split())
