import ast
import compiler
import sys
class CodePrinter:
    def __init__(self):
        self.src = ''
 
    def visitName(self,t):
        self.src += t.name + "++"
 
    def visitConst(self,t):
        self.src += str(t.value)+ "++"
 
    def visitStmt(self, t):
        for i in t:
            a = pretty_print(i)
            self.src += a + ""
 
    def visitAssName(self, t):
        self.src += t.name + " = "
 
def pretty_print(node):
    myvisitor = CodePrinter()
    # compiler.walk return the visitor instance : 2nd arg
    return compiler.walk(node, myvisitor).src

flist = ["Abs","acos","acosh","acot","acoth","arg","asin","asinh","atan","atan2","atanh","ceiling","conjugate","cos","cosh","cot","coth","exp","ExprCondPair","floor","HyperbolicFunction","IdentityFunction","im","LambertW","log","Min","Max","Piecewise","re","root","RoundFunction","sin","sinh","sqrt","sign","tan","tanh"]

def get_var_par (eq):
	'''
	This is the main function that parses the equation to 
	finds out the parameters and variables present in it.

	'''
	eq = eq.replace ("=","+")
	node= compiler.parse( eq )

	parastr = pretty_print(node)
	str_list = parastr.split("++")
	para = filter(None, str_list) 

	para = [x for x in para if x.isdigit()==False and x not in flist]
	par = []
	for str in para:
		for i in range(len(str)):
			par.append (str[i])
	par = list(set(par))

	vars = ["x","y","z"]
	out = {}
	out["parameters"] = [x for x in par if x not in vars]
	out["variables"] = [x for x in par if x in vars]

	return (out)

while (True):

	eq = raw_input("Enter the equation? \n")

	# take command line input
	# eq = sys.argv[1]

	print get_var_par(eq)
