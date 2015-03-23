from sympy import symbols,sympify,latex
import matplotlib.pyplot as plt
import regression
def points2dPlot(xArr,yArr,scale=2,deg=2,typeOfPlot='regression'):
	if typeOfPlot == 'regression':
		X,Y = regression.linreg(xArr,yArr,deg,scale)
	elif typeOfPlot == 'spline':
		X,Y = regression.spline(xArr,yArr,scale)
	print X
	print Y
	plt.plot(X, Y, '-o')
	plt.show()
if __name__ == "__main__":
	X = map(int, raw_input().split())
	Y = map(int, raw_input().split())
	points2dPlot(X,Y)
		
