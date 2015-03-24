# from __future__ import unicode_literals
# import sympyParsing
# import sympy
# import sys
# import time
# import os
# import random
# import sympyPlot
# from matplotlib import animation
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib.backends import qt4_compat
# use_pyside = qt4_compat.QT_API == qt4_compat.QT_API_PYSIDE
# if use_pyside:
#     from PySide import QtGui, QtCore
# else:
#     from PyQt4 import QtGui, QtCore

# from numpy import arange, sin, pi
# from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure

# progname = os.path.basename(sys.argv[0])
# progversion = "0.1"

# x = sympy.symbols('x')
# y = sympy.symbols('y')
# z = sympy.symbols('z')


# class customLineEdit(QtGui.QLineEdit):
#     def __init__(self,parent=None):
#         self.parent=parent
#         QtGui.QLineEdit.__init__(self)
#         #self.text=""
#         self.returnPressed.connect(self.sg_returnPressed)

#     def sg_returnPressed(self):
#         print("wooooo")
#         print(self.text())
#         #self.parent.
#         txt=sympyParsing.exprLatex(str(self.text()))
#         changed=sympyParsing.symStr(str(self.text()))
#         print(changed)
#         foo=sympy.sympify(changed)
#         sympy_p1 = sympyPlot.plot3d_implicit1(foo,show=False,ax=self.parent.sc.ax)
#         sympy_p1.plotNow()
#         #z_arr = [x[0] for x in z_arr]
#         #print(len(x_arr),len(y_arr),len(z_arr))
#         #print(y_arr)
#         #y_arr=[i[0] for i in y_arr]

#         #self.parent.sc.ax.scatter(x_arr,y_arr,z_arr,zdir='r')

#         #self.parent.sc.ax.plot(x_arr, y_arr, zs=0, zdir='z', label='zs=0, zdir=z')
#         #self.parent.sc.ax.legend()
#         self.parent.sc.update_figure()






# class MplPlot3dCanvas(FigureCanvas):
#   def __init__(self,parent=None):
#       self.surfs = [] # [{"xx":,"yy:","val:"}]
#       self.fig = Figure()
#       self.fig.suptitle("this is  the  figure  title",  fontsize=12)
#       FigureCanvas.__init__(self, self.fig)
#       FigureCanvas.setSizePolicy(self,
#           QtGui.QSizePolicy.Expanding,
#           QtGui.QSizePolicy.Expanding)
#       FigureCanvas.updateGeometry(self)
#       self.ax = self.fig.add_subplot(111, projection='3d')
#       #self.ax = Axes3D(self.fig) # Canvas figure must be created for mouse rotation
#       self.ax.set_xlabel('row (m CCD)')
#       self.ax.set_ylabel('col (m CCD)')
#       self.ax.set_zlabel('Phi (m)')
#       self.format_coord_org = self.ax.format_coord
#       self.ax.format_coord = self.report_pixel
#       self.ax.view_init(elev=45,azim=45)
#       self.ax.dist=20
#         # Clear figure
#       #self.fig.clear()
#         # Set figure title
#       #self.fig.suptitle('$\\int \\sqrt{\\frac{1}{x}}\\, dx$', x=0.0, y=0.5,  horizontalalignment='left', verticalalignment='center')

#       #timer = QtCore.QTimer(self)
#       #timer.timeout.connect(self.update_figure)
#       #timer.start(100)
#   def update_figure(self):
#       #print(time.localtime())
#       #self.ax.dist+=1
#       #self.ax.azim=(self.ax.azim+5)%360
#       self.draw()


#   def report_pixel(self, xd, yd):
#       s = self.format_coord_org(xd, yd)
#       s = s.replace(",", " ")
#       return s

#   def update_view(self):

#       print("boo")
#       self.draw()
# #      for plt in self.plots:
#               ## del plt
#           #self.ax.collections.remove(plt)
#           #self.plots = []
#           #for surf in self.surfs:
#               #plt = self.ax.plot_surface(surf["xx"], surf["yy"], surf["val"], rstride=5, cstride=5, cmap=cm.jet, linewidth=1, antialiased=True)
#       #        self.plots.append(plt)
#           #self.draw()


# #class MplPlot3dView(QWidget):
#     #def __init__(self, parent = None):
#        #super(MplPlot3dView, self).__init__(parent)
#        #self.canvas = MplPlot3dCanvas()
#        #self.toolbar = NavigationToolbar(self.canvas, self.canvas)
#        #self.vbox = QVBoxLayout()
#        #self.vbox.addWidget(self.canvas)
#        #self.vbox.addWidget(self.toolbar)
#        #self.setLayout(self.vbox)
# #       self.to_update = False

# class ApplicationWindow(QtGui.QMainWindow):
#     def __init__(self):
#         QtGui.QMainWindow.__init__(self)
#         self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
#         self.setWindowTitle("application main window")

#         self.file_menu = QtGui.QMenu('&File', self)
#         self.file_menu.addAction('&Quit', self.fileQuit,
#                                  QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
#         self.menuBar().addMenu(self.file_menu)

#         self.help_menu = QtGui.QMenu('&Help', self)
#         self.menuBar().addSeparator()
#         self.menuBar().addMenu(self.help_menu)

#         self.help_menu.addAction('&About', self.about)

#         self.main_widget = QtGui.QWidget(self)

#         l = QtGui.QVBoxLayout(self.main_widget)
#         textbox=customLineEdit(self)
#         sc = MplPlot3dCanvas(self.main_widget)
#         l.addWidget(sc)
#         l.addWidget(textbox)
#         self.sc=sc
#         self.main_widget.setFocus()
#         self.setCentralWidget(self.main_widget)

#         self.statusBar().showMessage("All hail matplotlib!", 2000)

#     def fileQuit(self):
#         self.close()
#     def animate(i):
#         self.ac.ax.view_init(elev=10., azim=i)

#     def closeEvent(self, ce):
#         self.fileQuit()

#     def about(self):
#         # Animate
#         print("woo")
#         #self.sc.update_view()
#         #QtGui.QMessageBox.about(self, "About",
# #"""embedding_in_qt4.py example
# #Copyright 2005 Florent Rougon, 2006 Darren Dale

# #This program is a simple example of a Qt4 application embedding matplotlib
# #canvases.

# #It may be used and modified with no restriction; raw copies as well as
# #modified versions may be distributed without limitation."""
# #)


# qApp = QtGui.QApplication(sys.argv)

# aw = ApplicationWindow()
# aw.setWindowTitle("%s" % progname)
# aw.show()
# #for ii in xrange(0,360,1):
#         #aw.sc.ax.view_init(elev=10., azim=ii)
# sys.exit(qApp.exec_())
# qApp.exec_()



#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we draw text in Russian azbuka.

author: Jan Bodnar
website: zetcode.com 
last edited: September 2011
"""

import sys
from PyQt4 import QtGui, QtCore

import numpy as np
import sympyParsing
from sympy import symbols,sympify,lambdify
from sympy.plotting.experimental_lambdify import vectorized_lambdify,experimental_lambdify




class Example(QtGui.QWidget):
    
    def __init__(self,strr):
        super(Example, self).__init__()
        self.str_expr=strr
        self.x = symbols('x')
        self.expr = sympify(sympyParsing.symStr(self.str_expr))
        self.initUI()

        
    def initUI(self):      

        
        self.setGeometry(100, 100,800,800)
        self.setWindowTitle('Drawing Line')
        self.show()

    def paintEvent(self, event):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.OwnPlot(event, qp,-40,40,-40,40)
        qp.end()
    def OwnPlot(self, event,qp,xStart=-10,xEnd=10,yStart=-10,yEnd=10,NopMul=800):
        Nop=NopMul/(max(xEnd,yEnd)-min(xStart,yStart))
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setPen(QtGui.QColor(168, 34, 3))

        xArr=np.ogrid[xStart:xEnd:100j]
        xArr1=np.array(xArr, dtype=float)
        # print x
        f = lambdify([self.x], self.expr, "numpy")
        # f = vectorized_lambdify((x), expr)
        print 'asdf'

        # y=xArr
        # for i in xrange(len(xArr)):
        #   y[i]=-1*expr.subs(x, xArr[i])
        # print 'lol',f
        y= f(xArr1)
        print y
        for i in xrange(len(y)):
          y[i]=-1*y[i]
        print xArr
        xInitStart=-1*min(xStart,yStart)
        print xInitStart
        xStart+=(xInitStart)
        xEnd+=(xInitStart)
        yEnd+=(xInitStart)
        yStart+=(xInitStart)
        print xStart,xEnd,yStart,yEnd
        for i in xrange(len(xArr)):
          xArr[i]+=xInitStart
        for i in xrange(len(y)):
          y[i]+=xInitStart
        qp.drawLine(xStart*Nop,xInitStart*Nop,xEnd*Nop,xInitStart*Nop)
        qp.drawLine(xInitStart*Nop,yStart*Nop,xInitStart*Nop,yEnd*Nop)
        # qp.drawLine(0,0,1000,100)
        qp.setPen(QtGui.QColor(25, 34, 3))
        for i in xrange(1,len(xArr)):
          if y[i]>(yEnd*Nop) or y[i]<(yStart*Nop) or np.isnan(y[i]) or np.isnan(y[i-1]):
            print y[i]
            continue
          # print xArr[i],y[i]
          qp.drawLine(xArr[i-1]*Nop,y[i-1]*Nop,xArr[i]*Nop,y[i]*Nop)
          # arc = C.create_line(xArr[i-1]*Nop,y[i-1]*Nop,xArr[i]*Nop,y[i]*Nop,fill='red')


        # self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):
      
        qp.setPen(QtGui.QColor(168, 34, 3))
        qp.setFont(QtGui.QFont('Decorative', 10))
        # qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)        
        qp.drawLine(0,0,100,100)
                
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    strr=raw_input()
    ex = Example(strr)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()