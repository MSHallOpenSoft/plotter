from scipy import linspace, polyval, polyfit, sqrt, stats, randn
from pylab import plot, title, show , legend
from scipy.interpolate import UnivariateSpline

def visualise(xarr, yarr, color='r'):
	plot(xarr, yarr, color)
	show()

def linreg(xarr, yarr, deg, scale):
	"""
	linear regression
	"""
	
	coeff = polyfit(xarr, yarr, deg)
	a = min(xarr)
	b = max(xarr)
	xs = linspace(a, b, scale * len(xarr))
	ys = polyval(coeff,xs)
	return xs, ys

def spline(xarr, yarr, scale):
	"""
	Univariate spline
	"""

	a = min(xarr)
	b = max(xarr)
	xs = linspace(a, b, scale * len(xarr))
	spl = UnivariateSpline(xarr,yarr)
	return xs,spl(xs)



# x = [0.1,0.2,0.3,0.4,0.5]
# y = [1,5,2,-1,4]
# print linreg(x, y, 2)
# xar, yar = linreg(x, y, 2)
# visualise(xar, yar, 'g')
